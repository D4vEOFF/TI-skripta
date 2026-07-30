from .ast_nodes import (
    BinaryExpr,
    Expr,
    LetStmt,
    NumberExpr,
    PrintStmt,
    Program,
)
from .tokens import TokenKind


class ConstantFolder:
    def optimize(self, program: Program) -> Program:
        statements = []
        for statement in program.statements:
            if isinstance(statement, LetStmt):
                statements.append(
                    LetStmt(
                        statement.name,
                        self._fold(statement.initializer),
                    )
                )
            elif isinstance(statement, PrintStmt):
                statements.append(
                    PrintStmt(self._fold(statement.expression))
                )
        return Program(statements)

    def _fold(self, expression: Expr) -> Expr:
        if not isinstance(expression, BinaryExpr):
            return expression

        left = self._fold(expression.left)
        right = self._fold(expression.right)

        if not isinstance(left, NumberExpr):
            return BinaryExpr(left, expression.operator, right)
        if not isinstance(right, NumberExpr):
            return BinaryExpr(left, expression.operator, right)

        a, b = left.value, right.value
        if expression.operator is TokenKind.PLUS:
            return NumberExpr(a + b)
        if expression.operator is TokenKind.MINUS:
            return NumberExpr(a - b)
        if expression.operator is TokenKind.STAR:
            return NumberExpr(a * b)
        if expression.operator is TokenKind.SLASH and b != 0:
            return NumberExpr(a / b)
        return BinaryExpr(left, expression.operator, right)
