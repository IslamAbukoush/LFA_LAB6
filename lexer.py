from token_types import TokenType, COMPILED_REGEX

class Token:
    """
    Represents a token identified by the lexer.
    """
    def __init__(self, token_type, value, position):
        self.type = token_type
        self.value = value
        self.position = position
    
    def __repr__(self):
        return f"Token({self.type}, '{self.value}', pos={self.position})"


class Lexer:
    """
    Lexical analyzer that converts input text into a stream of tokens.
    """
    def __init__(self, text):
        self.text = text
        self.position = 0
        self.tokens = []
    
    def tokenize(self):
        """
        Process the input text and generate a list of tokens.
        """
        self.tokens = []
        
        # Use regex to find all tokens in the input text
        for match in COMPILED_REGEX.finditer(self.text):
            token_type_name = match.lastgroup
            token_value = match.group()
            token_position = match.start()
            
            # Convert the token type name to the corresponding enum value
            token_type = TokenType[token_type_name]
            
            # Create a token and add it to the list
            token = Token(token_type, token_value, token_position)
            self.tokens.append(token)
        
        # Add EOF token at the end
        self.tokens.append(Token(TokenType.EOF, "", len(self.text)))
        
        return self.tokens
    
    def get_tokens(self, skip_whitespace=True):
        """
        Return the list of tokens, optionally filtering out whitespace tokens.
        """
        if not self.tokens:
            self.tokenize()
        
        if skip_whitespace:
            return [token for token in self.tokens if token.type != TokenType.WHITESPACE]
        else:
            return self.tokens


def tokenize_text(text):
    """
    Helper function to tokenize input text and return the list of tokens.
    """
    lexer = Lexer(text)
    return lexer.get_tokens()


if __name__ == "__main__":
    # Example usage
    sample_text = "2 + 3.14 * sin(0.5)"
    lexer = Lexer(sample_text)
    tokens = lexer.get_tokens()
    
    print(f"Input: {sample_text}")
    print("Tokens:")
    for token in tokens:
        print(f"  {token}")
