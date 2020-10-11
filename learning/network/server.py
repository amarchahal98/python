#!/usr/bin/python3

import socket

# Create Socket Object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get Local Machine Name
host = socket.gethostname()

port = 9999

# Bind to the port
serversocket.bind((host, port))

# Queue up to 5 requests
serversocket.listen(5)

while True:
    clientsocket,addr = serversocket.accept()

    print("Got a connection from " + str(addr))
    msg = "thank you for connecting, " + "\r\n"
    clientsocket.send(msg.encode('ascii'))
    clientsocket.close()

