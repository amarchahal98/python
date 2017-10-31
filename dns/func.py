
# (Import Modules)
import os
import socket
import sys

# (FUNC)

def check_vcn(domain):
    VCN_IP = "207.102.64."

    try:
        ip = socket.gethostbyname(domain)
        # (If domain matches VCN's IP)
        if ip.startswith(VCN_IP):
            print("VCN Domain: " + domain)

        # (If domain does not match VCN's IP)
        elif not ip.startswith(VCN_IP):
            print("Non-VCN Domain: " + domain)

    # (If DNS query was not successful)
    except socket.gaierror:
        print("Invalid Domain: " + domain)


def main(argv):

    usage = True
    if not sys.stdin.isatty():
        for line in sys.stdin.readlines():
            check_vcn(line.strip())
        usage = False

    if len(argv) >=1:
        for arg in argv:
            check_vcn(arg)
        usage = False
    if usage:
        print("usage1")
        

if __name__ == '__main__':
    main(sys.argv[1:])
