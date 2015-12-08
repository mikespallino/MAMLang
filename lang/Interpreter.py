from lang.ExprParser import ExprParser
from antlr4 import *


class Interpreter(ParseTreeVisitor):
    results = []
    memory = {'memory_type': 'global'}
    function_table = {}
    context = memory
    return_val = 0

    def visitProg(self, ctx):
        i = 0
        for child in ctx.children:
            if child == ctx.NEWLINE(i):
                i += 1
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
        if ctx.struct:
            return self.visit(ctx.struct)

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
        params = self.visit(ctx.params)
        block = ctx.bl
        self.function_table[ident] = (params, func_mem, block, )

    def visitFuncCall(self, ctx):
        ident = ctx.ident.text
        save_call_state = False
        if ident in self.function_table.keys():
            params_list = self.visit(ctx.params)
            if self.context['memory_type'] == ident:
                for val in self.context.keys():
                    self.function_table[ident][1][val] = self.context[val]
            self.function_table[ident][1]['memory_type'] = ident
            self.context = self.function_table[ident][1]
            if self.context['memory_type'] == ident:
                save_call_state = True
            self.context['memory_type'] = ident
            param_idx = 0
            for param in params_list:
                param = param.strip()
                if param[0].isdigit():
                    new_id = self.function_table[ident][0][param_idx]
                    self.context[new_id] = int(param)
                else:
                    if param in self.memory.keys() and param not in self.context.keys():
                        self.context[param] = self.memory[param]
                    else:
                        new_val = self.context[param]
                        new_id = self.function_table[ident][0][param_idx]
                        self.context[new_id] = new_val
                param_idx += 1
            for val in self.memory.keys():
                if val not in self.context.keys():
                    self.context[val] = self.memory[val]
            if len(params_list) == len(self.function_table[ident][0]):
                return_val = self.visit(self.function_table[ident][2])
                if not save_call_state:
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
        elif ctx.value.text not in self.context.keys() and not ctx.value.text[0].isdigit():
            print(self.context)
            raise Exception('Variable: {val} not defined.'.format(val=ctx.value.text))
        else:
            return int(ctx.value.text)

    def visitParamList(self, ctx):
        return ''.join([stmt.symbol.text for stmt in ctx.children]).split(',')

    def visitParamCallList(self, ctx):
        return ''.join([stmt.symbol.text for stmt in ctx.children]).split(',')

    def visitDecl(self, ctx):
        self.context[ctx.ident.text] = self.visit(ctx.right)

    def visitBlock(self, ctx):
        for stmt in ctx.children:
            if isinstance(stmt, ExprParser.RetrnContext):
                self.return_val = self.visit(stmt)
                return self.return_val
            else:
                self.visit(stmt)
        return self.return_val if isinstance(ctx.parentCtx, ExprParser.FuncDefContext) else 0

    def visitPrintc(self, ctx):
        if ctx.ident.text in self.context.keys():
            print('{iden} = {val}'.format(iden=ctx.ident.text, val=self.context[ctx.ident.text]))
        else:
            raise Exception('Variable: {val} not defined.'.format(val=ctx.ident.text))

    def visitCondition(self, ctx):
        leftVal = self.context[ctx.left.text]
        op = ctx.op.type
        rightVal = None
        if ctx.right.text in self.context.keys() and not(ctx.right.text[0].isdigit()):
            rightVal = self.context[ctx.right.text]
        elif ctx.right.text in self.context.keys() and ctx.right.text[0].isdigit():
            print(self.context)
            raise Exception('Variable: {val} not defined.'.format(val=ctx.right.text))
        else:
            rightVal = int(ctx.right.text)
        if op == ExprParser.EQ:
            return leftVal == rightVal
        elif op == ExprParser.NEQ:
            return leftVal != rightVal
        elif op == ExprParser.LT:
            return leftVal < rightVal
        elif op == ExprParser.LTEQ:
            return leftVal <= rightVal
        elif op == ExprParser.GT:
            return leftVal > rightVal
        elif op == ExprParser.GTEQ:
            return leftVal >= rightVal
        else:
            raise Exception('Operator: {op} not supported here'.format(op=ctx.op))

    def visitCtrlStruct(self, ctx):
        if ctx.whileStr:
            return self.visit(ctx.whileStr)
        if ctx.ifStr:
            return self.visit(ctx.ifStr)

        return None

    def visitWhileStruct(self, ctx):
        cond = self.visit(ctx.cond)
        while cond:
            self.visit(ctx.bl)
            cond = self.visit(ctx.cond)

        return None

    def visitIfStruct(self, ctx):
        cond = self.visit(ctx.cond)
        if cond:
            return self.visit(ctx.bl)
        else:
            return self.visit(ctx.bl2)