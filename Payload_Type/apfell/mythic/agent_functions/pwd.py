from mythic_payloadtype_container.MythicCommandBase import *
import sys
from mythic_payloadtype_container.MythicResponseRPC import *


class PwdArguments(TaskArguments):
    def __init__(self, command_line):
        super().__init__(command_line)
        self.args = {}

    async def parse_arguments(self):
        pass


class PwdCommand(CommandBase):
    cmd = "pwd"
    needs_admin = False
    help_cmd = "pwd"
    description = "Prints the current working directory for the agent"
    version = 1
    is_exit = False
    is_file_browse = False
    is_process_list = False
    is_download_file = False
    is_remove_file = False
    is_upload_file = False
    author = "@its_a_feature_"
    attackmapping = ["T1083"]
    argument_class = PwdArguments

    async def create_tasking(self, task: MythicTask) -> MythicTask:
        resp = await MythicResponseRPC(task).register_artifact(
            artifact_instance="fileManager.currentDirectoryPath",
            artifact_type="API Called",
        )
        return task

    async def process_response(self, response: AgentResponse):
        pass
