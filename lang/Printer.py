from antlr4 import *
from lang.ExprParser import ExprParser


class Printer(ParseTreeVisitor):

    def visitProg(self, ctx):
        builder = ['']
        i = 0
        for child in ctx.children:
            if child == ctx.NEWLINE(i):
                builder.append('\n')
                i = i + 1
            else:
                builder.append(self.visit(child))

        return ''.join(builder)

    def visitStatement(self, ctx):
        if ctx.dec:
            return self.visit(ctx.dec)
        if ctx.func:
            return self.visit(ctx.func)
        if ctx.fnCall:
            return self.visit(ctx.fnCall)
        if ctx.printcall:
            return self.visit(ctx.printcall)

    def visitDecl(self, ctx):
        return '{0} = {1}'.format(ctx.ident.text, self.visit(ctx.right))

    def visitFuncDef(self, ctx):
        builder = ['']
        builder.append('fn ')
        builder.append(ctx.ident.text)
        builder.append('(')
        builder.append(self.visit(ctx.params))
        builder.append(') ')
        builder.append(self.visit(ctx.bl))
        return ''.join(builder)

    def visitParamList(self, ctx):
        builder = ['']
        for stmt in ctx.children:
            builder.append(stmt.symbol.text)
        return ''.join(builder)

    def visitBlock(self, ctx):
        builder = ['']
        i = 0
        j = 0
        for stmt in ctx.children:
            if stmt == ctx.NEWLINE(i):
                builder.append('\n')
                i = i + 1
            elif stmt == ctx.TAB(j):
                builder.append('\t')
                j = j + 1
            elif stmt == ctx.OPEN_SCOPE():
                builder.append('[')
            elif stmt == ctx.CLOSE_SCOPE():
                builder.append(']')
            else:
                builder.append(self.visit(stmt))

        return ''.join(builder)

    def visitRetrn(self, ctx):
        builder = ['ret ']
        builder.append(ctx.value.text)
        return ''.join(builder)

    def visitFuncCall(self, ctx):
        builder = ['']
        builder.append(ctx.ident.text)
        builder.append('(')
        builder.append(self.visit(ctx.params))
        builder.append(')')
        return ''.join(builder)

    def visitExpr(self, expr):
        builder = ['']
        if expr.number:
            builder.append(str(expr.number.text))
        if expr.ident:
            builder.append(expr.ident.text)
        if expr.sub:
            builder.append('({})'.format(self.visit(expr.sub)))
        if expr.left:
            builder.append(self.visit(expr.left))
        if expr.op:
            op = expr.op.type
            if op == ExprParser.DIVIDE:
                builder.append('/')
            elif op == ExprParser.TIMES:
                builder.append('*')
            elif op == ExprParser.PLUS:
                builder.append('+')
            elif op == ExprParser.MINUS:
                builder.append('-')
        if expr.right:
            builder.append(self.visit(expr.right))
        if expr.call:
            builder.append(expr.call.ident.text)
            builder.append('(')
            for stmt in expr.call.params.children:
                builder.append(stmt.symbol.text)
            builder.append(')')
        return ''.join(builder)

    def visitPrintc(self, ctx):
        return 'print({val})'.format(val=ctx.ident.text)
