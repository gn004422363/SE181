"""
    This class connecting to the server.py and send/receive
    information.
"""

import socket

# getting the hostname by socket.gethostname() method
hostname = socket.gethostname()

# getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)

class Network():
    def __init__(self):
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server = ip_address
        self.port = 5555
        self.addr = (self.server, self.port)

    # Connect client to the server
    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2048).decode()
        except:
            pass
    # Send signal to server
    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2048)

        except socket.error as e:
            print(str(e))