import os
import socket
HEADER=64
PORT=18931
SERVER="autorack.proxy.rlwy.net"
ADDR=(SERVER, PORT)
FORMAT='utf-8'
DISCONNECT_MSG="!disconnect"
loggedin=False
client=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    global loggedin
    global s
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

if os.path.isdir("./userprofs"):
    global s
    profiles=[]
    for r in os.listdir("./userprofs"):
        if r.endswith(".prof"):
            profiles.append(r)
        for i in profiles:
            print(f"{profiles.index(i)+1}. {i}")
        sno=int(input("Choose user:- "))
        p=input("Enter Password:- ")
        sf=profiles[sno-1]
        s=sf.split(".")
        send(f"login-{s[0]}-{p}")
    else:
        if not loggedin:
            print("Fail 1")
            s=input("Enter username to signup:- ")
            p=input("Enter password:- ")
            send(f"signup-{s}-{p}")
else:
    if not loggedin:
        s=input("Enter username to signup:- ")
        p=input("Enter password:- ")
        send(f"signup-{s}-{p}")  
while True:
    i=input("Enter A text: ")
    send(i)
    if i==DISCONNECT_MSG:
        break
