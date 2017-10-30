### DNS Lookup Tool ###

# (Import Modules)
import sys
import socket


# (For using arguments as host input)
host=str(sys.argv[1])

# (DNS Lookup [Name to IP])
# print(socket.gethostbyname(host))

# (Reverse DNS Lookup [IP to Name])
result = socket.gethostbyaddr(host)

print(result[0])
