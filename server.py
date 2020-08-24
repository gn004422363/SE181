"""
    This server handling all of the players, it save
    and send server's status to each player.
"""

import socket
from _thread import *
from chessboard import chessboard
import sys

# getting the hostname by socket.gethostname() method
hostname = socket.gethostname()

# getting the IP address using socket.gethostbyname() method
ip_address = socket.gethostbyname(hostname)

server = ip_address
port = 5555

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    s.bind((server, port))
except socket.error as e:
    str(e)


def threaded_client(conn):
    global currentId, connections
    conn.send(str.encode("Connected"))

    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode("utf-8")

            if not data:
                print(addr, "Disconnected")
                break
            else:
                print("Received: ", data)

            conn.sendall(str.encode(reply))
        except:
            break

    print("Lost connection")
    conn.close()


s.listen(2)
print("The host server: " + server)
print("Waiting for a connection, Server Started")

# Display server's running status
while True:
    conn, addr = s.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn,))
