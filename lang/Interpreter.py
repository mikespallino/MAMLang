from lang.ExprParser import ExprParser
from antlr4 import *


class Interpreter(ParseTreeVisitor):
    results = []
    memory = {}
    function_table = {}
    context = memory

    def visitProg(self, ctx):
        i = 0
        for child in ctx.children:
            if child == ctx.NEWLINE(i):
                i = i + 1
            else:
                self.results.append(self.visit(child))


    def visitStatement(self, ctx):
        if ctx.dec:
            return self.visit(ctx.dec)
        if ctx.func:
            return self.visit(ctx.func)
        if ctx.fnCall:
            return self.visit(ctx.fnCall)
        if ctx.printcall:
            return self.visit(ctx.printcall)

    def visitExpr(self, expr):
        if expr.number:
            return float(expr.number.text)
        if expr.ident:
            if expr.ident.text in self.context.keys():
                return self.context[expr.ident.text]
            else:
                print(self.context)
                raise Exception('Variable: {val} not defined.'.format(val=expr.ident.text))
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

        if expr.call:
            return self.visit(expr.call)

        return 0.0

    def visitFuncDef(self, ctx):
        func_mem = {}
        ident = ctx.ident.text
        params = ctx.params
        block = ctx.bl
        self.function_table[ident] = (self.visit(params), func_mem, block, )

    def visitFuncCall(self, ctx):
        ident = ctx.ident.text
        if ident in self.function_table.keys():
            params_list = self.visit(ctx.params)
            self.context = self.function_table[ident][1]
            for param in params_list:
                param = param.strip()
                self.context[param] = self.memory[param]
            for val in self.memory.keys():
                if val not in self.context.keys():
                    self.context[val] = self.memory[val]
            if params_list == self.function_table[ident][0]:
                return_val = self.visit(self.function_table[ident][2])
                self.context = self.memory
                return return_val
            else:
                self.context = self.memory
                raise Exception('Incorrect parameters for {func} ({params})'.format(func=ident, params=params_list))

        else:
            raise Exception('Function {func} not defined.'.format(func=ident))

    def visitRetrn(self, ctx):
        if ctx.value.text in self.context.keys() and not(ctx.value.text[0].isdigit()):
            return self.context[ctx.value.text]
        elif ctx.value.text in self.context.keys() and ctx.value.text[0].isdigit():
            print(self.context)
            raise Exception('Variable: {val} not defined.'.format(val=ctx.value.text))
        else:
            return ctx.value.text

    def visitParamList(self, ctx):
        return ''.join([stmt.symbol.text for stmt in ctx.children]).split(',')

    def visitDecl(self, ctx):
        self.context[ctx.ident.text] = self.visit(ctx.right)

    def visitBlock(self, ctx):
        for stmt in ctx.children:
            if isinstance(stmt, ExprParser.RetrnContext):
                return self.visit(stmt)
            else:
                self.visit(stmt)

        return 0

    def visitPrintc(self, ctx):
        if ctx.ident.text in self.context.keys():
            print(self.context[ctx.ident.text])
        else:
            raise Exception('Variable: {val} not defined.'.format(val=ctx.ident.text))