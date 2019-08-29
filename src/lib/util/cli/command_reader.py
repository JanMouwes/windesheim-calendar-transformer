from typing import Dict


class CommandReader:
    _argv: [str] = []

    @staticmethod
    def infer_commands(commands) -> Dict[str, str]:
        def infer_command(command: str) -> [str, str]:
            [key, value] = command.split("=")

            return key[2::], value

        return dict(infer_command(arg) for arg in commands if len(arg.split("=")) is 2 and arg[0:2:1] == "--")

    @property
    def commands(self) -> Dict[str, str]:
        return self.infer_commands(self._argv)
