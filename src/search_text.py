import sys

from pyflow import Workflow

import utils


def main(workflow: Workflow):
    text = " ".join(workflow.args).lower()
    results = utils.search_by_text(text, limit=20)

    for ratio, (name, code) in results:
        workflow.new_item(
            title=f"{code} {name}",
            arg=f"copy:{code}",
            copytext=code,
            valid=True,
        ).set_icon_file(
            path=None,
        ).set_cmd_mod(
            arg=f"paste:{code}",
            subtitle="Paste emoji to frontmost app",
        ).set_alt_mod(
            subtitle=f"Match: {ratio:.2f}",
        )



if __name__ == "__main__":
    wf = Workflow()
    wf.run(main)
    wf.send_feedback()
    sys.exit()
