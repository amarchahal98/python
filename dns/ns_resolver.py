import dns
import os
import sys
from dns import resolver

compareTo = "vcn.bc.ca"


# Comparing Nameserver to VCN's Nameservers

def compare_nameserver(nameserver, domain_name):
    serverfile = open('nameserver.txt')
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

