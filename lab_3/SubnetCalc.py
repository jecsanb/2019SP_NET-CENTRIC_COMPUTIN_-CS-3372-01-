#!/usr/bin/env python3
__author__ = "Jecsan Blanco"


def is_valid_ip4(address):
    """Check if address is a valid ipv4 address"""
    valid = False
    candidate = str(address).split('.')
    if len(candidate) == 4:
        for octet in candidate:
            valid = True if (octet.isalnum() and 0 <= int(octet) <= 255) else False
            if not valid:
                break
    return valid


def is_valid_mask(mask):
    return str(mask).isdigit() and (True if 1 <= int(mask) <= 32 else False)


def bin_to_ip4(binary):
    """ Converts a 32 bit binary string in to an ipv4 formatted address"""
    if len(binary) != 32:
        print("Error, invalid binary length")
        return None
    n = 8
    # break in to four octets and convert back to decimal
    octets = [binary[i:i + n] for i in range(0, len(binary), n)]
    octets[:] = [str(int(i, 2)) for i in octets]
    return '.'.join(octets)


def ip4_to_bin(address):
    """ Converts a ipv4 formatted address in to a 32 bit binary string """
    if not is_valid_ip4(address):
        print("Error, invalid ip")
        return None
    # break in to 4 decimals and convert to 8 bit binary
    octets = address.split(".")
    octets[:] = [format(int(i), '08b') for i in octets]
    return ''.join(octets)


def main():
    while True:
        # read needed input
        ipv4 = input('Enter ipv4 address: ').strip()
        mask = input('Enter mask bits: ').strip()
        if not is_valid_ip4(ipv4) and not is_valid_mask(mask):
            print("Invalid address or mask")
        else:
            break
    mask = int(mask)
    subnet_mask = "1" * mask + "0" * (32 - mask)

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
