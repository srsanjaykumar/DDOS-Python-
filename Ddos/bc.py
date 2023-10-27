from subprocess import PIPE , STDOUT , Popen 

from threading import Thread
import socket , time
# Full Duplex 
class ProcessThreading(Thread):
    def __init__(self, p, c ,a):
        Thread.__init__(self)
        self.p = p
        self.c = c
        self.a = a 
        
    def run(self):
        try:
            while self.p.poll() is None:
                self.c.sendall(self.p.stdout.readline())
        except: 
            print("Connection reset for {} ".format(self.a[0]))
            con.remove(self.addr[0])
                   
        
class MathServer(Thread):
    def __init__(self, conn , addr ):
        Thread.__init__(self)
        self.conn = conn 
        self.addr = addr 
        
    def run(self):   
        # in this place PIPE is  a programmable One   
        
        # APPLICATION LAYER =>  we can hack it in application layer by passing some  certain inputs 
        p = Popen(['bc' , '-q'] , stdin=PIPE , stdout=PIPE , stderr = STDOUT)
        out_t = ProcessThreading(p, self.conn,self.addr)
        out_t.start()
        while p.poll() is None:
            try:
                self.conn.settimeout(5)
                #  PRESENTATION LAYER =>  here we encode to send data and decode the received data  and formatting the data  
                inp = self.conn.recv(1024)
                inp = inp.decode().strip()
                if not inp : 
                    break 
                elif inp == 'exit' or  inp == 'quit':
                    p.kill()    
                    self.conn.close()
                    break 
                p.stdin.write(inp.encode() +b"\n")
                p.stdin.flush()
            except:
                p.kill()    
                self.conn.close()
                con.remove(self.addr[0])
    
    
    

# SESSION LAYER  => because here we filtering and validating ip address that will be allow or not for the server 
HOST ='0.0.0.0'  
PORT = 3333
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR ,1 )
s.bind((HOST,PORT))
s.listen()
con=[]
while True : 
    conn , addr = s.accept()
    if addr[0] in con:
        print("Connection rejected  :{} {} ".format(addr[0] , addr[1]))
       # conn.close()
    else:
        # con.append(addr[0])
        print("Connection from : {} {} ".format(addr[0] , addr[1]))
        MathServer(conn ,addr).start()
