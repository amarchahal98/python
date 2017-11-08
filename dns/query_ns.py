import dns
import os
import sys
from dns import resolver

compareTo = "vcn.bc.ca"

def compare_nameserver(nameserver, domain_name):
    serverfile = open('nameserver.txt', 'r')
    check = False
    for line in serverfile:
        if line.strip() == nameserver:
            check = True
            break
    if not check:
        print(domain_name)

def lookingup_dns(domain_name):
    try:
        data = dns.resolver.query(domain_name, "NS")

        for server in data:
            url = str(server)
            if not url.endswith(compareTo + "."):
                print("option 1: ", domain_name)
                return
            elif url.endswith(compareTo + "."):
                print("option 2: ", domain_name)
                compare_nameserver(url[:-1], domain_name)

    except:
        print("option3: ", domain_name)


def main(argv):
    usage = True
    if not sys.stdin.isatty():
        for line in sys.stdin.readlines():
            lookingup_dns(line.strip())
        usage = False
    if len(sys.argv) >= 1:
        for arg in argv:
            lookingup_dns(arg)
        usage = False
    if usage:
        print('Usage: python ', sys.argv[0], '"domain name"')
        print('Usage: cat "text file" | python ', sys.argv[0])

if __name__ == '__main__':
    main(sys.argv[1:])
