# Generated from Expr.g4 by ANTLR 4.5.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\25h\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\7\2\32")
        buf.write(u"\n\2\f\2\16\2\35\13\2\3\3\3\3\3\3\3\3\5\3#\n\3\3\4\3")
        buf.write(u"\4\3\4\3\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\3\6\3\6\3\6\7")
        buf.write(u"\6\63\n\6\f\6\16\6\66\13\6\3\7\3\7\3\7\3\7\3\7\5\7=\n")
        buf.write(u"\7\3\7\3\7\6\7A\n\7\r\7\16\7B\3\7\3\7\3\b\3\b\3\b\3\t")
        buf.write(u"\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n")
        buf.write(u"W\n\n\3\n\3\n\3\n\3\n\3\n\3\n\7\n_\n\n\f\n\16\nb\13\n")
        buf.write(u"\3\13\3\13\3\13\3\13\3\13\2\3\22\f\2\4\6\b\n\f\16\20")
        buf.write(u"\22\24\2\5\4\2\n\n\f\f\3\2\17\20\3\2\r\16i\2\33\3\2\2")
        buf.write(u"\2\4\"\3\2\2\2\6$\3\2\2\2\b(\3\2\2\2\n/\3\2\2\2\f\67")
        buf.write(u"\3\2\2\2\16F\3\2\2\2\20I\3\2\2\2\22V\3\2\2\2\24c\3\2")
        buf.write(u"\2\2\26\27\5\4\3\2\27\30\7\13\2\2\30\32\3\2\2\2\31\26")
        buf.write(u"\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34")
        buf.write(u"\3\3\2\2\2\35\33\3\2\2\2\36#\5\6\4\2\37#\5\b\5\2 #\5")
        buf.write(u"\20\t\2!#\5\24\13\2\"\36\3\2\2\2\"\37\3\2\2\2\" \3\2")
        buf.write(u"\2\2\"!\3\2\2\2#\5\3\2\2\2$%\7\n\2\2%&\7\3\2\2&\'\5\22")
        buf.write(u"\n\2\'\7\3\2\2\2()\7\22\2\2)*\7\n\2\2*+\7\4\2\2+,\5\n")
        buf.write(u"\6\2,-\7\5\2\2-.\5\f\7\2.\t\3\2\2\2/\64\7\n\2\2\60\61")
        buf.write(u"\7\6\2\2\61\63\7\n\2\2\62\60\3\2\2\2\63\66\3\2\2\2\64")
        buf.write(u"\62\3\2\2\2\64\65\3\2\2\2\65\13\3\2\2\2\66\64\3\2\2\2")
        buf.write(u"\678\7\23\2\28@\7\13\2\29<\7\21\2\2:=\5\4\3\2;=\5\16")
        buf.write(u"\b\2<:\3\2\2\2<;\3\2\2\2=>\3\2\2\2>?\7\13\2\2?A\3\2\2")
        buf.write(u"\2@9\3\2\2\2AB\3\2\2\2B@\3\2\2\2BC\3\2\2\2CD\3\2\2\2")
        buf.write(u"DE\7\24\2\2E\r\3\2\2\2FG\7\25\2\2GH\t\2\2\2H\17\3\2\2")
        buf.write(u"\2IJ\7\n\2\2JK\7\7\2\2KL\5\n\6\2LM\7\b\2\2M\21\3\2\2")
        buf.write(u"\2NO\b\n\1\2OW\7\f\2\2PW\7\n\2\2QR\7\7\2\2RS\5\22\n\2")
        buf.write(u"ST\7\b\2\2TW\3\2\2\2UW\5\20\t\2VN\3\2\2\2VP\3\2\2\2V")
        buf.write(u"Q\3\2\2\2VU\3\2\2\2W`\3\2\2\2XY\f\b\2\2YZ\t\3\2\2Z_\5")
        buf.write(u"\22\n\t[\\\f\7\2\2\\]\t\4\2\2]_\5\22\n\b^X\3\2\2\2^[")
        buf.write(u"\3\2\2\2_b\3\2\2\2`^\3\2\2\2`a\3\2\2\2a\23\3\2\2\2b`")
        buf.write(u"\3\2\2\2cd\7\t\2\2de\7\n\2\2ef\7\b\2\2f\25\3\2\2\2\n")
        buf.write(u"\33\"\64<BV^`")
        return buf.getvalue()


