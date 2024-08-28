from LabeledExprVisitor import LabeledExprVisitor
from LabeledExprParser import LabeledExprParser

class MyVisitor1(LabeledExprVisitor):
    def __init__(self):
        self.memory = {}

    def visitAssign(self, ctx):
        name = ctx.ID().getText()
        value = self.visit(ctx.expr())
        self.memory[name] = value
        return value

    def visitPrintExpr(self, ctx):
        value = self.visit(ctx.expr())
        print(value)
        return 0

    def visitInt(self, ctx):
        return int(ctx.INT().getText())

    def visitBool(self, ctx):
        return ctx.BOOL().getText() == 'true'

    def visitId(self, ctx):
        name = ctx.ID().getText()
        if name in self.memory:
            return self.memory[name]
        return 0

    def visitMulDiv(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == LabeledExprParser.MUL:
            return left * right
        return left / right

    def visitAddSub(self, ctx):
        left = self.visit(ctx.expr(0))
        right = self.visit(ctx.expr(1))
        if ctx.op.type == LabeledExprParser.ADD:
            return left + right
        return left - right

    def visitNegation(self, ctx):
        value = self.visit(ctx.expr())
        return not value

    def visitUnaryMinus(self, ctx):
        value = self.visit(ctx.expr())
        return -value

    def visitParens(self, ctx):
        return self.visit(ctx.expr())
    
    def visitPostIncrement(self, ctx):
        name = ctx.ID().getText()
        value = self.memory.get(name, 0)
        self.memory[name] = value + 1
        return value
    
    def visitPostDecrement(self, ctx):
        name = ctx.ID().getText()
        value = self.memory.get(name, 0)
        self.memory[name] = value - 1
        return value
    
    def visitPreIncrement(self, ctx):
        name = ctx.ID().getText()
        value = self.memory.get(name, 0) + 1
        self.memory[name] = value
        return value
    
    def visitPreDecrement(self, ctx):
        name = ctx.ID().getText()
        value = self.memory.get(name, 0) - 1
        self.memory[name] = value
        return value



