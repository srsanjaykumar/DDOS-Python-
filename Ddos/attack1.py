from threading import Thread 
import socket 

def make_input(s):
    s.sendall(b'1232414124124^1242350235823052934')
    


HOST='0.0.0.0'
PORT = 3333
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST , PORT))
while True:
    Thread(target=make_input,args=(s,)).start()   