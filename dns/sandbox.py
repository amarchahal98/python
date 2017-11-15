# ( Import Modules)

import dns
import os
import socket
import sys
from dns import resolver


def compare_mailserver(mx, domain):
    mxfile = open('mailserver.txt', 'r')
    for line in mxfile:
        if line.strip() == mx:
            print('pass: ', mx)
           #break

        else:
            print('no pass: ', mx)

def mx_resolver(domain):
    data = dns.resolver.query(domain, 'MX')
    check = False
    for mx in data:
        url = str(mx)
        newurl = url.strip()
        compare_mailserver(newurl, domain)

if len(sys.argv) == 2:
    mx_resolver(sys.argv[1])
elif not sys.stdin.isatty():
    for line in sys.stdin:
        mx_resolver(line.strip());

