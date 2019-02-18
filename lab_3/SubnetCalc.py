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
    return True if 1 <= int(mask) <= 32 else False

def main():
    ipv4_octets = []
    while True:
        # read needed input
        ipv4 = input('Enter ipv4 address: ').strip()
        mask = input('Enter mask bits: ').strip()
        if isvalidipv4(ipv4) and isvalidmask(mask):
            ipv4_octets = ipv4.split('.')
            break
        else:
            print("Invalid address or mask")

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
