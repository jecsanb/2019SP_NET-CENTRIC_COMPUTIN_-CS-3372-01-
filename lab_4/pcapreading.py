#! /usr/bin/env python2.7
from scapy.all import *

def main():
    pcap_filename = None
    if len(sys.argv) >= 2:
        pcap_filename = (str(sys.argv[1])).strip()
    else:
        pcap_filename = 'Assignment5.pcapng'
        #exit()
    packets = rdpcap(pcap_filename)
    packet = packets[0]
    print(packet.summary())

if __name__ == '__main__':
    main()

