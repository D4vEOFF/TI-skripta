from .ast_nodes import (
    BinaryExpr,
    Expr,
    LetStmt,
    NameExpr,
    NumberExpr,
    PrintStmt,
    Program,
    Stmt,
)
from .tokens import Token, TokenKind


class ParserError(ValueError):
    pass


class Parser:
    def __init__(self, tokens: list[Token]) -> None:
        self.tokens = tokens
        self.current = 0

    def parse(self) -> Program:
        statements: list[Stmt] = []
        while not self._check(TokenKind.EOF):
            statements.append(self._statement())
        return Program(statements)

    def _statement(self) -> Stmt:
        if self._match(TokenKind.LET):
            name = self._consume(
                TokenKind.IDENTIFIER, "Expected a variable name."
            )
            self._consume(TokenKind.EQUAL, "Expected '='.")
            initializer = self._expression()
            self._consume(TokenKind.SEMICOLON, "Expected ';'.")
            return LetStmt(name.lexeme, initializer)

        if self._match(TokenKind.PRINT):
            expression = self._expression()
            self._consume(TokenKind.SEMICOLON, "Expected ';'.")
            return PrintStmt(expression)

        raise self._error("Expected 'let' or 'print'.")

    def _expression(self) -> Expr:
        expression = self._term()
        while self._match(TokenKind.PLUS, TokenKind.MINUS):
            operator = self._previous().kind
            right = self._term()
            expression = BinaryExpr(expression, operator, right)
        return expression

    def _term(self) -> Expr:
        expression = self._factor()
        while self._match(TokenKind.STAR, TokenKind.SLASH):
            operator = self._previous().kind
            right = self._factor()
            expression = BinaryExpr(expression, operator, right)
        return expression

    def _factor(self) -> Expr:
        if self._match(TokenKind.NUMBER):
            literal = self._previous().literal
            assert literal is not None
            return NumberExpr(literal)

        if self._match(TokenKind.IDENTIFIER):
            return NameExpr(self._previous().lexeme)

        if self._match(TokenKind.LEFT_PAREN):
            expression = self._expression()
            self._consume(TokenKind.RIGHT_PAREN, "Expected ')'.")
            return expression

        raise self._error("Expected a number, name, or '('.")

    def _match(self, *kinds: TokenKind) -> bool:
        for kind in kinds:
            if self._check(kind):
                self.current += 1
                return True
        return False

    def _consume(self, kind: TokenKind, message: str) -> Token:
        if self._check(kind):
            self.current += 1
            return self._previous()
        raise self._error(message)

    def _check(self, kind: TokenKind) -> bool:
        return self._peek().kind is kind

    def _peek(self) -> Token:
        return self.tokens[self.current]

    def _previous(self) -> Token:
        return self.tokens[self.current - 1]

    def _error(self, message: str) -> ParserError:
        token = self._peek()
        return ParserError(
            f"{message} At position {token.position}, "
            f"found {token.lexeme!r}."
        )
