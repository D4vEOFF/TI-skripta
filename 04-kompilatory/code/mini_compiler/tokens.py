from dataclasses import dataclass
from enum import Enum, auto


class TokenKind(Enum):
    LET = auto()
    PRINT = auto()
    IDENTIFIER = auto()
    NUMBER = auto()
    PLUS = auto()
    MINUS = auto()
    STAR = auto()
    SLASH = auto()
    EQUAL = auto()
    SEMICOLON = auto()
    LEFT_PAREN = auto()
    RIGHT_PAREN = auto()
    EOF = auto()


KEYWORDS = {
    "let": TokenKind.LET,
    "print": TokenKind.PRINT,
}


@dataclass(frozen=True)
class Token:
    kind: TokenKind
    lexeme: str
    literal: float | None
    position: int
