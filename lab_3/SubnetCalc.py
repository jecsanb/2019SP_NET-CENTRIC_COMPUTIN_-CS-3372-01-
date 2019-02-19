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


def isvalidmask(mask):
    return str(mask).isdigit() and True if 1 <= int(mask) <= 32 else False


def bintoip4(binary):
    if len(binary) != 32:
        print("Error, invalid binary length")
        return None
    n = 8
    octets = [binary[i:i + n] for i in range(0, len(binary), n)]
    octets[:] = [str(int(i, 2)) for i in octets]
    return '.'.join(octets)


def ip4tobin(address):
    if not isvalidipv4(address):
        print("Error, invalid ip")
        return None
    octets = address.split(".")
    octets[:] = [format(int(i), '08b') for i in octets]
    return ''.join(octets)


def main():
    while True:
        # read needed input
        ipv4 = input('Enter ipv4 address: ').strip()
        mask = input('Enter mask bits: ').strip()
        if not isvalidipv4(ipv4) and not isvalidmask(mask):
            print("Invalid address or mask")
        else:
            break
    mask = int(mask)
    subnet_mask = "1"*mask + "0"*(32-mask)

    # a. Subnet or Network ID (first IP address in the network range)
    print("Network Subnet: ")
    # b. Broadcast Address (last IP in the network range)
    print("Broadcast Address:")
    # c. Subnet Mask in decimal form (i.e. 255.255.255.192)
    print("Subnet Mask:")
    # d. Maximum number of hosts allowed in the network
    print("Hosts:")


if __name__ == '__main__':
    main()
