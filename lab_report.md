# Topic: Parser & Building an Abstract Syntax Tree

### Course: Formal Languages & Finite Automata
### Author: [Your Name]
### Group: [Your Group]

----

## Theory
The process of parsing and building Abstract Syntax Trees (ASTs) is fundamental to understanding how computers interpret and process programming languages:

**Parsing** is the process of analyzing a string of symbols according to the rules of a formal grammar. In the context of programming languages, parsing transforms source code from a raw textual format into a structured representation that captures its syntactic meaning. A parser typically works in conjunction with a lexer (tokenizer) that first breaks the input text into tokens.

**Abstract Syntax Trees (ASTs)** are hierarchical tree-like data structures that represent the abstract syntactic structure of source code. Unlike parse trees, ASTs omit syntactic details like punctuation and delimiters, focusing instead on the essential structure and meaning of the code. ASTs are widely used in:
- Compilers and interpreters
- Static code analysis
- Code refactoring tools
- Pretty-printers and formatters

The parsing process typically follows these steps:
1. **Lexical Analysis**: Converting the source code into tokens
2. **Syntax Analysis**: Building a parse tree or AST from the tokens
3. **Semantic Analysis**: Adding semantic information to the tree

## Objectives:
- Implement a lexical analyzer using regular expressions to categorize tokens
- Create a TokenType enumeration for token classification
- Design data structures for representing Abstract Syntax Trees
- Develop a parser to extract syntactic information from input text
- Create visualization tools for the AST

## Implementation

### TokenType Enum
I implemented a TokenType enum to categorize different types of tokens:

```python
class TokenType(Enum):
    NUMBER = auto()
    IDENTIFIER = auto()
    KEYWORD = auto()
    OPERATOR = auto()
    DELIMITER = auto()
    STRING = auto()
    COMMENT = auto()
    WHITESPACE = auto()
    UNKNOWN = auto()
```

Each token type corresponds to a specific category of language elements, making it easier to process them during parsing.

### Lexical Analysis
The lexer uses regular expressions to identify tokens from the input text:

```python
def tokenize(self, text: str) -> List[Token]:
    """Convert input text into a list of tokens"""
    tokens = []
    position = 0
    
    while position < len(text):
        match = self.compiled_regex.match(text[position:])
        if match:
            # Find which pattern matched
            for i, (token_type, _) in enumerate(self.token_patterns):
                group = match.group(i + 1)
                if group:
                    # Skip whitespace tokens but keep track of position
                    if token_type != TokenType.WHITESPACE:
                        tokens.append(Token(token_type, group, position))
                    position += len(group)
                    break
        else:
            # If no pattern matches, treat it as an unknown token
            tokens.append(Token(TokenType.UNKNOWN, text[position], position))
            position += 1
    
    return tokens
```

The regular expressions for each token type are defined as follows:

```python
token_patterns = [
    (TokenType.COMMENT, r"(\/\/.*$|\/\*[\s\S]*?\*\/)"),
    (TokenType.STRING, r"\"(\\.|[^\"])*\""),
    (TokenType.NUMBER, r"\b\d+(\.\d+)?\b"),
    (TokenType.KEYWORD, r"\b(if|else|while|for|return|int|float|void|class|public|private|static)\b"),
    (TokenType.IDENTIFIER, r"\b[a-zA-Z_][a-zA-Z0-9_]*\b"),
    (TokenType.OPERATOR, r"[\+\-\*\/\=\<\>\!\&\|\^%]|\<=|\>=|==|!=|\+\+|\-\-"),
    (TokenType.DELIMITER, r"[;,.(){}\[\]]"),
    (TokenType.WHITESPACE, r"\s+"),
]
```

### AST Data Structures
I designed a hierarchical structure for the AST:

```python
class ASTNode:
    """Base class for all AST nodes"""
    def __init__(self, node_type: str):
        self.node_type = node_type
        self.children = []
    
    def add_child(self, child):
        """Add a child node to this node"""
        self.children.append(child)
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert the node to a dictionary representation"""
        result = {"type": self.node_type}
        if self.children:
            result["children"] = [child.to_dict() for child in self.children]
        return result
```

