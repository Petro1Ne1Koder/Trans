from antlr4 import *
from gen.fLexer import fLexer
from gen.fParser import fParser


def main(file_name):
    input_stream = FileStream(file_name)
    lexer = fLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = fParser(stream)
    parser.program()
    token_stream = parser.getTokenStream()
    for token in token_stream.tokens:
        print(token)


if __name__ == '__main__':
    main('test.f')



