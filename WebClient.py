#!/usr/bin/python3
import socket

def main():
    s = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    # now connect to the web server on port 80
    # - the normal http port
    s.connect((socket.gethostname(), 8080))

    data = "GET  ./page.html HTTP/1.1 Host: www.someschool.edu"


if __name__ == '__main__':
    main()
