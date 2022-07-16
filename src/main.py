import sys
from difflib import SequenceMatcher

from emojis import emojis
from pyflow import Workflow


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


def main(workflow):
    text = workflow.args[0].lower()
    results = search(text, limit=20)

    for name, code in results:
        workflow.add_item(
            title=f"{code} {name}",
            arg=code,
            copytext=code,
            valid=True,
        )


if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
