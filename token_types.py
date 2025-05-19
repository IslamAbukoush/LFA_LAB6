from enum import Enum, auto
import re

class TokenType(Enum):
    """
    Enum representing the different types of tokens that can be identified in the input text.
    """
    # Numbers
    INTEGER = auto()      # Integer numbers (e.g., 42, 100)
    FLOAT = auto()        # Floating point numbers (e.g., 3.14, 2.5)
    
    # Operators
    PLUS = auto()         # Addition operator (+)
    MINUS = auto()        # Subtraction operator (-)
    MULTIPLY = auto()     # Multiplication operator (*)
    DIVIDE = auto()       # Division operator (/)
    POWER = auto()        # Power operator (^)
    
    # Parentheses
    LPAREN = auto()       # Left parenthesis (
    RPAREN = auto()       # Right parenthesis )
    
    # Functions
    SIN = auto()          # Sine function
    COS = auto()          # Cosine function
    TAN = auto()          # Tangent function
    LOG = auto()          # Logarithm function
    
    # Other
    IDENTIFIER = auto()   # Variable names or other identifiers
    WHITESPACE = auto()   # Spaces, tabs, newlines
    COMMA = auto()        # Comma separator
    EOF = auto()          # End of file/input
    UNKNOWN = auto()      # Unknown token type

# Regular expression patterns for token identification
TOKEN_PATTERNS = [
    (TokenType.FLOAT, r'\d+\.\d+'),
    (TokenType.INTEGER, r'\d+'),
    (TokenType.PLUS, r'\+'),
    (TokenType.MINUS, r'-'),
    (TokenType.MULTIPLY, r'\*'),
    (TokenType.DIVIDE, r'/'),
    (TokenType.POWER, r'\^'),
    (TokenType.LPAREN, r'\('),
    (TokenType.RPAREN, r'\)'),
    (TokenType.SIN, r'sin'),
    (TokenType.COS, r'cos'),
    (TokenType.TAN, r'tan'),
    (TokenType.LOG, r'log'),
    (TokenType.COMMA, r','),
    (TokenType.IDENTIFIER, r'[a-zA-Z_][a-zA-Z0-9_]*'),
    (TokenType.WHITESPACE, r'[ \t\n\r]+'),
]

# Compile all patterns into a single regex for efficient matching
TOKEN_REGEX = '|'.join('(?P<%s>%s)' % (token_type.name, pattern) for token_type, pattern in TOKEN_PATTERNS)
COMPILED_REGEX = re.compile(TOKEN_REGEX)
