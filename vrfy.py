#!/usr/bin/python

import socket
import sys

if len(sys.argv) != 3:
    print("Usage: vrfy.py <username> <ip_address>")
    sys.exit(0)

username = sys.argv[1]
ip_address = sys.argv[2]

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to the server
    s.connect((ip_address, 25))

    # Receive the banner
    banner = s.recv(1024)
    print(banner)

    # VRFY a user
    s.send('VRFY ' + username + '\r\n')
    result = s.recv(1024)
    print(result)

except socket.error as e:
    print(f"Socket error: {e}")
finally:
    # Close the socket
    s.close()
