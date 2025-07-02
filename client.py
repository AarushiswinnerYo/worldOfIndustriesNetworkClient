import os
import socket
HEADER=64
PORT=5555
SERVER="192.168.29.178"
ADDR=(SERVER, PORT)
FORMAT='utf-8'
DISCONNECT_MSG="!disconnect"
loggedin=False
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def main(msg):
    def send(msg):
        global loggedin
        global s
        if msg=="!connect":
            client.connect(ADDR)
            return
        elif msg==DISCONNECT_MSG:
            client.close()
        else:
            message=msg.encode(FORMAT)
            msg_length=len(message)
            send_length=str(msg_length).encode(FORMAT)
            send_length+=b' '*(HEADER - len(send_length))
            client.send(send_length)
            client.send(message)
            f=client.recv(8192).decode(FORMAT)
            if f=="User signed up successfully":
                print("Signed up!")
                if os.path.isdir("userprofs"):
                    os.chdir("userprofs")
                    with open(f"{s}.prof", "w") as w:
                        w.write("")
                else:
                    os.mkdir("userprofs")
                    os.chdir("userprofs")
                    with open(f"{s}.prof", "w") as w:
                        w.write("")
                send(f"user-{s}")
            elif f=="Successfully logged in!":
                loggedin=True
                s=s[0]
                send(f"user-{s}")
            elif f=="Non-existent":
                quit()
            elif f=="Incorrect password":
                quit()
            else:
                print(f)
                return f
    return send(msg=msg)