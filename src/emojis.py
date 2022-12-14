import os

from aliases import CUSTOM_EMOJI_ALIAS
from emoji import EMOJI_DATA

VALID_SKIN_TONES = {
    "": "",
    "light": "_light_skin_tone",
    "medium-light": "_medium-light_skin_tone",
    "medium": "_medium_skin_tone",
    "medium-dark": "_medium-dark_skin_tone",
    "dark": "_dark_skin_tone",
}


def _main_emojis():
    main_emojis = {}

    skin_tone = os.getenv("SKIN_TONE", "").lower()
    skin_tone = VALID_SKIN_TONES.get(skin_tone)

    skin_tones = {}

    for emoji, data in EMOJI_DATA.items():
        name = data["en"]

        if "flag_for" in name:
            continue

        save_skin_tone = False

        if name.endswith("skin_tone:"):
            if not skin_tone:
                continue

            if not name.endswith(skin_tone + ":"):
                continue

            name = name.replace(skin_tone, "")
            save_skin_tone = True

        name = name.lower().replace("_", " ").replace("-", " ").replace(":", "").strip()
        code = "{}\U0000FE0F".format(emoji)

        if save_skin_tone:
            skin_tones[name] = code
        else:
            main_emojis[name] = code

    main_emojis.update(skin_tones)
    return main_emojis


def _build():
    main_emojis = _main_emojis()
    final_emojis = list(map(tuple, main_emojis.items()))

    for name, aliases in CUSTOM_EMOJI_ALIAS.items():
        for alias in aliases:
            if name in main_emojis:
                final_emojis.append((alias, main_emojis[name]))

    return final_emojis


emojis = _build()
