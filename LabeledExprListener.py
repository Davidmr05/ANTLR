# Generated from LabeledExpr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .LabeledExprParser import LabeledExprParser
else:
    from LabeledExprParser import LabeledExprParser

# This class defines a complete listener for a parse tree produced by LabeledExprParser.
class LabeledExprListener(ParseTreeListener):

    # Enter a parse tree produced by LabeledExprParser#prog.
    def enterProg(self, ctx:LabeledExprParser.ProgContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#prog.
    def exitProg(self, ctx:LabeledExprParser.ProgContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#printExpr.
    def enterPrintExpr(self, ctx:LabeledExprParser.PrintExprContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#printExpr.
    def exitPrintExpr(self, ctx:LabeledExprParser.PrintExprContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#assign.
    def enterAssign(self, ctx:LabeledExprParser.AssignContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#assign.
    def exitAssign(self, ctx:LabeledExprParser.AssignContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#blank.
    def enterBlank(self, ctx:LabeledExprParser.BlankContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#blank.
    def exitBlank(self, ctx:LabeledExprParser.BlankContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#PreIncrement.
    def enterPreIncrement(self, ctx:LabeledExprParser.PreIncrementContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#PreIncrement.
    def exitPreIncrement(self, ctx:LabeledExprParser.PreIncrementContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#parens.
    def enterParens(self, ctx:LabeledExprParser.ParensContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#parens.
    def exitParens(self, ctx:LabeledExprParser.ParensContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#bool.
    def enterBool(self, ctx:LabeledExprParser.BoolContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#bool.
    def exitBool(self, ctx:LabeledExprParser.BoolContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#Negation.
    def enterNegation(self, ctx:LabeledExprParser.NegationContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#Negation.
    def exitNegation(self, ctx:LabeledExprParser.NegationContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#AddSub.
    def enterAddSub(self, ctx:LabeledExprParser.AddSubContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#AddSub.
    def exitAddSub(self, ctx:LabeledExprParser.AddSubContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#MulDiv.
    def enterMulDiv(self, ctx:LabeledExprParser.MulDivContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#MulDiv.
    def exitMulDiv(self, ctx:LabeledExprParser.MulDivContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#PostDecrement.
    def enterPostDecrement(self, ctx:LabeledExprParser.PostDecrementContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#PostDecrement.
    def exitPostDecrement(self, ctx:LabeledExprParser.PostDecrementContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#UnaryMinus.
    def enterUnaryMinus(self, ctx:LabeledExprParser.UnaryMinusContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#UnaryMinus.
    def exitUnaryMinus(self, ctx:LabeledExprParser.UnaryMinusContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#id.
    def enterId(self, ctx:LabeledExprParser.IdContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#id.
    def exitId(self, ctx:LabeledExprParser.IdContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#PostIncrement.
    def enterPostIncrement(self, ctx:LabeledExprParser.PostIncrementContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#PostIncrement.
    def exitPostIncrement(self, ctx:LabeledExprParser.PostIncrementContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#PreDecrement.
    def enterPreDecrement(self, ctx:LabeledExprParser.PreDecrementContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#PreDecrement.
    def exitPreDecrement(self, ctx:LabeledExprParser.PreDecrementContext):
        pass


    # Enter a parse tree produced by LabeledExprParser#int.
    def enterInt(self, ctx:LabeledExprParser.IntContext):
        pass

    # Exit a parse tree produced by LabeledExprParser#int.
    def exitInt(self, ctx:LabeledExprParser.IntContext):
        pass



del LabeledExprParser