from antlr4 import *
from CalcLexer import CalcLexer
from CalcParser import CalcParser
from CalcVisitor import CalcVisitor

class CalcErrorListener(ErrorListener):
    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        print(f"error: {msg}", file=sys.stderr)

class CalcVisitor(ParseTreeVisitor):
    def visitExp(self, ctx):
        if ctx.factor():
            return self.visit(ctx.factor())
        elif ctx.ADD():
            return self.visit(ctx.exp(0)) + self.visit(ctx.exp(1))
        elif ctx.SUB():
            return self.visit(ctx.exp(0)) - self.visit(ctx.factor())
        elif ctx.ABS():
            return abs(self.visit(ctx.exp()))
    
    def visitFactor(self, ctx):
        if ctx.term():
            return self.visit(ctx.term())
    
    def visitTerm(self, ctx):
        if ctx.NUMBER():
            return int(ctx.NUMBER().getText())
        elif ctx.OP():
            return self.visit(ctx.exp())
    
    def visit(self, tree):
        return super().visit(tree)

def main():
    input_stream = InputStream(input("> "))
    lexer = CalcLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = CalcParser(stream)
    parser.removeErrorListeners()
    parser.addErrorListener(CalcErrorListener())
    tree = parser.calclist()
    visitor = CalcVisitor()
    while True:
        try:
            result = visitor.visit(tree)
            print(f"= {result}\n> ", end="")
        except EOFError:
            break

if __name__ == '__main__':
    main()

