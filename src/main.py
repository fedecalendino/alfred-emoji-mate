import sys
from workflow import Workflow

from emojis import EMOJIS
from mate import search


def main(workflow):
    text = workflow.args[0].lower()
    results = search(text)

    if not results:
        title = u'{} No emojis found for "{}"'.format(EMOJIS['cross mark'], text)
        wf.add_item(title=title, valid=False)
    else:
        for name, code in search(text, limit=10):
            title = u'{}{} {}'.format(code, u'\U0000FE0F', name)

            wf.add_item(title=title, arg=code, copytext=code, icon='icons/none.png', valid=True)

    workflow.send_feedback()


if __name__ == u"__main__":
    wf = Workflow()
    sys.exit(wf.run(main))
