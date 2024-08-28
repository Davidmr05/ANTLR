# Generated from LabeledExpr.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\21")
        buf.write(":\4\2\t\2\4\3\t\3\4\4\t\4\3\2\6\2\n\n\2\r\2\16\2\13\3")
        buf.write("\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\3\5\3\27\n\3\3\4\3\4")
        buf.write("\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3")
        buf.write("\4\3\4\3\4\3\4\3\4\5\4-\n\4\3\4\3\4\3\4\3\4\3\4\3\4\7")
        buf.write("\4\65\n\4\f\4\16\48\13\4\3\4\2\3\6\5\2\4\6\2\4\3\2\13")
        buf.write("\f\3\2\t\n\2D\2\t\3\2\2\2\4\26\3\2\2\2\6,\3\2\2\2\b\n")
        buf.write("\5\4\3\2\t\b\3\2\2\2\n\13\3\2\2\2\13\t\3\2\2\2\13\f\3")
        buf.write("\2\2\2\f\3\3\2\2\2\r\16\5\6\4\2\16\17\7\20\2\2\17\27\3")
        buf.write("\2\2\2\20\21\7\r\2\2\21\22\7\3\2\2\22\23\5\6\4\2\23\24")
        buf.write("\7\20\2\2\24\27\3\2\2\2\25\27\7\20\2\2\26\r\3\2\2\2\26")
        buf.write("\20\3\2\2\2\26\25\3\2\2\2\27\5\3\2\2\2\30\31\b\4\1\2\31")
        buf.write("-\7\16\2\2\32-\7\17\2\2\33-\7\r\2\2\34\35\7\4\2\2\35-")
        buf.write("\5\6\4\t\36\37\7\r\2\2\37-\7\5\2\2 !\7\r\2\2!-\7\6\2\2")
        buf.write("\"#\7\5\2\2#-\7\r\2\2$%\7\6\2\2%-\7\r\2\2&\'\7\f\2\2\'")
        buf.write("-\5\6\4\4()\7\7\2\2)*\5\6\4\2*+\7\b\2\2+-\3\2\2\2,\30")
        buf.write("\3\2\2\2,\32\3\2\2\2,\33\3\2\2\2,\34\3\2\2\2,\36\3\2\2")
        buf.write("\2, \3\2\2\2,\"\3\2\2\2,$\3\2\2\2,&\3\2\2\2,(\3\2\2\2")
        buf.write("-\66\3\2\2\2./\f\16\2\2/\60\t\2\2\2\60\65\5\6\4\17\61")
        buf.write("\62\f\r\2\2\62\63\t\3\2\2\63\65\5\6\4\16\64.\3\2\2\2\64")
        buf.write("\61\3\2\2\2\658\3\2\2\2\66\64\3\2\2\2\66\67\3\2\2\2\67")
        buf.write("\7\3\2\2\28\66\3\2\2\2\7\13\26,\64\66")
        return buf.getvalue()


