# https://www.datacamp.com/tutorial/a-complete-guide-to-socket-programming-in-python

# https://github.com/sshlafman/PP4E/blob/master/System/Processes/socket_preview.py

import socket

_SERVER_IP = "127.0.0.1"
_PORT = 8000

def run_server():
    # server code
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((_SERVER_IP, _PORT))

