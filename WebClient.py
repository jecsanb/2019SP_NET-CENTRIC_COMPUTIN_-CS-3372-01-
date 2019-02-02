#!/usr/bin/python
import socket


def main():
    s = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    # now connect to the web server on port 80
    # - the normal http port
    s.connect((socket.gethostname(), 8080))
    data = s.recv(1024).decode()
    print("Server: " + str(data))
    data = "Hi!!!!!!!!!".encode()
    s.send(data)


if __name__ == '__main__':
    main()
