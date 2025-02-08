#!/usr/bin/python

import socket
import sys
import ipaddress

def scan_network(ip_range, username):
    network = ipaddress.ip_network(ip_range, strict=False)
    for ip in network.hosts():
        ip_address = str(ip)
        print(f"Scanning {ip_address}...")
        try:
            # Create a socket
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(5)  # Set a timeout for the connection attempt

            # Connect to the server
            s.connect((ip_address, 25))

            # Receive the banner
            banner = s.recv(1024)
            print(f"Banner from {ip_address}: {banner.decode()}")

            # VRFY a user
            s.send(f'VRFY {username}\r\n')
            result = s.recv(1024)
            print(f"VRFY result from {ip_address}: {result.decode()}")

            # Close the socket
            s.close()

        except socket.error as e:
            print(f"Socket error for {ip_address}: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: scan_smtp.py <ip_range> <username>")
        print("Example: scan_smtp.py 192.168.1.0/24 testuser")
        sys.exit(0)

    ip_range = sys.argv[1]
    username = sys.argv[2]

    scan_network(ip_range, username)
