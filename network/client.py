#!/usr/bin/python3

import socket

# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get Local Machine Name
host = socket.gethostname()

port = 9999


# Connection to hostname on the port
s.connect((host, port))

# Receive up to 1024 bytes
msg = s.recv(1024)

s.close()
print(msg.decode('ascii'))

