#! /usr/bin/env python2.7
from scapy.all import *


def main():
    pcap_filename = None
    if len(sys.argv) >= 2:
        # The program will accept the filename of a pcap file on the command line. This can be accomplished with argv
        pcap_filename = (str(sys.argv[1])).strip()
    else:
        pcap_filename = 'Assignment5.pcapng'
        # exit()
    # 2 The program will read in the pcap file. This can be done with rdpcap in the scapy module.
    packets = rdpcap(pcap_filename)
    packet = packets[0]
    print(packet.summary())
    print(packet.show())
    #  The program will display the following information from the 1st packet of the pcap file.
    # a. Source IP address
    print("Source IP:   \t%s" % packet[ARP].psrc)
    # b. Requested IP address
    print("Requested IP:\t%s" % packet[ARP].pdst)
    # c. Source hardware address
    print("Source MAC:  \t%s" % packet.src)
    # d. Destination hardware address
    print("Dest  MAC:   \t%s" % packet.dst)


if __name__ == '__main__':
    main()
