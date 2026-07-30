from collections.abc import Callable

from .codegen import Instruction


class VirtualMachine:
    def __init__(
        self, output: Callable[[float], None] = print
    ) -> None:
        self.output = output
        self.stack: list[float] = []
        self.variables: dict[str, float] = {}

    def run(self, code: list[Instruction]) -> None:
        instruction_pointer = 0
        while True:
            instruction = code[instruction_pointer]
            instruction_pointer += 1
            opcode = instruction.opcode

            if opcode == "HALT":
                return
            if opcode == "PUSH":
                assert isinstance(instruction.argument, float)
                self.stack.append(instruction.argument)
            elif opcode == "LOAD":
                assert isinstance(instruction.argument, str)
                self.stack.append(self.variables[instruction.argument])
            elif opcode == "STORE":
                assert isinstance(instruction.argument, str)
                self.variables[instruction.argument] = self.stack.pop()
            elif opcode == "PRINT":
                self.output(self.stack.pop())
            else:
                self._binary_operation(opcode)

    def _binary_operation(self, opcode: str) -> None:
        right = self.stack.pop()
        left = self.stack.pop()
        operations = {
            "ADD": lambda: left + right,
            "SUB": lambda: left - right,
            "MUL": lambda: left * right,
            "DIV": lambda: left / right,
        }
        try:
            result = operations[opcode]()
        except KeyError as error:
            raise ValueError(f"Unknown opcode {opcode!r}.") from error
        self.stack.append(result)