class LabeledExprParser ( Parser ):

    grammarFileName = "LabeledExpr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'='", "'!'", "'++'", "'--'", "'('", "')'", 
                     "'*'", "'/'", "'+'", "'-'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "MUL", "DIV", 
                      "ADD", "SUB", "ID", "INT", "BOOL", "NEWLINE", "WS" ]

    RULE_prog = 0
    RULE_stat = 1
    RULE_expr = 2

    ruleNames =  [ "prog", "stat", "expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    MUL=7
    DIV=8
    ADD=9
    SUB=10
    ID=11
    INT=12
    BOOL=13
    NEWLINE=14
    WS=15

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LabeledExprParser.StatContext)
            else:
                return self.getTypedRuleContext(LabeledExprParser.StatContext,i)


        def getRuleIndex(self):
            return LabeledExprParser.RULE_prog

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProg" ):
                listener.enterProg(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProg" ):
                listener.exitProg(self)




    def prog(self):

        localctx = LabeledExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 7 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 6
                self.stat()
                self.state = 9 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not ((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LabeledExprParser.T__1) | (1 << LabeledExprParser.T__2) | (1 << LabeledExprParser.T__3) | (1 << LabeledExprParser.T__4) | (1 << LabeledExprParser.SUB) | (1 << LabeledExprParser.ID) | (1 << LabeledExprParser.INT) | (1 << LabeledExprParser.BOOL) | (1 << LabeledExprParser.NEWLINE))) != 0)):
                    break

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LabeledExprParser.RULE_stat

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class BlankContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def NEWLINE(self):
            return self.getToken(LabeledExprParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlank" ):
                listener.enterBlank(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlank" ):
                listener.exitBlank(self)


    class PrintExprContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LabeledExprParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(LabeledExprParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintExpr" ):
                listener.enterPrintExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintExpr" ):
                listener.exitPrintExpr(self)


    class AssignContext(StatContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.StatContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LabeledExprParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(LabeledExprParser.ExprContext,0)

        def NEWLINE(self):
            return self.getToken(LabeledExprParser.NEWLINE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)



    def stat(self):

        localctx = LabeledExprParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 20
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                localctx = LabeledExprParser.PrintExprContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 11
                self.expr(0)
                self.state = 12
                self.match(LabeledExprParser.NEWLINE)
                pass

            elif la_ == 2:
                localctx = LabeledExprParser.AssignContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 14
                self.match(LabeledExprParser.ID)
                self.state = 15
                self.match(LabeledExprParser.T__0)
                self.state = 16
                self.expr(0)
                self.state = 17
                self.match(LabeledExprParser.NEWLINE)
                pass

            elif la_ == 3:
                localctx = LabeledExprParser.BlankContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 19
                self.match(LabeledExprParser.NEWLINE)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LabeledExprParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class PreIncrementContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LabeledExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreIncrement" ):
                listener.enterPreIncrement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreIncrement" ):
                listener.exitPreIncrement(self)


    class ParensContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LabeledExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParens" ):
                listener.enterParens(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParens" ):
                listener.exitParens(self)


    class BoolContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def BOOL(self):
            return self.getToken(LabeledExprParser.BOOL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBool" ):
                listener.enterBool(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBool" ):
                listener.exitBool(self)


    class NegationContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(LabeledExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegation" ):
                listener.enterNegation(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegation" ):
                listener.exitNegation(self)


    class AddSubContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LabeledExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(LabeledExprParser.ExprContext,i)

        def ADD(self):
            return self.getToken(LabeledExprParser.ADD, 0)
        def SUB(self):
            return self.getToken(LabeledExprParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddSub" ):
                listener.enterAddSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddSub" ):
                listener.exitAddSub(self)


    class MulDivContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LabeledExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(LabeledExprParser.ExprContext,i)

        def MUL(self):
            return self.getToken(LabeledExprParser.MUL, 0)
        def DIV(self):
            return self.getToken(LabeledExprParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMulDiv" ):
                listener.enterMulDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMulDiv" ):
                listener.exitMulDiv(self)


    class PostDecrementContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LabeledExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostDecrement" ):
                listener.enterPostDecrement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostDecrement" ):
                listener.exitPostDecrement(self)


    class UnaryMinusContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def SUB(self):
            return self.getToken(LabeledExprParser.SUB, 0)
        def expr(self):
            return self.getTypedRuleContext(LabeledExprParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterUnaryMinus" ):
                listener.enterUnaryMinus(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitUnaryMinus" ):
                listener.exitUnaryMinus(self)


    class IdContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LabeledExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)


    class PostIncrementContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LabeledExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPostIncrement" ):
                listener.enterPostIncrement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPostIncrement" ):
                listener.exitPostIncrement(self)


    class PreDecrementContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(LabeledExprParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPreDecrement" ):
                listener.enterPreDecrement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPreDecrement" ):
                listener.exitPreDecrement(self)


    class IntContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LabeledExprParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(LabeledExprParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LabeledExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                localctx = LabeledExprParser.IntContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 23
                self.match(LabeledExprParser.INT)
                pass

            elif la_ == 2:
                localctx = LabeledExprParser.BoolContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 24
                self.match(LabeledExprParser.BOOL)
                pass

            elif la_ == 3:
                localctx = LabeledExprParser.IdContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 25
                self.match(LabeledExprParser.ID)
                pass

            elif la_ == 4:
                localctx = LabeledExprParser.NegationContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 26
                self.match(LabeledExprParser.T__1)
                self.state = 27
                self.expr(7)
                pass

            elif la_ == 5:
                localctx = LabeledExprParser.PostIncrementContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 28
                self.match(LabeledExprParser.ID)
                self.state = 29
                self.match(LabeledExprParser.T__2)
                pass

            elif la_ == 6:
                localctx = LabeledExprParser.PostDecrementContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 30
                self.match(LabeledExprParser.ID)
                self.state = 31
                self.match(LabeledExprParser.T__3)
                pass

            elif la_ == 7:
                localctx = LabeledExprParser.PreIncrementContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 32
                self.match(LabeledExprParser.T__2)
                self.state = 33
                self.match(LabeledExprParser.ID)
                pass

            elif la_ == 8:
                localctx = LabeledExprParser.PreDecrementContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 34
                self.match(LabeledExprParser.T__3)
                self.state = 35
                self.match(LabeledExprParser.ID)
                pass

            elif la_ == 9:
                localctx = LabeledExprParser.UnaryMinusContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 36
                self.match(LabeledExprParser.SUB)
                self.state = 37
                self.expr(2)
                pass

            elif la_ == 10:
                localctx = LabeledExprParser.ParensContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 38
                self.match(LabeledExprParser.T__4)
                self.state = 39
                self.expr(0)
                self.state = 40
                self.match(LabeledExprParser.T__5)
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 52
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 50
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = LabeledExprParser.AddSubContext(self, LabeledExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 44
                        if not self.precpred(self._ctx, 12):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 12)")
                        self.state = 45
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==LabeledExprParser.ADD or _la==LabeledExprParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 46
                        self.expr(13)
                        pass

                    elif la_ == 2:
                        localctx = LabeledExprParser.MulDivContext(self, LabeledExprParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 47
                        if not self.precpred(self._ctx, 11):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 11)")
                        self.state = 48
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==LabeledExprParser.MUL or _la==LabeledExprParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 49
                        self.expr(12)
                        pass

             
                self.state = 54
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 12)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 11)
         




