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


def main():
    port = "8080"
    if len(sys.argv) >= 2:
        port = (str(sys.argv[1])).strip()
    # print('Number of arguments:', len(sys.argv), 'arguments.')
    # print('The port was ', port)


if __name__ == '__main__':
    main()
