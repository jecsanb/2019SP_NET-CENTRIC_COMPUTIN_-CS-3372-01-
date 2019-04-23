#! /usr/bin/env python2.7
# Jecsan Blanco
# 2019SP NET-CENTRIC COMPUTIN (CS-3372-01)

from scapy.all import *


def get_reply_packet(packet):
    print("Replying...ง •̀_•́)ง")
    reply = packet.copy()
    reply.src = packet.dst
    reply.dst = packet.src
    reply[IP].src = packet[IP].dst
    reply[IP].dst = packet[IP].src
    reply[ICMP].type = 0
    return reply


def print_info(packet):
    src = packet[IP].src
    dst = packet[IP].dst
    seq = str(packet[ICMP].seq)
    chksum = str(packet[ICMP].chksum)
    # print(packet.command())
    print("Source: " + src)
    print("Dest: " + dst)
    print("ICMP sequence number: " + seq)
    print("ICMP checksum: " + chksum)
    print()


def main():
    print("Sniffing...~(˘▾˘~)")
    #  1 The program will sniff the network listening for icmp echo requests.
    packets = sniff(filter="icmp[icmptype] == icmp-echo", count=5)
    packet_count = 1
    for packet in packets:
        print("count: %s" % packet_count)
        print_info(packet)

        reply = get_reply_packet(packet)

        print_info(reply)
        sendp(reply)
        packet_count += 1
    print("Stopping...(⌐■_■)")


if __name__ == '__main__': main()
