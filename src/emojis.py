from emoji import EMOJI_ALIAS_UNICODE

from custom import CUSTOM_EMOJI_ALIAS

DEFAULT_SKIN_TONE = "light_skin_tone"


def _emoji_filter(name):
    if "skin_tone" in name:
        return DEFAULT_SKIN_TONE in name

    if "flag_for" in name:
        return False

    return True


def _emoji_cleaner(name):
    return name\
        .lower()\
        .replace("_", " ")\
        .replace("-", " ")\
        .replace(":", "")


def _get_emojis():
    emojis = {
        _emoji_cleaner(name): code
        for name, code in EMOJI_ALIAS_UNICODE.items()
        if _emoji_filter(name)
    }

    for name, aliases in CUSTOM_EMOJI_ALIAS.items():
        for alias in aliases:
            if name in emojis:
                emojis[alias] = emojis[name]

    return emojis


EMOJIS = _get_emojis()
