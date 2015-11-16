# Generated from Expr.g4 by ANTLR 4.5.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\f)\4\2\t\2\4\3\t\3\4\4\t\4\3\2\3\2\3\2\7\2\f\n\2\f\2")
        buf.write(u"\16\2\17\13\2\3\3\3\3\3\3\3\3\3\4\3\4\3\4\3\4\3\4\3\4")
        buf.write(u"\3\4\5\4\34\n\4\3\4\3\4\3\4\3\4\3\4\3\4\7\4$\n\4\f\4")
        buf.write(u"\16\4\'\13\4\3\4\2\3\6\5\2\4\6\2\4\3\2\13\f\3\2\t\n*")
        buf.write(u"\2\r\3\2\2\2\4\20\3\2\2\2\6\33\3\2\2\2\b\t\5\4\3\2\t")
        buf.write(u"\n\7\7\2\2\n\f\3\2\2\2\13\b\3\2\2\2\f\17\3\2\2\2\r\13")
        buf.write(u"\3\2\2\2\r\16\3\2\2\2\16\3\3\2\2\2\17\r\3\2\2\2\20\21")
        buf.write(u"\7\6\2\2\21\22\7\3\2\2\22\23\5\6\4\2\23\5\3\2\2\2\24")
        buf.write(u"\25\b\4\1\2\25\34\7\b\2\2\26\34\7\6\2\2\27\30\7\4\2\2")
        buf.write(u"\30\31\5\6\4\2\31\32\7\5\2\2\32\34\3\2\2\2\33\24\3\2")
        buf.write(u"\2\2\33\26\3\2\2\2\33\27\3\2\2\2\34%\3\2\2\2\35\36\f")
        buf.write(u"\7\2\2\36\37\t\2\2\2\37$\5\6\4\b !\f\6\2\2!\"\t\3\2\2")
        buf.write(u"\"$\5\6\4\7#\35\3\2\2\2# \3\2\2\2$\'\3\2\2\2%#\3\2\2")
        buf.write(u"\2%&\3\2\2\2&\7\3\2\2\2\'%\3\2\2\2\6\r\33#%")
        return buf.getvalue()


class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'='", u"'('", u"')'", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"'+'", u"'-'", u"'*'", 
                     u"'/'" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"ID", u"NEWLINE", u"INT", u"PLUS", u"MINUS", u"TIMES", 
                      u"DIVIDE" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_expr = 2

    ruleNames =  [ u"prog", u"statement", u"expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    ID=4
    NEWLINE=5
    INT=6
    PLUS=7
    MINUS=8
    TIMES=9
    DIVIDE=10

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
            self.state = 11
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ExprParser.ID:
                self.state = 6
                self.statement()
                self.state = 7
                self.match(ExprParser.NEWLINE)
                self.state = 13
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
            self.ident = None # Token
            self.right = None # ExprContext

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(ExprParser.ExprContext,0)


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
            self.enterOuterAlt(localctx, 1)
            self.state = 14
            localctx.ident = self.match(ExprParser.ID)
            self.state = 15
            self.match(ExprParser.T__0)
            self.state = 16
            localctx.right = self.expr(0)
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
        _startState = 4
        self.enterRecursionRule(localctx, 4, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            token = self._input.LA(1)
            if token in [ExprParser.INT]:
                self.state = 19
                localctx.number = self.match(ExprParser.INT)

            elif token in [ExprParser.ID]:
                self.state = 20
                localctx.ident = self.match(ExprParser.ID)

            elif token in [ExprParser.T__1]:
                self.state = 21
                self.match(ExprParser.T__1)
                self.state = 22
                localctx.sub = self.expr(0)
                self.state = 23
                self.match(ExprParser.T__2)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 35
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,3,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 33
                    la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 27
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 28
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ExprParser.TIMES or _la==ExprParser.DIVIDE):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 29
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 30
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 31
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ExprParser.PLUS or _la==ExprParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 32
                        localctx.right = self.expr(5)
                        pass

             
                self.state = 37
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,3,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx



    def sempred(self, localctx, ruleIndex, predIndex):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[2] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx, predIndex):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         




