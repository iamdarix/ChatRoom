import socket
import threading

HEADER = 64
PORT = 8088
# SERVER = '192.168.1.2' or use
SERVER = socket.gethostbyname(socket.gethostname())
ADDR = (SERVER,PORT)
FORMAT  = 'utf-8'
DISCONNECT_MSG = '!@#$%^&*()'
# print(SERVER,socket.gethostname())
# AF_INET determines the type of socket
server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind(ADDR)

def handle_client(conn,addr):
    print(f"[NEW CONNECTION ADDED] {addr}  joined!")
    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT) # recv = recieved
        ''' here we have given the header as 64 bytes so for example we will send the message
        "hello" which is of 6 bytes length si we send "6     " of 64 bytes length to tell 
        the server the length of the message comming next
        then we send the next messsage'''
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                msg = 'I have diconnected'
                connected = False
            elif msg.startswith("@#$"):
                names.update({conn:msg[3:]})
                print(f"[NEW NAME ADDED] {names}")
                continue
            l = len(msg)
            print(f"[{addr}] {msg} {l}")
            #conn.send("Got your message!".encode(FORMAT))
            for x in active_clients:
                if x!=conn:
                    l = len(msg)
                    m = f'{names[conn]} : {msg}'
                    x.send(m.encode(FORMAT))

    active_clients.remove(conn)
    print(f"[DISCONNECTED] {conn} disconnected")
    print(f"[ACTIVE_CLIENTS] {active_clients}")
    conn.close()


active_clients = []
names = {}

def start():
    server.listen()
    print(f'[LISTENING] Server is listening at {SERVER}')
    while True:
        conn,addr = server.accept()
        active_clients.append(conn)
        thread = threading.Thread(target=handle_client,args=(conn,addr))
        thread.start()
        print("[ACTIVE CONNECTIONS]  "+ str(threading.active_count()-1))

print("[STARTING] server is starting. Please wait ....")
start()

