#!/usr/bin/python3

import sys
import os
import base64

filename = sys.argv[1] 
f = open(filename, "r")


for line in f:
    lineb = line.encode("ascii")
    b64bytes = base64.b64encode(lineb)
    b64string = b64bytes.decode("ascii")
    print(b64string)
