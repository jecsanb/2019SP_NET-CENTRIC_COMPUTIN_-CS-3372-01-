#!/usr/bin/python

# Jecsan Blanco
# 2019SP NET-CENTRIC COMPUTIN (CS-3372-01)
# Hint: The socket module from python will be very useful.
# In this assignment you will develop a program that will send an email message using SMTP using Python
# with the following requirements:
# 1 The program will ask for the following information:
# a. Destination server (fqdn or IP address)
# b. Sender email address
# c. Recipient email address
# d. Subject
# e. Body
# 2 Your program will initiate a connection to port 25 of the destination and communicate with
# the server to send the email.
# 3 Your program will display the result from the destination server. (Typically the last message
# from the server such as queued for delivery)
# 4 The program will exit after the email has been delivered.
import sys
import socket
import os

DEFAULT_PORT = '8080'


def main():
    print("Client started.")
    # Change port if a command line argument was provided
    if len(sys.argv) >= 2:
        port = (str(sys.argv[1])).strip()
        if not port.isdigit():
            print('Invalid port number.')
            exit()
    else:
        port = DEFAULT_PORT

    print("Client stopped.")

if __name__ == '__main__':
    main()
