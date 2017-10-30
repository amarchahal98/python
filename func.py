import os
import socket
import sys

# (VARS)

VCN_IP = "207.102.64."
domain_name = str(sys.argv[1])

def check_vcn(domain_name):
    try:
        ip = socket.gethostbyname(domain_name)
        if ip.startswith(VCN_IP):
            print("VCN Domain: " + domain_name)

        elif not ip.startswith(VCN_IP):
            print("Non-VCN Domain: " + domain_name)
    except socket.gaierror:
        print("Invalid Domain: " + domain_name)

check_vcn(domain_name)
