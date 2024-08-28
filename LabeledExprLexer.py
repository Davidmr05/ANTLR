# Generated from LabeledExpr.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\21")
        buf.write("X\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\3\2\3\2\3\3\3\3\3\4\3\4\3\4")
        buf.write("\3\5\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\t\3\t\3\n\3\n\3")
        buf.write("\13\3\13\3\f\6\f9\n\f\r\f\16\f:\3\r\6\r>\n\r\r\r\16\r")
        buf.write("?\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\3\16\5\16K\n")
        buf.write("\16\3\17\5\17N\n\17\3\17\3\17\3\20\6\20S\n\20\r\20\16")
        buf.write("\20T\3\20\3\20\2\2\21\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21")
        buf.write("\n\23\13\25\f\27\r\31\16\33\17\35\20\37\21\3\2\5\4\2C")
        buf.write("\\c|\3\2\62;\4\2\13\13\"\"\2\\\2\3\3\2\2\2\2\5\3\2\2\2")
        buf.write("\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17")
        buf.write("\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3")
        buf.write("\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2")
        buf.write("\2\2\3!\3\2\2\2\5#\3\2\2\2\7%\3\2\2\2\t(\3\2\2\2\13+\3")
        buf.write("\2\2\2\r-\3\2\2\2\17/\3\2\2\2\21\61\3\2\2\2\23\63\3\2")
        buf.write("\2\2\25\65\3\2\2\2\278\3\2\2\2\31=\3\2\2\2\33J\3\2\2\2")
        buf.write("\35M\3\2\2\2\37R\3\2\2\2!\"\7?\2\2\"\4\3\2\2\2#$\7#\2")
        buf.write("\2$\6\3\2\2\2%&\7-\2\2&\'\7-\2\2\'\b\3\2\2\2()\7/\2\2")
        buf.write(")*\7/\2\2*\n\3\2\2\2+,\7*\2\2,\f\3\2\2\2-.\7+\2\2.\16")
        buf.write("\3\2\2\2/\60\7,\2\2\60\20\3\2\2\2\61\62\7\61\2\2\62\22")
        buf.write("\3\2\2\2\63\64\7-\2\2\64\24\3\2\2\2\65\66\7/\2\2\66\26")
        buf.write("\3\2\2\2\679\t\2\2\28\67\3\2\2\29:\3\2\2\2:8\3\2\2\2:")
        buf.write(";\3\2\2\2;\30\3\2\2\2<>\t\3\2\2=<\3\2\2\2>?\3\2\2\2?=")
        buf.write("\3\2\2\2?@\3\2\2\2@\32\3\2\2\2AB\7v\2\2BC\7t\2\2CD\7w")
        buf.write("\2\2DK\7g\2\2EF\7h\2\2FG\7c\2\2GH\7n\2\2HI\7u\2\2IK\7")
        buf.write("g\2\2JA\3\2\2\2JE\3\2\2\2K\34\3\2\2\2LN\7\17\2\2ML\3\2")
        buf.write("\2\2MN\3\2\2\2NO\3\2\2\2OP\7\f\2\2P\36\3\2\2\2QS\t\4\2")
        buf.write("\2RQ\3\2\2\2ST\3\2\2\2TR\3\2\2\2TU\3\2\2\2UV\3\2\2\2V")
        buf.write("W\b\20\2\2W \3\2\2\2\b\2:?JMT\3\b\2\2")
        return buf.getvalue()


class LabeledExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    MUL = 7
    DIV = 8
    ADD = 9
    SUB = 10
    ID = 11
    INT = 12
    BOOL = 13
    NEWLINE = 14
    WS = 15

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'='", "'!'", "'++'", "'--'", "'('", "')'", "'*'", "'/'", "'+'", 
            "'-'" ]

    symbolicNames = [ "<INVALID>",
            "MUL", "DIV", "ADD", "SUB", "ID", "INT", "BOOL", "NEWLINE", 
            "WS" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "MUL", 
                  "DIV", "ADD", "SUB", "ID", "INT", "BOOL", "NEWLINE", "WS" ]

    grammarFileName = "LabeledExpr.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


