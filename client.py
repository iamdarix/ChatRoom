import socket
import threading

HEADER = 64
PORT = 8088
FORMAT  = 'utf-8'
DISCONNECT_MSG = '!@#$%^&*()'
SERVER = 'INTERNET IP Address'
ADDR = (SERVER,PORT)

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(ADDR)



def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    if msg_length!=0:
        send_length = str(msg_length).encode(FORMAT)
        send_length+= b' '*(HEADER-len(send_length)) # b' ' means the byte for the blank space 
        # why are we doing this is said the client part
        client.send(send_length)
        client.send(message)

name = input("Enter your name. This name will be visible to everyone in the chat room     ")
name_msg = "@#$"+name
send(name_msg)


def recieve():
    while True:
        res = client.recv(2048).decode(FORMAT)
        message.insert(END, f" {res}  \n\n")

def fail_safe():
    send(DISCONNECT_MSG)
    base.destroy()

def run(nothing_important):
    msg = input_place.get()
    input_place.delete(0,END)
    if len(str(msg)) !=0:
        message.insert(END, " You: " + msg + '\n\n')
    send(msg)
        
from tkinter import *

base = Tk()
base.title('Chat room')
base.geometry("400x500")



message = Text(base,width=50)
message.grid(row=0,column=0,padx=10,pady=10)

scroll_y = Scrollbar(base,command=message.yview)
message['yscrollcommand'] = scroll_y.set

input_place = Entry(base,width=50)
input_place.grid(row=1,column=0,padx=10,pady=10)
input_place.bind('<Return>',run)

send_button = Button(base,text='Send',padx=10,pady=10,command=lambda : run(0))
send_button.grid(row=2,column=0)
scroll_y.place(x=385, y=6, height=386)
rev = threading.Thread(target=recieve)
rev.daemon=True
rev.start()

base.protocol("WM_DELETE_WINDOW",fail_safe)
base.mainloop()      
