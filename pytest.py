import sys
import socket
import os

var = str(sys.argv[1])
ip = socket.gethostbyname(var)

print(ip)
