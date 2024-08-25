from difflib import SequenceMatcher
from typing import Iterable, Tuple

from emojis import emojis


def match(s1, s2):
    ratio = SequenceMatcher(None, s1, s2).ratio()

    if s2 in s1:
        ratio *= 3

    return 100 * ratio


def search_by_text(text: str, limit: int = 10):
    return search(text, limit, index=0, min_ratio=1)


def search_by_emoji(text: str, limit: int = 10):
    return search(text, limit, index=1, min_ratio=50.0)


def search(text: str, limit: int = 10, index: int = 0, min_ratio: float = 0):
    result = sorted(
        filter(
            lambda item: item[0] >= min_ratio,
            map(
                lambda item: (match(item[index], text), item),
                emojis,
            ),
        ),
        key=lambda item: item[0],
        reverse=True,
    )

    return list(result)[:limit]
