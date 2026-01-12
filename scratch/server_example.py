import socket

# this is creating a serer socket that has the AF_INET type which is an internet socket
# and SOCK_STREAM is what creates a tcp connection

_ip = 'localhost'
_port = 9999
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((_ip, _port))

# 3 max connections
server.listen(3)

while True:
    # the address of the cliet that connects
    # the client instance that connects(used to communicate with the other client the clients
    # socket)
    client, address = server.accept()

    print('Connected to this address:', address)

    # received message
    print(client.recv(1024).decode())

    # send a message to the client
    client.send('Hello from the server python file'.encode())


