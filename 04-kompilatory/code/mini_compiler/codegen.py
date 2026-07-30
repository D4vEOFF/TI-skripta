from dataclasses import dataclass

from .ast_nodes import (
    BinaryExpr,
    Expr,
    LetStmt,
    NameExpr,
    NumberExpr,
    PrintStmt,
    Program,
)
from .tokens import TokenKind


@dataclass(frozen=True)
class Instruction:
    opcode: str
    argument: float | str | None = None


class CodeGenerator:
    OPERATORS = {
        TokenKind.PLUS: "ADD",
        TokenKind.MINUS: "SUB",
        TokenKind.STAR: "MUL",
        TokenKind.SLASH: "DIV",
    }

    def generate(self, program: Program) -> list[Instruction]:
        code: list[Instruction] = []
        for statement in program.statements:
            if isinstance(statement, LetStmt):
                self._emit_expr(statement.initializer, code)
                code.append(Instruction("STORE", statement.name))
            elif isinstance(statement, PrintStmt):
                self._emit_expr(statement.expression, code)
                code.append(Instruction("PRINT"))
        code.append(Instruction("HALT"))
        return code

    def _emit_expr(
        self, expression: Expr, code: list[Instruction]
    ) -> None:
        if isinstance(expression, NumberExpr):
            code.append(Instruction("PUSH", expression.value))
        elif isinstance(expression, NameExpr):
            code.append(Instruction("LOAD", expression.name))
        elif isinstance(expression, BinaryExpr):
            self._emit_expr(expression.left, code)
            self._emit_expr(expression.right, code)
            code.append(Instruction(self.OPERATORS[expression.operator]))
        else:
            raise TypeError(f"Unknown expression: {expression!r}")
