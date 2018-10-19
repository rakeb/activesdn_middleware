#!/usr/bin/env python3
"""
Very simple HTTP server in python for logging requests
Usage::
    ./server.py [<port>]
"""
# mdonkers/server.py
# https://gist.github.com/mdonkers/63e115cc0c79b4f6b8b3a6b797e485c7
import logging
from http.server import BaseHTTPRequestHandler, HTTPServer

from api.handler import notification_handler


class S(BaseHTTPRequestHandler):
    def _set_response(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        self._set_response()
        self.wfile.write("GET request for {}".format(self.path).encode('utf-8'))

    def do_POST(self):
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself
        logging.info("POST request,\nPath: %s\nHeaders:\n%s\n\nBody:\n%s\n",
                     str(self.path), str(self.headers), post_data.decode('utf-8'))
        data = post_data.decode('utf-8')
        # print(data)

        self._set_response()
        self.wfile.write("POST request for {}".format(self.path).encode('utf-8'))

        # TODO checking notification as queue
        # notification_handler.handle_notification(data)

        notificationQueue = notification_handler.getNotificationQueue()
        notificationQueue.put(data)


def s_run(server_class=HTTPServer, handler_class=S, port=5555):
    logging.basicConfig(level=logging.INFO)
    print(port)
    server_address = ('172.16.53.1', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting httpd...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping httpd...\n')


if __name__ == '__main__':
    from sys import argv

    if len(argv) == 2:
        s_run(port=int(argv[1]))
    else:
        s_run()
