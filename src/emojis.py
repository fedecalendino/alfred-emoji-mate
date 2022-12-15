import os
from uuid import uuid4
from collections import defaultdict

from emoji import EMOJI_DATA

VALID_SKIN_TONES = {
    "": "",
    "light": "_light_skin_tone",
    "medium-light": "_medium-light_skin_tone",
    "medium": "_medium_skin_tone",
    "medium-dark": "_medium-dark_skin_tone",
    "dark": "_dark_skin_tone",
}


def clean(name: str) -> str:
    return name.strip().replace("_", " ").replace("-", " ").replace(":", "").lower()


def build():
    normal_emojis = defaultdict(list)
    skin_toned_emojis = defaultdict(list)
    aliased_emojis = defaultdict(list)

    skin_tone = os.getenv("SKIN_TONE", "light").lower()
    skin_tone = VALID_SKIN_TONES.get(skin_tone)

    # sort emojis from olders to newest
    for emoji, data in sorted(EMOJI_DATA.items(), key=lambda kv: kv[1]["E"]):
        if data["status"] != 2:  # fully_qualified
            continue

        name = data["en"]

        if "flag_for" in name:
            continue

        prioritize_skin_tone = False

        # change or skip unwanted skin tones
        if "skin_tone" in name:
            if skin_tone not in name:
                continue

            name = name.replace(skin_tone, "", 1)
            prioritize_skin_tone = True

        name = clean(name)
        code = f"{emoji}\U0000FE0F"
        uuid = uuid4()

        if prioritize_skin_tone:
            # reuse the same uuid as the non skin toned version
            normal = normal_emojis.get(name)

            if normal:
                uuid = normal[0][0]

            skin_toned_emojis[name].append((uuid, code))
        else:
            normal_emojis[name].append((uuid, code))

        # add all aliases for that specific emoji
        for alias in data.get("alias", []):
            if "flag_for" in alias:
                continue

            aliased_emojis[uuid].append(clean(alias))

    # replace the selected skin toned emojis over the non skin toned
    normal_emojis.update(skin_toned_emojis)

    for name, codes in normal_emojis.items():
        for uuid, code in codes:
            yield name, code

            for alias in aliased_emojis.get(uuid, []):
                yield alias, code


emojis = list(build())
