import os
import socket
HEADER=64
PORT=5555
SERVER="192.168.29.178"
ADDR=(SERVER, PORT)
FORMAT='utf-8'
DISCONNECT_MSG="!disconnect"
loggedin=False

def main(msg):
    def send(msg):
        global loggedin
        global s
        global client
        if msg=="!connect":
            client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            client.connect(ADDR)
            return
        elif msg==DISCONNECT_MSG:
            client.close()
            print("Disconnected")
        else:
            message=msg.encode(FORMAT)
            msg_length=len(message)
            send_length=str(msg_length).encode(FORMAT)
            send_length+=b' '*(HEADER - len(send_length))
            client.send(send_length)
            client.send(message)
            f=client.recv(10000).decode(FORMAT)
            return f
    return send(msg=msg)