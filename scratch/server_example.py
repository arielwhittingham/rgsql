import socket

# this is creating a serer socket that has the AF_INET type which is an internet socket
# and SOCK_STREAM is what creates a tcp connection

_ip = 'localhost'
_port = 3003
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((_ip, _port))

# 3 max connections
server.listen(3)
stop_server = False
try:
    while not stop_server:
        # the address of the client that connects
        # the client instance that connects(used to communicate with the other client the clients
        # socket)
        print("waiting to accept\n ")
        client, address = server.accept()
        try:
            while True:
                print('Connected to this address:', address)

                # received message
                msg = client.recv(1024)
                if not msg:
                    break
                print(msg.decode())
                if msg == b"\0":
                    print("null byte, received -  closing.")
                    stop_server = True
                    break
                # send a message to the client
                client.sendall('Hello from the server python file'.encode())
                continue
        finally:
            client.close()


except socket.error as e:
    print(f"Socket error: {e}")
except KeyboardInterrupt:
    print("Server stopped by user.")
finally:
    print("Closing server socket.")
    server.close()