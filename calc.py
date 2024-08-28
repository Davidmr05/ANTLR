
import sys
from antlr4 import *
from antlr4.InputStream import InputStream
from LabeledExprLexer import LabeledExprLexer
from LabeledExprParser import LabeledExprParser
from MyVisitor1 import MyVisitor1
from MyVisitor2 import MyVisitor2

if __name__ == '__main__':
	if len(sys.argv) > 1:
		input_stream = FileStream(sys.argv[1])
	else:
		input_stream = InputStream(sys.stdin.readline())
	a = 2

	while(True):
		print("Seleccione la asociacion ")
		print("1. Por la derecha")
		print("2. Por la izquierda")
		x = input()
		if (x == "1"):
			print("Los resultados son: ")
			lexer = LabeledExprLexer(input_stream)
			token_stream = CommonTokenStream(lexer)
			parser = LabeledExprParser(token_stream)
			tree = parser.prog()
			visitor = MyVisitor1()
			visitor.visit(tree)
			break

		elif (x == "2"):
			print("Los resultados son: ")
			lexer = LabeledExprLexer(input_stream)
			token_stream = CommonTokenStream(lexer)
			parser = LabeledExprParser(token_stream)
			tree = parser.prog()
			visitor = MyVisitor2()
			visitor.visit(tree)
			break
		else :
			print("Seleccione una opcion correcta")
