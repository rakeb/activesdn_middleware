from sys import argv

from middleware.prolog.prolog_generator import generate_prolog_file
from translator.parser.policy_parser import parser

if __name__ == '__main__':
    rule = None
    if len(argv) > 1:
        rule = parser(argv[1])
    else:
        rule = parser('translator/lexer/rule.txt')
    generate_prolog_file(rule,"prolog.pl")
