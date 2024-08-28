# Generated from Calc.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2\f")
        buf.write("8\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\6\2\31\n\2\r\2")
        buf.write("\16\2\32\3\3\3\3\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\t\3\t\3\n\5\n,\n\n\3\n\3\n\5\n\60\n\n\3\13\6\13\63")
        buf.write("\n\13\r\13\16\13\64\3\13\3\13\2\2\f\3\3\5\4\7\5\t\6\13")
        buf.write("\7\r\b\17\t\21\n\23\13\25\f\3\2\4\3\2\62;\4\2\13\13\"")
        buf.write("\"\2;\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2")
        buf.write("\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2")
        buf.write("\23\3\2\2\2\2\25\3\2\2\2\3\30\3\2\2\2\5\34\3\2\2\2\7\36")
        buf.write("\3\2\2\2\t \3\2\2\2\13\"\3\2\2\2\r$\3\2\2\2\17&\3\2\2")
        buf.write("\2\21(\3\2\2\2\23/\3\2\2\2\25\62\3\2\2\2\27\31\t\2\2\2")
        buf.write("\30\27\3\2\2\2\31\32\3\2\2\2\32\30\3\2\2\2\32\33\3\2\2")
        buf.write("\2\33\4\3\2\2\2\34\35\7-\2\2\35\6\3\2\2\2\36\37\7/\2\2")
        buf.write("\37\b\3\2\2\2 !\7,\2\2!\n\3\2\2\2\"#\7\61\2\2#\f\3\2\2")
        buf.write("\2$%\7~\2\2%\16\3\2\2\2&\'\7*\2\2\'\20\3\2\2\2()\7+\2")
        buf.write("\2)\22\3\2\2\2*,\7\17\2\2+*\3\2\2\2+,\3\2\2\2,-\3\2\2")
        buf.write("\2-\60\7\f\2\2.\60\7\17\2\2/+\3\2\2\2/.\3\2\2\2\60\24")
        buf.write("\3\2\2\2\61\63\t\3\2\2\62\61\3\2\2\2\63\64\3\2\2\2\64")
        buf.write("\62\3\2\2\2\64\65\3\2\2\2\65\66\3\2\2\2\66\67\b\13\2\2")
        buf.write("\67\26\3\2\2\2\7\2\32+/\64\3\b\2\2")
        return buf.getvalue()


class CalcLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    NUMBER = 1
    ADD = 2
    SUB = 3
    MUL = 4
    DIV = 5
    ABS = 6
    OP = 7
    CP = 8
    EOL = 9
    WS = 10

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'+'", "'-'", "'*'", "'/'", "'|'", "'('", "')'" ]

    symbolicNames = [ "<INVALID>",
            "NUMBER", "ADD", "SUB", "MUL", "DIV", "ABS", "OP", "CP", "EOL", 
            "WS" ]

    ruleNames = [ "NUMBER", "ADD", "SUB", "MUL", "DIV", "ABS", "OP", "CP", 
                  "EOL", "WS" ]

    grammarFileName = "Calc.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


