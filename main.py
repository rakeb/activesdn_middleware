from translator.parser.policy_parser import parser
from sys import argv

if __name__ == '__main__':
	if (len(argv) > 1):
		parser(argv[1])
	else:
		parser('translator/lexer/rule.txt')
