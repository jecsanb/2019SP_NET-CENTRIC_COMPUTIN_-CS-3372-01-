#!/usr/bin/env python3
__author__ = 'Jecsan Blanco'

# A basic ipv4 subnet calculator


def is_valid_ip4(address):
    # Check if address is a valid ipv4 address
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
    # Converts a 32 bit number in to an ipv4 formatted string
    mask = 255
    octets = []
    # turn each octet in to a decimal format
    for i in range(0, 4):
        octets.append(str(binary & mask))
        binary = binary >> 8
    # add the . separators
    return '.'.join(reversed(octets))


def ip4_to_bin(address):
    #  Converts a ipv4 formatted address string in to a 32 bit binary number
    if not is_valid_ip4(address):
        print('Error, invalid ip')
        return None
    # break in to 4 decimals
    octets = address.split('.')
    number = 0
    # create one binary string
    for octet in octets:
        number = (number << 8) | int(octet)
    return number


def main():
    while True:
        # read needed input
        ipv4 = input('Enter ipv4 address: ').strip()
        mask = input('Enter mask bits: ').strip()
        if is_valid_ip4(ipv4) and is_valid_mask(mask):
            break
        else:
            print('Invalid address or mask')
    mask = int(mask)
    subnet_mask = -1 << (32 - mask)
    network_mask = ~subnet_mask
    bin_ip = ip4_to_bin(ipv4)
    subnet_id = subnet_mask & bin_ip

    # a. Subnet or Network ID (first IP address in the network range)
    print('Subnet ID: %s ' % bin_to_ip4(subnet_id))
    # b. Broadcast Address (last IP in the network range)
    print('Broadcast Address: %s' % bin_to_ip4(subnet_id | network_mask))
    # c. Subnet Mask in decimal form (i.e. 255.255.255.192)
    print('Subnet Mask: %s' % bin_to_ip4(subnet_mask))
    # d. Maximum number of hosts allowed in the network
    print('Hosts: %s' % str(1 if mask == 32 else network_mask - 1))


if __name__ == '__main__':
    main()
