import os
import socket
import sys

# (VARS)

domain_name = sys.argv[1]
VCN_IP = "207.102.64."

print(domain_name)
ip = socket.gethostbyname(domain_name)

print("\n")

if ip.startswith(VCN_IP):
    print(True)

else:
    print(False)


