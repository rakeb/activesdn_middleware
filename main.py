from sys import argv

from translator.parser.policy_parser import parser

if __name__ == '__main__':
	if (len(argv) > 1):
		parser(argv[1])
	else:
		parser('translator/lexer/rule.txt')
