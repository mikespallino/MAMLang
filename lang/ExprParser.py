# Generated from Expr.g4 by ANTLR 4.5.1
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"\24W\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write(u"\4\b\t\b\4\t\t\t\3\2\3\2\3\2\7\2\26\n\2\f\2\16\2\31\13")
        buf.write(u"\2\3\3\3\3\5\3\35\n\3\3\4\3\4\3\4\3\4\3\5\3\5\3\5\3\5")
        buf.write(u"\3\5\3\5\3\5\3\6\3\6\7\6,\n\6\f\6\16\6/\13\6\3\7\3\7")
        buf.write(u"\3\7\3\7\3\7\5\7\66\n\7\3\7\3\7\6\7:\n\7\r\7\16\7;\3")
        buf.write(u"\7\3\7\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\5\tJ\n")
        buf.write(u"\t\3\t\3\t\3\t\3\t\3\t\3\t\7\tR\n\t\f\t\16\tU\13\t\3")
        buf.write(u"\t\2\3\20\n\2\4\6\b\n\f\16\20\2\4\3\2\16\17\3\2\f\rW")
        buf.write(u"\2\27\3\2\2\2\4\34\3\2\2\2\6\36\3\2\2\2\b\"\3\2\2\2\n")
        buf.write(u"-\3\2\2\2\f\60\3\2\2\2\16?\3\2\2\2\20I\3\2\2\2\22\23")
        buf.write(u"\5\4\3\2\23\24\7\n\2\2\24\26\3\2\2\2\25\22\3\2\2\2\26")
        buf.write(u"\31\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\3\3\2\2\2")
        buf.write(u"\31\27\3\2\2\2\32\35\5\6\4\2\33\35\5\b\5\2\34\32\3\2")
        buf.write(u"\2\2\34\33\3\2\2\2\35\5\3\2\2\2\36\37\7\t\2\2\37 \7\3")
        buf.write(u"\2\2 !\5\20\t\2!\7\3\2\2\2\"#\7\21\2\2#$\7\t\2\2$%\7")
        buf.write(u"\4\2\2%&\5\n\6\2&\'\7\5\2\2\'(\5\f\7\2(\t\3\2\2\2)*\7")
        buf.write(u"\t\2\2*,\7\6\2\2+)\3\2\2\2,/\3\2\2\2-+\3\2\2\2-.\3\2")
        buf.write(u"\2\2.\13\3\2\2\2/-\3\2\2\2\60\61\7\22\2\2\619\7\n\2\2")
        buf.write(u"\62\65\7\20\2\2\63\66\5\4\3\2\64\66\5\16\b\2\65\63\3")
        buf.write(u"\2\2\2\65\64\3\2\2\2\66\67\3\2\2\2\678\7\n\2\28:\3\2")
        buf.write(u"\2\29\62\3\2\2\2:;\3\2\2\2;9\3\2\2\2;<\3\2\2\2<=\3\2")
        buf.write(u"\2\2=>\7\23\2\2>\r\3\2\2\2?@\7\24\2\2@A\7\t\2\2A\17\3")
        buf.write(u"\2\2\2BC\b\t\1\2CJ\7\13\2\2DJ\7\t\2\2EF\7\7\2\2FG\5\20")
        buf.write(u"\t\2GH\7\b\2\2HJ\3\2\2\2IB\3\2\2\2ID\3\2\2\2IE\3\2\2")
        buf.write(u"\2JS\3\2\2\2KL\f\7\2\2LM\t\2\2\2MR\5\20\t\bNO\f\6\2\2")
        buf.write(u"OP\t\3\2\2PR\5\20\t\7QK\3\2\2\2QN\3\2\2\2RU\3\2\2\2S")
        buf.write(u"Q\3\2\2\2ST\3\2\2\2T\21\3\2\2\2US\3\2\2\2\n\27\34-\65")
        buf.write(u";IQS")
        return buf.getvalue()


