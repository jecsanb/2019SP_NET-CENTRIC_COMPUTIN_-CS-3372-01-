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

ROOT_PATH = "./"
DEFAULT_PORT = "8080"


def getfilecontents(file):
    # print("File requested: " + file)
    data = None
    for filename in os.listdir(ROOT_PATH):
        if os.path.isfile(filename) and file == filename:
            # print(os.path.join("./", filename))
            f = open(filename, "+r")
            data = f.read()
            break
    return data


def main():
    # Change port if a command line argument was provided
    if len(sys.argv) >= 2:
        port = (str(sys.argv[1])).strip()
        if not port.isdigit():
            print('Invalid port number.')
            exit()
    else:
        port = DEFAULT_PORT
    # print('Number of arguments:', len(sys.argv), 'arguments.')
    # print('The port was ', port)

    # init socket
    serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind((socket.gethostname(), int(port)))
    serversocket.listen(5)

    # process the requests when connected
    print("Listening on port: " + str(port))

    # accept connections from outside
    (clientsocket, address) = serversocket.accept()

    # now do something with the clientsocket
    print("Connected to client: " + str(address))

    data = clientsocket.recv(1024).decode().split(" ")
    request = data[0]

    # check for GET, server only accpets GET requests
    if request != 'GET':
        clientsocket.send("HTTP/1.1 400 Bad Request\r\n".encode())
        quit()
    data = getfilecontents(data[1])
    if data is None:
        clientsocket.send("HTTP/1.1 404 Not Found\r\n".encode())
    else:
        clientsocket.send(data.encode())

    clientsocket.close()
    serversocket.close()


if __name__ == '__main__':
    main()
