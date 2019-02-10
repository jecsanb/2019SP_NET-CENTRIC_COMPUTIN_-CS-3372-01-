#!/usr/local/bin/python3

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

DEFAULT_MAIL_SERVER = 'localhost'
DEFAULT_PORT = '25'

GOOD_REPLY = ['220', '250', '354', '221']


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

    hello = "HELO %s\r\n" % str(socket.gethostname())
    sender = "MAIL FROM: <%s>\r\n"
    recipient = "RCPT TO: <%s>\r\n"
    subject = "Subject: %s\r\n"
    data = "DATA\r\n"
    body = "%s\r\n"
    bye = "QUIT\r\n"

    server = input("Enter destination server: ").strip()
    sender = sender % input("From: ").strip()
    recipient = recipient % input("To: ").strip()
    subject = subject % input("Subject: ").strip()
    body = body % input("Body:\n").strip()
    msg = sender[5:] + recipient[5:] + subject + body + "\r\n.\r\n"

    commands = [hello, sender, recipient, data, msg, bye]

    s = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.connect((server, int(port)))
    reply = s.recv(1024).decode().split()
    error = False
    for command in commands:
        print("s: %s" % reply)
        if reply[0] not in GOOD_REPLY:
            error = True
            break
        print("c: %s" % command)
        s.send(command.encode())
        reply = s.recv(1024).decode().split()

    if error is True:
        print("Error Occurred: %s\n" % reply)
        s.send(bye.encode())

    else:
        print("s: %s" % reply)

    s.close()
    print("client stopping")


if __name__ == '__main__':
    main()
# S: 220 smtp.example.com ESMTP Postfix
# C: HELO relay.example.com
# S: 250 smtp.example.com, I am glad to meet you
# C: MAIL FROM:<bob@example.com>
# S: 250 Ok
# C: RCPT TO:<alice@example.com>
# S: 250 Ok
# C: RCPT TO:<theboss@example.com>
# S: 250 Ok
# C: DATA
# S: 354 End data with <CR><LF>.<CR><LF>
# C: From: "Bob Example" <bob@example.com>
# C: To: Alice Example <alice@example.com>
# C: Cc: theboss@example.com
# C: Date: Tue, 15 January 2008 16:02:43 -0500
# C: Subject: Test message
# C:
# C: Hello Alice.
# C: This is a test message with 5 header fields and 4 lines in the message body.
# C: Your friend,
# C: Bob
# C: .
# S: 250 Ok: queued as 12345
# C: QUIT
# S: 221 Bye
# {The server closes the connection}
