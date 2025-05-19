class ASTNode:
    """
    Base class for all AST nodes.
    """
    def __init__(self):
        pass
    
    def __str__(self):
        return self.__class__.__name__


class NumberNode(ASTNode):
    """
    AST node representing a numeric literal (integer or float).
    """
    def __init__(self, value):
        super().__init__()
        self.value = value
    
    def __str__(self):
        return f"Number({self.value})"


class BinaryOpNode(ASTNode):
    """
    AST node representing a binary operation (e.g., addition, multiplication).
    """
    def __init__(self, left, operator, right):
        super().__init__()
        self.left = left
        self.operator = operator
        self.right = right
    
    def __str__(self):
        return f"BinaryOp({self.operator}, {self.left}, {self.right})"


class UnaryOpNode(ASTNode):
    """
    AST node representing a unary operation (e.g., negation).
    """
    def __init__(self, operator, operand):
        super().__init__()
        self.operator = operator
        self.operand = operand
    
    def __str__(self):
        return f"UnaryOp({self.operator}, {self.operand})"


class FunctionCallNode(ASTNode):
    """
    AST node representing a function call (e.g., sin, cos).
    """
    def __init__(self, function_name, arguments):
        super().__init__()
        self.function_name = function_name
        self.arguments = arguments  # List of argument nodes
    
    def __str__(self):
        args_str = ", ".join(str(arg) for arg in self.arguments)
        return f"FunctionCall({self.function_name}, [{args_str}])"


class IdentifierNode(ASTNode):
    """
    AST node representing a variable or identifier.
    """
    def __init__(self, name):
        super().__init__()
        self.name = name
    
    def __str__(self):
        return f"Identifier({self.name})"


class ProgramNode(ASTNode):
    """
    Root node of the AST representing the entire program or expression.
    """
    def __init__(self, expression):
        super().__init__()
        self.expression = expression
    
    def __str__(self):
        return f"Program({self.expression})"


def print_ast(node, indent=0):
    """
    Helper function to print the AST in a readable tree format.
    """
    indent_str = "  " * indent
    
    if isinstance(node, NumberNode):
        print(f"{indent_str}Number: {node.value}")
    
    elif isinstance(node, BinaryOpNode):
        print(f"{indent_str}BinaryOp: {node.operator}")
        print(f"{indent_str}  Left:")
        print_ast(node.left, indent + 2)
        print(f"{indent_str}  Right:")
        print_ast(node.right, indent + 2)
    
    elif isinstance(node, UnaryOpNode):
        print(f"{indent_str}UnaryOp: {node.operator}")
        print(f"{indent_str}  Operand:")
        print_ast(node.operand, indent + 2)
    
    elif isinstance(node, FunctionCallNode):
        print(f"{indent_str}FunctionCall: {node.function_name}")
        print(f"{indent_str}  Arguments:")
        for i, arg in enumerate(node.arguments):
            print(f"{indent_str}    Arg {i}:")
            print_ast(arg, indent + 3)
    
    elif isinstance(node, IdentifierNode):
        print(f"{indent_str}Identifier: {node.name}")
    
    elif isinstance(node, ProgramNode):
        print(f"{indent_str}Program:")
        print_ast(node.expression, indent + 1)
    
    else:
        print(f"{indent_str}Unknown node type: {type(node)}")
