import threading
from sys import argv

from api.handler import notification_handler
from middleware.prolog.prolog_generator import generate_prolog_file
from middleware.python import python_api_caller
from translator.parser.policy_parser import parser
from api.receive import http_receive

if __name__ == '__main__':
    rule = None
    if len(argv) > 1:
        rule = parser(argv[1])
    else:
        rule = parser('translator/lexer/rule.txt')

    # prolog generation
    generate_prolog_file(rule, "prolog.pl")

    # strating http server to receive activesdn responses
    http_server_thread = threading.Thread(target=http_receive.s_run, args=())
    # http_server_thread.setDaemon(True)
    http_server_thread.start()

    # start api calling
    python_api_caller.event_caller(rule)

    # notification handler will get the rule
    notification_handler.setRule(rule)
    notification_thread = threading.Thread(target=notification_handler.handle_notification, args=())
    # notification_thread.setDaemon(True)
    notification_thread.start()

    # TODO for mocking server
    # python_api_caller.coa_caller(rule, 'openflow:1:4')
    print("Main quit, however Middleware server still listening...")
