#!/usr/bin/python

# Jecsan Blanco
# 2019SP NET-CENTRIC COMPUTIN (CS-3372-01)
# In this assignment you will develop a simple web server using Python with the following requirements:
#
# 1 The port can be defined at the command line, else it defaults to 8080.
# (ex. server.py 8888)
#
# 2 The content for the webserver will be directory where the server is run from.
#
# 3 A 404 error message will be displayed for any file that is not found.
#
# 4 The program will terminate after responding to the first request
#
# Hint: The socket module from python will be very useful.
import sys
import socket
import os

ROOT_PATH = './'
DEFAULT_PORT = '8080'

# check for GET, server only accepts GET requests
HTTP_200 = 'http/1.1 200 OK\r\n'
HTTP_404 = 'HTTP/1.1 404 File Not Found\r\n'
HTTP_500 = 'HTTP/1.1 500 Internal Server Error\r\n'

NOTFOUND_HTML = '<!doctype html><head> <meta charset="UTF-8">' \
                '<title>Sorry Not Found</title> </head> <body> <h1>404 File ' \
                'Not Found </h1> </body> </html>'
INTERNAL_ERR_HTML = '<!doctype html><head> <meta charset="UTF-8">' \
                    '<title>Error</title> </head> <body> <h1>Server Error,' \
                    ' Checking Hamsters </h1> </body> </html>'
BLK_LINE = '\r\n'
HDR_LINES = 'Connection: close\r\n' \
            'Content-Type: text/html\r\n'


def main():
    # Change port if a command line argument was provided
    if len(sys.argv) >= 2:
        port = (str(sys.argv[1])).strip()
        if not port.isdigit():
            print('Invalid port number.')
            exit()
    else:
        port = DEFAULT_PORT

    serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(("localhost", int(port)))
    serversocket.listen(5)

    while 1:
        # process the requests when connected
        print('Listening on port: ' + str(port))

        # accept connections from outside
        (clientsocket, address) = serversocket.accept()

        # now do something with the clientsocket
        print('Connected to client: ' + str(address))

        request = clientsocket.recv(1024).decode()
        filename = ROOT_PATH + request.split(' ')[1]
        reply = HTTP_404
        data = NOTFOUND_HTML

        if os.path.isfile(filename):
            data = open(filename).read()
            reply = HTTP_200

        reply += HDR_LINES + BLK_LINE + data
        print("Reply:\n" + reply)
        # print(reply)
        clientsocket.send(reply.encode())
        clientsocket.close()
        break

    serversocket.close()


if __name__ == '__main__':
    main()
