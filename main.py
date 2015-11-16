from lang.ExprLexer import ExprLexer
from lang.ExprParser import ExprParser
from lang.Printer import Printer
from antlr4 import *

if __name__ == '__main__':
    fin = FileStream('test.mam')
    lexer = ExprLexer(fin)
    tokens = CommonTokenStream(lexer)
    parser = ExprParser(tokens)

    tree = parser.prog()
    printer = Printer()
    print(printer.visit(tree))
    print('Done.')