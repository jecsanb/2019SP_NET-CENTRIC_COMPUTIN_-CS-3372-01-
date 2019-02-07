#!/usr/bin/python
import socket

WEB_HOST = socket.gethostname()
PORT = "8080"


def main():
    request = "GET / HTTP/1.1\r\n" \
              "Host: " + WEB_HOST + "\r\n" \
                                    "Accept: text/html\r\n\r\n"
    print(request)

    s = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    # now connect to the web server on port 80
    # - the normal http port
    s.connect((WEB_HOST, int(PORT)))
    s.send(request.encode())
    s.settimeout(1)
    answer = s.recv(1024)
    print(str(answer))


if __name__ == '__main__':
    main()
