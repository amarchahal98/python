# Testing isatty functionality (Is stdin being piped?)

import sys
# (Interactive)
if sys.stdin.isatty():
    print("isatty")

# (Data is being piped)
elif not sys.stdin.isatty():
    print("not isatty")
