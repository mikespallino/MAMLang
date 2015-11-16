from antlr4 import *
from lang.ExprParser import ExprParser


class Calculator(ParseTreeVisitor):
    results = []
    memory = {}
    def visitProg(self, ctx):
        i = 0
        for child in ctx.children:
            if child == ctx.NEWLINE(i):
                i = i + 1
            else:
                self.results.append(self.visit(child))

        return self.visit(ctx.children[0])

    def visitStatement(self, ctx):
        result = self.visit(ctx.right)
        self.memory[ctx.ident.text] = result
        return result

    def visitExpr(self, expr):
        if expr.number:
            return float(expr.number.text)
        if expr.ident:
            return self.memory[expr.ident.text]
        if expr.sub:
            return self.visit(expr.sub)
        if expr.op:
            op = expr.op.type
            if op == ExprParser.DIVIDE:
                return self.visit(expr.left) / self.visit(expr.right)
            elif op == ExprParser.TIMES:
                return self.visit(expr.left) * self.visit(expr.right)
            elif op == ExprParser.PLUS:
                return self.visit(expr.left) + self.visit(expr.right)
            elif op == ExprParser.MINUS:
                return self.visit(expr.left) - self.visit(expr.right)

        return 0.0
