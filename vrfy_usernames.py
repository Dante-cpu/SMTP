#!/usr/bin/python

import socket
import sys

def verify_username(ip_address, username):
    # Create a socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        s.connect((ip_address, 25))

        # Receive the banner
        banner = s.recv(1024)
        print(f"Banner from {ip_address}: {banner.decode()}")

        # VRFY a user
        s.send(f'VRFY {username}\r\n')
        result = s.recv(1024)
        print(f"VRFY result for {username}: {result.decode()}")

    except socket.error as e:
        print(f"Socket error for {ip_address}: {e}")
    finally:
        # Close the socket
        s.close()

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: vrfy.py <ip_address> <username_file>")
        print("Example: vrfy.py 192.168.1.1 usernames.txt")
        sys.exit(0)

    ip_address = sys.argv[1]
    username_file = sys.argv[2]

    try:
        with open(username_file, 'r') as file:
            usernames = file.readlines()
            for username in usernames:
                username = username.strip()
                if username:
                    verify_username(ip_address, username)
    except FileNotFoundError:
        print(f"File not found: {username_file}")
    except Exception as e:
        print(f"An error occurred: {e}")