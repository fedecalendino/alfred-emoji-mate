from difflib import SequenceMatcher

from emojis import emojis


def match(s1, s2):
    ratio = SequenceMatcher(None, s1, s2).ratio()

    if s2 in s1:
        ratio *= 3

    return 100 * ratio


def search(text, limit=10):
    return list(
        sorted(
            emojis,
            key=lambda item: match(item[0], text),
            reverse=True,
        )
    )[:limit]

