from pyflow.testing import WorklowTestCase

from main import main


class TestWorkflow(WorklowTestCase):
    def test_run(self):
        envs = {}

        args = []

        workflow = self.workflow(**envs)
        feedback = self.run_workflow(workflow, main, *args)
