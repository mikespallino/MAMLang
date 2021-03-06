# Generated from Expr.g4 by ANTLR 4.5.1
from antlr4 import *

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#prog.
    def visitProg(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#statement.
    def visitStatement(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#decl.
    def visitDecl(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#funcDef.
    def visitFuncDef(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#paramList.
    def visitParamList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#paramCallList.
    def visitParamCallList(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#block.
    def visitBlock(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#retrn.
    def visitRetrn(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ctrlStruct.
    def visitCtrlStruct(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#whileStruct.
    def visitWhileStruct(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#ifStruct.
    def visitIfStruct(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#funcCall.
    def visitFuncCall(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#condition.
    def visitCondition(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expr.
    def visitExpr(self, ctx):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#printc.
    def visitPrintc(self, ctx):
        return self.visitChildren(ctx)


