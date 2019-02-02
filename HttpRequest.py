#!/usr/bin/python3
# classes bellow do not do any data validation
class RequestLine:
    def __init__(self, method, url, version):
        self.METHOD = method
        self.URL = url
        self.VERSION = version

    def getmethod(self):
        return self.METHOD

    def geturl(self):
        return self.URL

    def getversion(self):
        return self.VERSION

    def __str__(self):
        return f'{self.METHOD} {self.URL} {self.VERSION}\r\n'


class HeaderField:
    def __init__(self, name, value):
        self.NAME = name
        self.VALUE = value

    def __str__(self):
        return f'{self.NAME} {self.VALUE}\r\n'


class HeaderLines:
    def __init__(self, headerfield):
        self.HEADER_LINES = [headerfield]

    def addfield(self, headerfield):
        self.HEADER_LINES.append(headerfield)

    def count(self):
        return len(self.HEADER_LINES)

    def __str__(self):
        ans = ""
        for line in self.HEADER_LINES:
            ans += str(line)
        return ans


class EntityBody:
    def __init__(self, data):
        self.DATA = data

    def __str__(self):
        return str(self.DATA)


class HttpRequest:
    def __init__(self, requestline, headerlines, entitybody):
        self.REQUEST_LINE = requestline
        self.HEADER_LINES = headerlines
        self.ENTITY_BODY = entitybody

    def getrequestline(self):
        return self.REQUEST_LINE

    def getheaderlines(self):
        return self.HEADER_LINES

    def getentitybody(self):
        return self.ENTITY_BODY

    def __str__(self):
        return f'{str(self.REQUEST_LINE)}{str(self.HEADER_LINES)}\r\n{self.ENTITY_BODY}'


def main():
    rl = RequestLine("GET", "/hello.htm", "HTTP/1.1")
    hf = HeaderField("User-Agent:", "Mozilla/4.0")
    hl = HeaderLines(hf)
    eb = EntityBody("Data is here")
    hr = HttpRequest(rl, hl, eb)
    print(hr, end="")


if __name__ == '__main__':
    main()
