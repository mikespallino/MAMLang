from lang.ExprLexer import ExprLexer
from lang.ExprParser import ExprParser
from lang.Printer import Printer
from lang.Interpreter import Interpreter
from antlr4 import *

if __name__ == '__main__':
    fin = FileStream('test.mam')
    lexer = ExprLexer(fin)
    tokens = CommonTokenStream(lexer)
    parser = ExprParser(tokens)

    tree = parser.prog()
    printer = Printer()
    print(printer.visit(tree))

    interpreter = Interpreter()
    interpreter.visit(tree)

    #calculator = Calculator()
    #result = calculator.visit(tree)
    #for ident in calculator.memory.keys():
    #    print('{idnt} = {value}'.format(idnt=ident, value=calculator.memory[ident]))