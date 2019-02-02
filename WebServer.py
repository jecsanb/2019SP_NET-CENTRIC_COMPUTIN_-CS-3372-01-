#!/usr/bin/python3

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
import os
import socket


def fetchfile(rootpath, filename):
    for root, dirs, files in os.walk(rootpath):
        for name in files:
            if name == filename:
                print(os.path.join(root, name))
                return
    print("404")


def main():
    # Change port if a command line argument was provided
    if len(sys.argv) >= 2:
        port = (str(sys.argv[1])).strip()
        if not port.isdigit():
            print('Invalid port number.')
            exit()
    else:
        port = "8080"
    # print('Number of arguments:', len(sys.argv), 'arguments.')
    # print('The port was ', port)

    # init socket
    serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((socket.gethostname(), int(port)))
    serversocket.listen(5)
    # process the requests when connected
    while 1:
        print("Listening on port " + port + "...")
        # accept connections from outside
        (clientsocket, address) = serversocket.accept()
        # now do something with the clientsocket
        print("Connected to client: " + str(address))
        data = "Hello " + str(address) + " my name is " + str(socket.gethostname())
        clientsocket.send(data.encode())
        data = clientsocket.recv(1024).decode()
        print("Client: " + str(data))


if __name__ == '__main__':
    main()
