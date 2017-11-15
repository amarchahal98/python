#( Import Modules)

import dns
import os
import socket
import sys
from dns import resolver

def compare_mailserver(mailserver, domain):
    mxfile = open('mailserver.txt', 'r')
    check = False
    for line in mxfile:
        if line.strip() == mailserver:
            check = True
            break
    if not check:
        print(domain)

def mx_resolver(domain):
    try:
        data = dns.resolver.query(domain, 'MX')
        mx_match = False
        for server in data:
            url = str(server)
            if mx_match == False:
                mx_match = compare_mailserver(url, domain)
            
    except dns.resolver.NoAnswer:
        print('No MX Record: ', domain)

if len(sys.argv) == 2:
    mx_resolver(sys.argv[1])
elif not sys.stdin.isatty():
    for line in sys.stdin:
        mx_resolver(line.strip())

else:
    print('Usage: python ', sys.argv[0], '"domain name"')
    print('Usage: cat "text file" | python ', sys.argv[0])
