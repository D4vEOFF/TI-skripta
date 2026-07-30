from .codegen import CodeGenerator
from .lexer import Lexer
from .optimizer import ConstantFolder
from .parser import Parser
from .semantic import SemanticAnalyzer
from .virtual_machine import VirtualMachine


SOURCE = """
let x = 2 + 3 * 4;
print x;
let y = (x - 2) / 3;
print y;
"""


def main() -> None:
    tokens = Lexer(SOURCE).scan_tokens()
    syntax_tree = Parser(tokens).parse()
    SemanticAnalyzer().analyze(syntax_tree)
    optimized_tree = ConstantFolder().optimize(syntax_tree)
    bytecode = CodeGenerator().generate(optimized_tree)

    for instruction in bytecode:
        print(instruction)

    print("Program output:")
    VirtualMachine().run(bytecode)


if __name__ == "__main__":
    main()