The specialized node types include:

1. **ProgramNode**: Root node of the AST representing a complete program
2. **StatementNode**: Represents statements like if-statements, declarations, etc.
3. **ExpressionNode**: Represents expressions including literals, variables, and function calls

### Parser Implementation
The parser implements a recursive descent approach for building the AST:

```python
def parse(self) -> ASTNode:
    """Parse the tokens into an AST"""
    root = ProgramNode()
    
    while self.peek():
        statement = self.parse_statement()
        if statement:
            root.add_child(statement)
    
    return root
```

The parser has specialized methods for different language constructs:
- `parse_statement()`: Handles general statements
- `parse_if_statement()`: Parses if-else constructs
- `parse_declaration()`: Handles variable and function declarations
- `parse_expression()`: Processes expressions

### Visualization
I implemented multiple visualization methods to display the AST:

```python
def print_fancy_tree(node: ASTNode, prefix="", is_last=True):
    """Print a fancy tree visualization of the AST"""
    # Special characters for the tree
    branch = "└── " if is_last else "├── "
    
    # Different colors for different types of nodes
    if "Program" in node.node_type:
        color = Fore.CYAN + Style.BRIGHT
    elif "Statement" in node.node_type:
        color = Fore.GREEN
    elif "Expression" in node.node_type:
        color = Fore.YELLOW
    else:
        color = Fore.WHITE
        
    # Print the current node
    print(f"{prefix}{branch}{color}{node.node_type}")
    
    # Print value if it's an expression with a value
    if isinstance(node, ExpressionNode) and node.value is not None:
        value_branch = "    " if is_last else "│   "
        print(f"{prefix}{value_branch}{Fore.MAGENTA}Value: '{node.value}'")
    
    # Prepare prefix for children
    new_prefix = prefix + ("    " if is_last else "│   ")
    
    # Print children
    child_count = len(node.children)
    for i, child in enumerate(node.children):
        is_last_child = i == child_count - 1
        ASTVisualizer.print_fancy_tree(child, new_prefix, is_last_child)
```

## Results

When running the program with the sample code:

```c
// This is a sample program
int main() {
    int x = 10;
    if (x > 5) {
        printf("x is greater than 5");
    } else {
        return 0;
    }
}
```

The output shows:

1. The original code
2. The tokens identified by the lexer, color-coded by type
3. The Abstract Syntax Tree visualized as a hierarchical tree
4. The AST in JSON format

The AST correctly represents the structure of the program, including:
- The main function declaration
- The variable declaration for 'x'
- The if-else statement
- The function call to printf
- The return statement

## Conclusions

This laboratory work provided valuable insights into the processes of lexical analysis, parsing, and Abstract Syntax Tree construction:

1. **Lexical Analysis**: I learned how to use regular expressions to efficiently tokenize source code, recognizing different types of language elements.

2. **Token Classification**: Implementing the TokenType enum showed the importance of categorizing tokens for easier processing during parsing.

3. **Parser Implementation**: The recursive descent parsing approach demonstrated how to build a structured representation of the code following the grammar rules.

4. **AST Construction**: Building the AST revealed how to represent code in a hierarchical structure that captures its essential meaning while abstracting away syntactic details.

5. **Visualization**: Creating visualization tools highlighted the importance of being able to inspect and understand the AST for debugging and educational purposes.

This implementation serves as a foundation for more advanced language processing tasks, such as semantic analysis, optimization, and code generation. The principles learned can be applied to compiler development, static code analysis, and other language tooling.

## References:
- [Parsing Wiki](https://en.wikipedia.org/wiki/Parsing)
- [Abstract Syntax Tree Wiki](https://en.wikipedia.org/wiki/Abstract_syntax_tree)
- [Recursive Descent Parsing](https://en.wikipedia.org/wiki/Recursive_descent_parser)
- [Regular Expressions](https://en.wikipedia.org/wiki/Regular_expression)
