import socket


_ip = 'localhost'
_port = 9999


# SOCK_STREAM: tcp socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((_ip, _port))

client.send('Hi i am the client'.encode())

print(client.recv(1024).decode())

