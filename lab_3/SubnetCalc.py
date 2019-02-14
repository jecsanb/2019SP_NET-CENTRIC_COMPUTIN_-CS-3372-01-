#!/usr/bin/env python3
def isvalidipv4(address):
    valid = False
    candidate = str(address).split('.')
    if len(candidate) == 4:
        for octet in candidate:
            valid = True if (octet.isalnum() and 0 <= int(octet) <= 255) else False
            if not valid:
                break
    return valid


def main():
    ipv4 = str(input('Enter ipv4 address: ')).strip()
    print(isvalidipv4(ipv4))


if __name__ == '__main__':
    main()
