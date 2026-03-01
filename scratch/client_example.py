import socket
import time

_ip = "localhost"
_port = 3003


# SOCK_STREAM: tcp socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((_ip, _port))

# loop through and send automatically

for i in range(100):
    time.sleep(1)
    if i != 9:
        client.send(f"Hi i am the client and this is message # {i}".encode())
        print(client.recv(1024).decode())
        print(0)
    else:
        client.send(b"\0")
        print(client.recv(1024).decode())
        print(1)
        client.close()
        break


