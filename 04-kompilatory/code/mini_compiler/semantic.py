from .ast_nodes import (
    BinaryExpr,
    Expr,
    LetStmt,
    NameExpr,
    NumberExpr,
    PrintStmt,
    Program,
)


class SemanticError(ValueError):
    pass


class SemanticAnalyzer:
    def __init__(self) -> None:
        self.declared_names: set[str] = set()

    def analyze(self, program: Program) -> None:
        for statement in program.statements:
            if isinstance(statement, LetStmt):
                if statement.name in self.declared_names:
                    raise SemanticError(
                        f"Variable {statement.name!r} is already declared."
                    )
                self._check_expr(statement.initializer)
                self.declared_names.add(statement.name)
            elif isinstance(statement, PrintStmt):
                self._check_expr(statement.expression)

    def _check_expr(self, expression: Expr) -> None:
        if isinstance(expression, NumberExpr):
            return
        if isinstance(expression, NameExpr):
            if expression.name not in self.declared_names:
                raise SemanticError(
                    f"Variable {expression.name!r} is not declared."
                )
            return
        if isinstance(expression, BinaryExpr):
            self._check_expr(expression.left)
            self._check_expr(expression.right)
            return
        raise TypeError(f"Unknown expression: {expression!r}")
