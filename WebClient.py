#!/usr/bin/python3
import socket
import HttpRequest as HReq


def main():
    rl = HReq.RequestLine("GET", "/index.html", "HTTP/1.1")
    hf = HReq.HeaderField("Host:", "localhost")
    hl = HReq.HeaderLines(hf)
    hl.HEADER_LINES.append(HReq.HeaderField("Connection:", "keep-alive"))
    eb = HReq.EntityBody("")
    hr = HReq.HttpRequest(rl, hl, eb)
    s = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    # now connect to the web server on port 80
    # - the normal http port
    s.connect((str(socket.gethostname()), 8080))
    data = str(hr)
    s.send(data.encode())
    data = s.recv(1024).decode()
    print(str(data))


if __name__ == '__main__':
    main()
