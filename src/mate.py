# coding=utf-8

import sys

from workflow import Workflow

from search import search


def main(workflow):
    text = workflow.args[0].lower()
    results = search(text, limit=20)

    for name, code in results:
        title = u'{} {}'.format(code, name)
        wf.add_item(title=title, arg=code, copytext=code, icon='icons/none.png', valid=True)

    workflow.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
