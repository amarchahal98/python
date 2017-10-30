import sys
import socket
import os

var = str(sys.argv[1])
ip = socket.gethostbyname(var)

GO_IP = "216.58.216."
print(ip)
if ip.startswith(GO_IP):
    print(var)

