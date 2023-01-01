import os
import socket

# Host and port of server
server_host = "server.example.com"
server_port = 12345

# Host and directory to scan
host = "host.example.com"
directory = "/path/to/directory"

# Connect to server
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((server_host, server_port))

# Send request to scan directory
sock.sendall(f"SCAN {host} {directory}\n".encode())

# Receive and print response from server
response = sock.recv(1024).decode()
print(response)

# Close socket
sock.close()
