# Generated from Expr.g4 by ANTLR 4.5.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"\f\66\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\3\3")
        buf.write(u"\3\3\4\3\4\3\5\3\5\7\5 \n\5\f\5\16\5#\13\5\3\6\6\6&\n")
        buf.write(u"\6\r\6\16\6\'\3\7\6\7+\n\7\r\7\16\7,\3\b\3\b\3\t\3\t")
        buf.write(u"\3\n\3\n\3\13\3\13\2\2\f\3\3\5\4\7\5\t\6\13\7\r\b\17")
        buf.write(u"\t\21\n\23\13\25\f\3\2\6\6\2&&C\\aac|\7\2&&\62;C\\aa")
        buf.write(u"c|\4\2\f\f\17\17\3\2\62;8\2\3\3\2\2\2\2\5\3\2\2\2\2\7")
        buf.write(u"\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3")
        buf.write(u"\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\3\27\3")
        buf.write(u"\2\2\2\5\31\3\2\2\2\7\33\3\2\2\2\t\35\3\2\2\2\13%\3\2")
        buf.write(u"\2\2\r*\3\2\2\2\17.\3\2\2\2\21\60\3\2\2\2\23\62\3\2\2")
        buf.write(u"\2\25\64\3\2\2\2\27\30\7?\2\2\30\4\3\2\2\2\31\32\7*\2")
        buf.write(u"\2\32\6\3\2\2\2\33\34\7+\2\2\34\b\3\2\2\2\35!\t\2\2\2")
        buf.write(u"\36 \t\3\2\2\37\36\3\2\2\2 #\3\2\2\2!\37\3\2\2\2!\"\3")
        buf.write(u"\2\2\2\"\n\3\2\2\2#!\3\2\2\2$&\t\4\2\2%$\3\2\2\2&\'\3")
        buf.write(u"\2\2\2\'%\3\2\2\2\'(\3\2\2\2(\f\3\2\2\2)+\t\5\2\2*)\3")
        buf.write(u"\2\2\2+,\3\2\2\2,*\3\2\2\2,-\3\2\2\2-\16\3\2\2\2./\7")
        buf.write(u"-\2\2/\20\3\2\2\2\60\61\7/\2\2\61\22\3\2\2\2\62\63\7")
        buf.write(u",\2\2\63\24\3\2\2\2\64\65\7\61\2\2\65\26\3\2\2\2\6\2")
        buf.write(u"!\',\2")
        return buf.getvalue()


class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    ID = 4
    NEWLINE = 5
    INT = 6
    PLUS = 7
    MINUS = 8
    TIMES = 9
    DIVIDE = 10

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'='", u"'('", u"')'", u"'+'", u"'-'", u"'*'", u"'/'" ]

    symbolicNames = [ u"<INVALID>",
            u"ID", u"NEWLINE", u"INT", u"PLUS", u"MINUS", u"TIMES", u"DIVIDE" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"ID", u"NEWLINE", u"INT", 
                  u"PLUS", u"MINUS", u"TIMES", u"DIVIDE" ]

    grammarFileName = u"Expr.g4"

    def __init__(self, input=None):
        super(ExprLexer, self).__init__(input)
        self.checkVersion("4.5.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


