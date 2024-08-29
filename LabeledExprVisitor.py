# Generated from LabeledExpr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LabeledExprParser import LabeledExprParser
else:
    from LabeledExprParser import LabeledExprParser

# This class defines a complete generic visitor for a parse tree produced by LabeledExprParser.

class LabeledExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LabeledExprParser#prog.
    def visitProg(self, ctx:LabeledExprParser.ProgContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#printExpr.
    def visitPrintExpr(self, ctx:LabeledExprParser.PrintExprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#assign.
    def visitAssign(self, ctx:LabeledExprParser.AssignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#blank.
    def visitBlank(self, ctx:LabeledExprParser.BlankContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#PreIncrement.
    def visitPreIncrement(self, ctx:LabeledExprParser.PreIncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#parens.
    def visitParens(self, ctx:LabeledExprParser.ParensContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#bool.
    def visitBool(self, ctx:LabeledExprParser.BoolContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#Negation.
    def visitNegation(self, ctx:LabeledExprParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#AddSub.
    def visitAddSub(self, ctx:LabeledExprParser.AddSubContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#MulDiv.
    def visitMulDiv(self, ctx:LabeledExprParser.MulDivContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#PostDecrement.
    def visitPostDecrement(self, ctx:LabeledExprParser.PostDecrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#UnaryMinus.
    def visitUnaryMinus(self, ctx:LabeledExprParser.UnaryMinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#id.
    def visitId(self, ctx:LabeledExprParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#PostIncrement.
    def visitPostIncrement(self, ctx:LabeledExprParser.PostIncrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#PreDecrement.
    def visitPreDecrement(self, ctx:LabeledExprParser.PreDecrementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LabeledExprParser#int.
    def visitInt(self, ctx:LabeledExprParser.IntContext):
        return self.visitChildren(ctx)



del LabeledExprParser