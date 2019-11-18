from fuzzywuzzy import fuzz

from emojis import EMOJIS


def match(name, text):
    return fuzz.ratio(name, text) * (2 if text in name else 1)


def search(text, limit=0):
    results = list(
        sorted(
            filter(
                lambda item: match(item[0], text) > 50,
                EMOJIS.items(),
            ),
            key=lambda item: match(item[0], text),
            reverse=True
        )
    )

    control = {}
    uniques = []

    for kv in results:
        code = kv[1]

        if code not in control:
            control[code] = None
            uniques.append(kv)

    return uniques if not limit else uniques[:limit]
