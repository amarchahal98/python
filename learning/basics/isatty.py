# Testing isatty functionality (Is stdin being piped?)

import sys
# (Interactive)
if sys.stdin.isatty():
    print("No stdin was piped")

# (Data is being piped)
elif not sys.stdin.isatty():
    print("Data is being piped")
