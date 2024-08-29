import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from LabeledExprLexer import LabeledExprLexer
from LabeledExprParser import LabeledExprParser
from MyVisitor1 import MyVisitor1

def main():
    # Determine the input source
    if len(sys.argv) > 1:
        input_stream = FileStream(sys.argv[1])
    else:
        input_stream = InputStream(sys.stdin.read())
    
    # Create lexer and parser
    lexer = LabeledExprLexer(input_stream)
    token_stream = CommonTokenStream(lexer)
    parser = LabeledExprParser(token_stream)
    
    # Parse the input to generate the parse tree
    tree = parser.prog()
    
    # Create the visitor and visit the parse tree
    visitor = MyVisitor1()
    visitor.visit(tree)

if __name__ == '__main__':
    main()

