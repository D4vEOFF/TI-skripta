from .tokens import KEYWORDS, Token, TokenKind


class LexerError(ValueError):
    pass


class Lexer:
    SINGLE_CHAR_TOKENS = {
        "+": TokenKind.PLUS,
        "-": TokenKind.MINUS,
        "*": TokenKind.STAR,
        "/": TokenKind.SLASH,
        "=": TokenKind.EQUAL,
        ";": TokenKind.SEMICOLON,
        "(": TokenKind.LEFT_PAREN,
        ")": TokenKind.RIGHT_PAREN,
    }

    def __init__(self, source: str) -> None:
        self.source = source
        self.current = 0
        self.tokens: list[Token] = []

    def scan_tokens(self) -> list[Token]:
        while not self._at_end():
            start = self.current
            char = self._advance()

            if char.isspace():
                continue
            if char == "/" and self._peek() == "/":
                self._skip_comment()
            elif char.isdigit():
                self._scan_number(start)
            elif char.isalpha() or char == "_":
                self._scan_identifier(start)
            elif char in self.SINGLE_CHAR_TOKENS:
                self._add(self.SINGLE_CHAR_TOKENS[char], start)
            else:
                raise LexerError(
                    f"Unexpected character {char!r} at position {start}."
                )

        self.tokens.append(
            Token(TokenKind.EOF, "", None, self.current)
        )
        return self.tokens

    def _scan_number(self, start: int) -> None:
        while self._peek().isdigit():
            self._advance()

        if self._peek() == "." and self._peek_next().isdigit():
            self._advance()
            while self._peek().isdigit():
                self._advance()

        lexeme = self.source[start:self.current]
        self.tokens.append(
            Token(TokenKind.NUMBER, lexeme, float(lexeme), start)
        )

    def _scan_identifier(self, start: int) -> None:
        while self._peek().isalnum() or self._peek() == "_":
            self._advance()

        lexeme = self.source[start:self.current]
        kind = KEYWORDS.get(lexeme, TokenKind.IDENTIFIER)
        self.tokens.append(Token(kind, lexeme, None, start))

    def _skip_comment(self) -> None:
        while not self._at_end() and self._peek() != "\n":
            self._advance()

    def _add(self, kind: TokenKind, start: int) -> None:
        lexeme = self.source[start:self.current]
        self.tokens.append(Token(kind, lexeme, None, start))

    def _advance(self) -> str:
        char = self.source[self.current]
        self.current += 1
        return char

    def _peek(self) -> str:
        if self._at_end():
            return "\0"
        return self.source[self.current]

    def _peek_next(self) -> str:
        if self.current + 1 >= len(self.source):
            return "\0"
        return self.source[self.current + 1]

    def _at_end(self) -> bool:
        return self.current >= len(self.source)