class ExprParser ( Parser ):

    grammarFileName = "Expr.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"'='", u"' ('", u"') '", u"', '", u"'('", 
                     u"')'", u"<INVALID>", u"<INVALID>", u"<INVALID>", u"'+'", 
                     u"'-'", u"'*'", u"'/'", u"'    '", u"'fn '", u"'['", 
                     u"']'", u"'ret '" ]

    symbolicNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                      u"<INVALID>", u"<INVALID>", u"<INVALID>", u"ID", u"NEWLINE", 
                      u"INT", u"PLUS", u"MINUS", u"TIMES", u"DIVIDE", u"TAB", 
                      u"FN", u"OPEN_SCOPE", u"CLOSE_SCOPE", u"RET" ]

    RULE_prog = 0
    RULE_statement = 1
    RULE_decl = 2
    RULE_funcDef = 3
    RULE_paramList = 4
    RULE_block = 5
    RULE_retrn = 6
    RULE_expr = 7

    ruleNames =  [ u"prog", u"statement", u"decl", u"funcDef", u"paramList", 
                   u"block", u"retrn", u"expr" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    ID=7
    NEWLINE=8
    INT=9
    PLUS=10
    MINUS=11
    TIMES=12
    DIVIDE=13
    TAB=14
    FN=15
    OPEN_SCOPE=16
    CLOSE_SCOPE=17
    RET=18

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
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ExprParser.ID or _la==ExprParser.FN:
                self.state = 16
                self.statement()
                self.state = 17
                self.match(ExprParser.NEWLINE)
                self.state = 23
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

        def decl(self):
            return self.getTypedRuleContext(ExprParser.DeclContext,0)


        def funcDef(self):
            return self.getTypedRuleContext(ExprParser.FuncDefContext,0)


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
            self.state = 26
            token = self._input.LA(1)
            if token in [ExprParser.ID]:
                self.enterOuterAlt(localctx, 1)
                self.state = 24
                localctx.dec = self.decl()

            elif token in [ExprParser.FN]:
                self.enterOuterAlt(localctx, 2)
                self.state = 25
                localctx.func = self.funcDef()

            else:
                raise NoViableAltException(self)

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
            self.state = 28
            localctx.ident = self.match(ExprParser.ID)
            self.state = 29
            self.match(ExprParser.T__0)
            self.state = 30
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
            self.state = 32
            self.match(ExprParser.FN)
            self.state = 33
            localctx.ident = self.match(ExprParser.ID)
            self.state = 34
            self.match(ExprParser.T__1)
            self.state = 35
            localctx.params = self.paramList()
            self.state = 36
            self.match(ExprParser.T__2)
            self.state = 37
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
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==ExprParser.ID:
                self.state = 39
                localctx.ident = self.match(ExprParser.ID)
                self.state = 40
                localctx.split = self.match(ExprParser.T__3)
                self.state = 45
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
            self.state = 46
            self.match(ExprParser.OPEN_SCOPE)
            self.state = 47
            self.match(ExprParser.NEWLINE)
            self.state = 55 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 48
                self.match(ExprParser.TAB)
                self.state = 51
                token = self._input.LA(1)
                if token in [ExprParser.ID, ExprParser.FN]:
                    self.state = 49
                    self.statement()

                elif token in [ExprParser.RET]:
                    self.state = 50
                    self.retrn()

                else:
                    raise NoViableAltException(self)

                self.state = 53
                self.match(ExprParser.NEWLINE)
                self.state = 57 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==ExprParser.TAB):
                    break

            self.state = 59
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
            self.ident = None # Token

        def RET(self):
            return self.getToken(ExprParser.RET, 0)

        def ID(self):
            return self.getToken(ExprParser.ID, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(ExprParser.RET)
            self.state = 62
            localctx.ident = self.match(ExprParser.ID)
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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            token = self._input.LA(1)
            if token in [ExprParser.INT]:
                self.state = 65
                localctx.number = self.match(ExprParser.INT)

            elif token in [ExprParser.ID]:
                self.state = 66
                localctx.ident = self.match(ExprParser.ID)

            elif token in [ExprParser.T__4]:
                self.state = 67
                self.match(ExprParser.T__4)
                self.state = 68
                localctx.sub = self.expr(0)
                self.state = 69
                self.match(ExprParser.T__5)

            else:
                raise NoViableAltException(self)

            self._ctx.stop = self._input.LT(-1)
            self.state = 81
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,7,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 79
                    la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
                    if la_ == 1:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 73
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 74
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ExprParser.TIMES or _la==ExprParser.DIVIDE):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 75
                        localctx.right = self.expr(6)
                        pass

                    elif la_ == 2:
                        localctx = ExprParser.ExprContext(self, _parentctx, _parentState)
                        localctx.left = _prevctx
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 76
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 77
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==ExprParser.PLUS or _la==ExprParser.MINUS):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self.consume()
                        self.state = 78
                        localctx.right = self.expr(5)
                        pass

             
                self.state = 83
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,7,self._ctx)

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
        self._predicates[7] = self.expr_sempred
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
         




