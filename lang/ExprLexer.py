# Generated from Expr.g4 by ANTLR 4.5.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO


def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\2")
        buf.write(u"\24a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write(u"\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t")
        buf.write(u"\r\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22")
        buf.write(u"\4\23\t\23\3\2\3\2\3\3\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3")
        buf.write(u"\5\3\6\3\6\3\7\3\7\3\b\3\b\7\b9\n\b\f\b\16\b<\13\b\3")
        buf.write(u"\t\6\t?\n\t\r\t\16\t@\3\n\6\nD\n\n\r\n\16\nE\3\13\3\13")
        buf.write(u"\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3")
        buf.write(u"\20\3\20\3\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23")
        buf.write(u"\3\23\3\23\2\2\24\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n")
        buf.write(u"\23\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24")
        buf.write(u"\3\2\6\6\2&&C\\aac|\7\2&&\62;C\\aac|\4\2\f\f\17\17\3")
        buf.write(u"\2\62;c\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2")
        buf.write(u"\2\2\13\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2")
        buf.write(u"\2\23\3\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2")
        buf.write(u"\2\33\3\2\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2")
        buf.write(u"#\3\2\2\2\2%\3\2\2\2\3\'\3\2\2\2\5)\3\2\2\2\7,\3\2\2")
        buf.write(u"\2\t/\3\2\2\2\13\62\3\2\2\2\r\64\3\2\2\2\17\66\3\2\2")
        buf.write(u"\2\21>\3\2\2\2\23C\3\2\2\2\25G\3\2\2\2\27I\3\2\2\2\31")
        buf.write(u"K\3\2\2\2\33M\3\2\2\2\35O\3\2\2\2\37T\3\2\2\2!X\3\2\2")
        buf.write(u"\2#Z\3\2\2\2%\\\3\2\2\2\'(\7?\2\2(\4\3\2\2\2)*\7\"\2")
        buf.write(u"\2*+\7*\2\2+\6\3\2\2\2,-\7+\2\2-.\7\"\2\2.\b\3\2\2\2")
        buf.write(u"/\60\7.\2\2\60\61\7\"\2\2\61\n\3\2\2\2\62\63\7*\2\2\63")
        buf.write(u"\f\3\2\2\2\64\65\7+\2\2\65\16\3\2\2\2\66:\t\2\2\2\67")
        buf.write(u"9\t\3\2\28\67\3\2\2\29<\3\2\2\2:8\3\2\2\2:;\3\2\2\2;")
        buf.write(u"\20\3\2\2\2<:\3\2\2\2=?\t\4\2\2>=\3\2\2\2?@\3\2\2\2@")
        buf.write(u">\3\2\2\2@A\3\2\2\2A\22\3\2\2\2BD\t\5\2\2CB\3\2\2\2D")
        buf.write(u"E\3\2\2\2EC\3\2\2\2EF\3\2\2\2F\24\3\2\2\2GH\7-\2\2H\26")
        buf.write(u"\3\2\2\2IJ\7/\2\2J\30\3\2\2\2KL\7,\2\2L\32\3\2\2\2MN")
        buf.write(u"\7\61\2\2N\34\3\2\2\2OP\7\"\2\2PQ\7\"\2\2QR\7\"\2\2R")
        buf.write(u"S\7\"\2\2S\36\3\2\2\2TU\7h\2\2UV\7p\2\2VW\7\"\2\2W \3")
        buf.write(u"\2\2\2XY\7]\2\2Y\"\3\2\2\2Z[\7_\2\2[$\3\2\2\2\\]\7t\2")
        buf.write(u"\2]^\7g\2\2^_\7v\2\2_`\7\"\2\2`&\3\2\2\2\6\2:@E\2")
        return buf.getvalue()


class ExprLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]


    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    ID = 7
    NEWLINE = 8
    INT = 9
    PLUS = 10
    MINUS = 11
    TIMES = 12
    DIVIDE = 13
    TAB = 14
    FN = 15
    OPEN_SCOPE = 16
    CLOSE_SCOPE = 17
    RET = 18

    modeNames = [ u"DEFAULT_MODE" ]

    literalNames = [ u"<INVALID>",
            u"'='", u"' ('", u"') '", u"', '", u"'('", u"')'", u"'+'", u"'-'", 
            u"'*'", u"'/'", u"'    '", u"'fn '", u"'['", u"']'", u"'ret '" ]

    symbolicNames = [ u"<INVALID>",
            u"ID", u"NEWLINE", u"INT", u"PLUS", u"MINUS", u"TIMES", u"DIVIDE", 
            u"TAB", u"FN", u"OPEN_SCOPE", u"CLOSE_SCOPE", u"RET" ]

    ruleNames = [ u"T__0", u"T__1", u"T__2", u"T__3", u"T__4", u"T__5", 
                  u"ID", u"NEWLINE", u"INT", u"PLUS", u"MINUS", u"TIMES", 
                  u"DIVIDE", u"TAB", u"FN", u"OPEN_SCOPE", u"CLOSE_SCOPE", 
                  u"RET" ]

    grammarFileName = u"Expr.g4"

    def __init__(self, input=None):
        super(ExprLexer, self).__init__(input)
        self.checkVersion("4.5.1")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


