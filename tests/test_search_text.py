from pyflow.testing import WorklowTestCase

from search_text import main


class TestMain(WorklowTestCase):
    def test_run(self):
        workflow = self.workflow()
        feedback = self.run_workflow(workflow, main, "fede")

        found = ""

        for item in feedback["items"]:
            found += item["arg"]

        self.assertEqual(found, "🆓️🐾️🇩🇪️🍳️☕️📒️🇸🇪️🫕️🔚️🐑️🐝️🛏️️👁️️😳️🪶️📁️🍺️📅️👀️🔥️")
