#( Import Modules)
import dns
import os
import socket
import sys
from dns import resolver

# (FUNC)

def lookup_mx(mailserver, domain):

    mxlist = dns.resolver.query(domain, 'MX')
    for mx in mxlist:
        print(mx)

def main(argv):
    usage = True
    if not sys.stdin.isatty():
        for line in sys.stdin.readlines():
            lookup_mx(line.strip())
        usage = False
    if len(sys.argv) >= 1:
        for arg in argv:
            lookup_mx(arg)
        usage = False
    if usage:
        print('Usage: python', sys.argv[0], '"[domain name]"')
        print('Usage: cat [text file] | python ', sys.argv[0])


if __name__ == '__main__':
    main(sys.argv[1:])

