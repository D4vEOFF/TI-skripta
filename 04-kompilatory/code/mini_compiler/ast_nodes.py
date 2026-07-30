from __future__ import annotations

from dataclasses import dataclass

from .tokens import TokenKind


class Expr:
    pass


@dataclass(frozen=True)
class NumberExpr(Expr):
    value: float


@dataclass(frozen=True)
class NameExpr(Expr):
    name: str


@dataclass(frozen=True)
class BinaryExpr(Expr):
    left: Expr
    operator: TokenKind
    right: Expr


class Stmt:
    pass


@dataclass(frozen=True)
class LetStmt(Stmt):
    name: str
    initializer: Expr


@dataclass(frozen=True)
class PrintStmt(Stmt):
    expression: Expr


@dataclass(frozen=True)
class Program:
    statements: list[Stmt]