class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'='", u"' ('", u"') '", u"', '", u"'('", 
                     u"')'", u"'print('", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"'+'", u"'-'", u"'*'", u"'/'", u"'    '", u"'fn '", 
                     u"'['", u"']'", u"'ret '" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"ID", u"NEWLINE", u"INT", u"PLUS", u"MINUS", u"TIMES", 
                      u"DIVIDE", u"TAB", u"FN", u"OPEN_SCOPE", u"CLOSE_SCOPE", 
                      u"RET" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_decl = 2
    RULE_funcDef = 3
    RULE_paramList = 4
    RULE_block = 5
    RULE_retrn = 6
    RULE_funcCall = 7
    RULE_expr = 8
    RULE_printc = 9

    ruleNames =  [ u"prog", u"statement", u"decl", u"funcDef", u"paramList", 
                   u"block", u"retrn", u"funcCall", u"expr", u"printc" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    ID=8
    NEWLINE=9
    INT=10
    PLUS=11
    MINUS=12
    TIMES=13
    DIVIDE=14
    TAB=15
    FN=16
    OPEN_SCOPE=17
    CLOSE_SCOPE=18
    RET=19

    def __init__(self, input):
        super(ExprParser, self).__init__(input)
        self.checkVersion("4.5.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class ProgContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ExprParser.ProgContext, self).__init__(parent, invokingState)
            self.parser = parser

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def NEWLINE(self, i=None):
            if i is None:
                return self.getTokens(ExprParser.NEWLINE)
            else:
                return self.getToken(ExprParser.NEWLINE, i)

        def getRuleIndex(self):
            return ExprParser.RULE_prog

        def accept(self, visitor):
            if hasattr(visitor, "visitProg"):
                return visitor.visitProg(self)
            else:
                return visitor.visitChildren(self)




    def prog(self):

        localctx = ExprParser.ProgContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_prog)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << ExprParser.T__6) | (1 << ExprParser.ID) | (1 << ExprParser.FN))) != 0):
                self.state = 20
                self.statement()
                self.state = 21
                self.match(ExprParser.NEWLINE)
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class StatementContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ExprParser.StatementContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.dec = None # DeclContext
            self.func = None # FuncDefContext
            self.fnCall = None # FuncCallContext
            self.printcall = None # PrintcContext

        def decl(self):
            return self.getTypedRuleContext(ExprParser.DeclContext,0)


        def funcDef(self):
            return self.getTypedRuleContext(ExprParser.FuncDefContext,0)


        def funcCall(self):
            return self.getTypedRuleContext(ExprParser.FuncCallContext,0)


        def printc(self):
            return self.getTypedRuleContext(ExprParser.PrintcContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_statement

        def accept(self, visitor):
            if hasattr(visitor, "visitStatement"):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = ExprParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 32
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                localctx.dec = self.decl()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
                localctx.func = self.funcDef()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 30
                localctx.fnCall = self.funcCall()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 31
                localctx.printcall = self.printc()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ExprParser.DeclContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.ident = None # Token
            self.right = None # ExprContext

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_decl

        def accept(self, visitor):
            if hasattr(visitor, "visitDecl"):
                return visitor.visitDecl(self)
            else:
                return visitor.visitChildren(self)




    def decl(self):

        localctx = ExprParser.DeclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_decl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 34
            localctx.ident = self.match(ExprParser.ID)
            self.state = 35
            self.match(ExprParser.T__0)
            self.state = 36
            localctx.right = self.expr(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncDefContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ExprParser.FuncDefContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.ident = None # Token
            self.params = None # ParamListContext
            self.bl = None # BlockContext

        def FN(self):
            return self.getToken(ExprParser.FN, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def paramList(self):
            return self.getTypedRuleContext(ExprParser.ParamListContext,0)


        def block(self):
            return self.getTypedRuleContext(ExprParser.BlockContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_funcDef

        def accept(self, visitor):
            if hasattr(visitor, "visitFuncDef"):
                return visitor.visitFuncDef(self)
            else:
                return visitor.visitChildren(self)




    def funcDef(self):

        localctx = ExprParser.FuncDefContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_funcDef)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 38
            self.match(ExprParser.FN)
            self.state = 39
            localctx.ident = self.match(ExprParser.ID)
            self.state = 40
            self.match(ExprParser.T__1)
            self.state = 41
            localctx.params = self.paramList()
            self.state = 42
            self.match(ExprParser.T__2)
            self.state = 43
            localctx.bl = self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ParamListContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ExprParser.ParamListContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.ident = None # Token
            self.split = None # Token
            self.ident2 = None # Token

        def ID(self, i=None):
            if i is None:
                return self.getTokens(ExprParser.ID)
            else:
                return self.getToken(ExprParser.ID, i)

        def getRuleIndex(self):
            return ExprParser.RULE_paramList

        def accept(self, visitor):
            if hasattr(visitor, "visitParamList"):
                return visitor.visitParamList(self)
            else:
                return visitor.visitChildren(self)




    def paramList(self):

        localctx = ExprParser.ParamListContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_paramList)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 45
            localctx.ident = self.match(ExprParser.ID)
            self.state = 50
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ExprParser.T__3:
                self.state = 46
                localctx.split = self.match(ExprParser.T__3)
                self.state = 47
                localctx.ident2 = self.match(ExprParser.ID)
                self.state = 52
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class BlockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ExprParser.BlockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def OPEN_SCOPE(self):
            return self.getToken(ExprParser.OPEN_SCOPE, 0)

        def NEWLINE(self, i=None):
            if i is None:
                return self.getTokens(ExprParser.NEWLINE)
            else:
                return self.getToken(ExprParser.NEWLINE, i)

        def CLOSE_SCOPE(self):
            return self.getToken(ExprParser.CLOSE_SCOPE, 0)

        def TAB(self, i=None):
            if i is None:
                return self.getTokens(ExprParser.TAB)
            else:
                return self.getToken(ExprParser.TAB, i)

        def statement(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.StatementContext)
            else:
                return self.getTypedRuleContext(ExprParser.StatementContext,i)


        def retrn(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.RetrnContext)
            else:
                return self.getTypedRuleContext(ExprParser.RetrnContext,i)


        def getRuleIndex(self):
            return ExprParser.RULE_block

        def accept(self, visitor):
            if hasattr(visitor, "visitBlock"):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = ExprParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 53
            self.match(ExprParser.OPEN_SCOPE)
            self.state = 54
            self.match(ExprParser.NEWLINE)
            self.state = 62 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 55
                self.match(ExprParser.TAB)
                self.state = 58
                token = self._input.LA(1)
                if token in [ExprParser.T__6, ExprParser.ID, ExprParser.FN]:
                    self.state = 56
                    self.statement()

                elif token in [ExprParser.RET]:
                    self.state = 57
                    self.retrn()

                else:
                    raise NoViableAltException(self)

                self.state = 60
                self.match(ExprParser.NEWLINE)
                self.state = 64 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ExprParser.TAB):
                    break

            self.state = 66
            self.match(ExprParser.CLOSE_SCOPE)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class RetrnContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ExprParser.RetrnContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.value = None # Token

        def RET(self):
            return self.getToken(ExprParser.RET, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_retrn

        def accept(self, visitor):
            if hasattr(visitor, "visitRetrn"):
                return visitor.visitRetrn(self)
            else:
                return visitor.visitChildren(self)




    def retrn(self):

        localctx = ExprParser.RetrnContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_retrn)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(ExprParser.RET)
            self.state = 69
            localctx.value = self._input.LT(1)
            _la = self._input.LA(1)
            if not(_la==ExprParser.ID or _la==ExprParser.INT):
                localctx.value = self._errHandler.recoverInline(self)
            else:
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FuncCallContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ExprParser.FuncCallContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.ident = None # Token
            self.params = None # ParamListContext

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def paramList(self):
            return self.getTypedRuleContext(ExprParser.ParamListContext,0)


        def getRuleIndex(self):
            return ExprParser.RULE_funcCall

        def accept(self, visitor):
            if hasattr(visitor, "visitFuncCall"):
                return visitor.visitFuncCall(self)
            else:
                return visitor.visitChildren(self)




    def funcCall(self):

        localctx = ExprParser.FuncCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_funcCall)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            localctx.ident = self.match(ExprParser.ID)
            self.state = 72
            self.match(ExprParser.T__4)
            self.state = 73
            localctx.params = self.paramList()
            self.state = 74
            self.match(ExprParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class ExprContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ExprParser.ExprContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.left = None # ExprContext
            self.number = None # Token
            self.ident = None # Token
            self.sub = None # ExprContext
            self.call = None # FuncCallContext
            self.op = None # Token
            self.right = None # ExprContext

        def INT(self):
            return self.getToken(ExprParser.INT, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def expr(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(ExprParser.ExprContext)
            else:
                return self.getTypedRuleContext(ExprParser.ExprContext,i)


        def funcCall(self):
            return self.getTypedRuleContext(ExprParser.FuncCallContext,0)


        def TIMES(self):
            return self.getToken(ExprParser.TIMES, 0)

        def DIVIDE(self):
            return self.getToken(ExprParser.DIVIDE, 0)

        def PLUS(self):
            return self.getToken(ExprParser.PLUS, 0)

        def MINUS(self):
            return self.getToken(ExprParser.MINUS, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_expr

        def accept(self, visitor):
            if hasattr(visitor, "visitExpr"):
                return visitor.visitExpr(self)
            else:
                return visitor.visitChildren(self)



    def expr(self, _p=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = ExprParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 16
        self.enterRecursionRule(localctx, 16, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 84
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                self.state = 77
                localctx.number = self.match(ExprParser.INT)
                pass

            elif la_ == 2:
                self.state = 78
                localctx.ident = self.match(ExprParser.ID)
                pass

            elif la_ == 3:
                self.state = 79
                self.match(ExprParser.T__4)
                self.state = 80
                localctx.sub = self.expr(0)
                self.state = 81
                self.match(ExprParser.T__5)
                pass

            elif la_ == 4:
                self.state = 83
                localctx.call = self.funcCall()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 94
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 92
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 86
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 87
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ExprParser.TIMES or _la==ExprParser.DIVIDE):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 88
                        localctx.right = self.expr(7)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 89
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 90
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ExprParser.PLUS or _la==ExprParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 91
                        localctx.right = self.expr(6)
                        pass

             
                self.state = 96
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx

    class PrintcContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(ExprParser.PrintcContext, self).__init__(parent, invokingState)
            self.parser = parser
            self.ident = None # Token

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def getRuleIndex(self):
            return ExprParser.RULE_printc

        def accept(self, visitor):
            if hasattr(visitor, "visitPrintc"):
                return visitor.visitPrintc(self)
            else:
                return visitor.visitChildren(self)




    def printc(self):

        localctx = ExprParser.PrintcContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_printc)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(ExprParser.T__6)
            self.state = 98
            localctx.ident = self.match(ExprParser.ID)
            self.state = 99
            self.match(ExprParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[8] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 5)
         




