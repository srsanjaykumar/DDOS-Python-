from subprocess import PIPE , STDOUT , Popen 
from threading import Thread
import socket    
def  ProcessThreading(p):
      while p.poll() is None:
          print(p.stdout.readline().decode().strip())

# in this place PIPE is  a programmable One     
p = Popen(['bc' , '-q'] , stdin=PIPE , stdout=PIPE , stderr = STDOUT)


while p.poll() is None:
    inp = input("")
    inp = inp + "\n"
    p.stdin.write(inp.encode())
    p.stdin.flush()
    
    
HOST ='0.0.0.0'  
PORT = 3333
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR ,1 )
s.bind((HOST,PORT))
s.listen()

while True : 
    conn , addr = s.accept()
    Thread(target=ProcessThreading, args=(p,)).start()
