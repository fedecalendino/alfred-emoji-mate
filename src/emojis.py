import os
from uuid import uuid4
from collections import defaultdict

from emoji import EMOJI_DATA

VALID_SKIN_TONES = {
    "light": "_light_skin_tone",
    "medium-light": "_medium-light_skin_tone",
    "medium": "_medium_skin_tone",
    "medium-dark": "_medium-dark_skin_tone",
    "dark": "_dark_skin_tone",
}


def clean(name: str) -> str:
    return name.strip().replace("_", " ").replace("-", " ").replace(":", "").lower()


def build():
    names = defaultdict()
    normal_emojis = defaultdict(list)
    skin_toned_emojis = defaultdict(list)
    aliased_emojis = defaultdict(list)

    lang = os.getenv("LANG", "en").lower()[:2]

    skin_tone = os.getenv("SKIN_TONE") or ""
    skin_tone = VALID_SKIN_TONES.get(skin_tone.lower()) or ""

    # sort emojis from olders to newest
    for emoji, data in sorted(EMOJI_DATA.items(), key=lambda kv: kv[1]["E"]):
        if data["status"] != 2:  # fully_qualified
            continue

        if not data.get(lang):
            continue

        key = data["en"]

        if "flag_for" in key:
            continue

        prioritize_skin_tone = False

        # change or skip unwanted skin tones
        if "skin_tone" in key:
            if skin_tone not in key:
                continue

            key = key.replace(skin_tone, "", 1)
            prioritize_skin_tone = True

        key = clean(key)
        code = f"{emoji}\U0000FE0F"
        uuid = uuid4()

        if prioritize_skin_tone:
            # reuse the same uuid as the non skin toned version
            normal = normal_emojis.get(key)

            if normal:
                uuid = normal[0][0]

            skin_toned_emojis[key].append((uuid, code))
        else:
            normal_emojis[key].append((uuid, code))

        names[uuid] = clean(data[lang])

        # add all aliases for that specific emoji
        for alias in data.get("alias", []):
            if "flag_for" in alias:
                continue

            alias = clean(alias)

            if key != alias:
                aliased_emojis[uuid].append(alias)

    # replace the selected skin toned emojis over the non skin toned
    normal_emojis.update(skin_toned_emojis)

    for key, codes in normal_emojis.items():
        for uuid, code in codes:
            yield names[uuid], code

            if lang != "en":
                continue

            for alias in aliased_emojis.get(uuid, []):
                yield alias, code


emojis = list(build())
