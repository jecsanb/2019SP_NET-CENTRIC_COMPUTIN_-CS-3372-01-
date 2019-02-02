#!/usr/bin/python
import socket


def main():
    s = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    # now connect to the web server on port 80
    # - the normal http port
    s.connect((socket.gethostname(), 8080))
    message = "Hello!"
    s.send(message.encode())


if __name__ == '__main__':
    main()
