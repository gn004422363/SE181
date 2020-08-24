"""
    This server handling all of the players, it save
    and send server's status to each player.
"""

import socket
from _thread import *
import chessboard
import sys
sys.path.insert(0, "./SE181_pieces")
import SE181_samplemain
import pickle


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
    print(str(e))

def threaded_client(conn):
    conn.send(str.encode("Connected"))
    board = SE181_samplemain.board
    while True:
        try:
            data = conn.recv(2048 * 8)

            reply = pickle.dumps(board)

            if not data:
                print(addr, "Disconnected")
                break
            else:
                print("Received: ", data)
                print("Sending : ", reply)

            conn.sendall(reply)
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
