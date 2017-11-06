import dns
import os
import sys
from dns import resolver

compareTo = "vcn.bc.ca"


try:
    print("Replies: ")
    for i in dns.resolver.query(sys.argv[1], "NS"):
        print("\t", str(i))
except:
    print("exception")

