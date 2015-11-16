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
        return '{0} = {1}'.format(ctx.ident.text, self.visit(ctx.right))

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

        return ''.join(builder)
