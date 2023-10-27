import socket as s 
from threading import Thread 
# HOST = 'localhost' # get incomming connection in localhost only 

HOST = '0.0.0.0' # get incomming connection to any where 

PORT = 5001

soc = s.socket(s.AF_INET , s.SOCK_STREAM)

soc.setsockopt(s.SOL_SOCKET , s.SO_REUSEADDR , 1)

soc.bind((HOST,PORT))

soc.listen()

res = """ HTTP


<!doctype html>
<html>
<head>
    <title>Example Domain</title>

    <meta charset="utf-8" />
    <meta http-equiv="Content-type" content="text/html; charset=utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <style type="text/css">
    body {
        background-color: #f0f0f2;
        margin: 0;
        padding: 0;
        font-family: -apple-system, system-ui, BlinkMacSystemFont, "Segoe UI", "Open Sans", "Helvetica Neue", Helvetica, Arial, sans-serif;
        
    }
    div {
        width: 600px;
        margin: 5em auto;
        padding: 2em;
        background-color: #fdfdff;
        border-radius: 0.5em;
        box-shadow: 2px 3px 7px 2px rgba(0,0,0,0.02);
    }
    a:link, a:visited {
        color: #38488f;
        text-decoration: none;
    }
    @media (max-width: 700px) {
        div {
            margin: 0 auto;
            width: auto;
        }
    }
    </style>    
</head>

<body>
<div>
    <h1>Example Domain</h1>
    <p>This domain is for use in illustrative examples in documents. You may use this
    domain in literature without prior coordination or asking for permission.</p>
    <p><a href="https://www.iana.org/domains/example">More information...</a></p>
</div>
</body>
</html>


"""

class Connection(Thread):
    def __init__(self , conn , addr ):
        Thread.__init__(self)
        self.conn = conn 
        self.addr = addr
    
    def run(self):
        self.conn.sendall(res.encode('utf-8'))
        # self.conn.sendall(b"Welcome To Chat Room for Jobless Fellows \n")
        
        # data = conn.recv(2048)
        # while data:
        #     print("{}".format(self.addr[0]) + data.decode(),end="")
        #     data = conn.recv(2048)
            
    
    
while True:
    conn , addr = soc.accept()
    Connection(conn , addr).start()
    # print("Connection received from {} : {} ".format(addr[0], addr[1]))
    # conn.sendall(b"Welcome To Chat Room for Jobless Fellows ")
    # data = conn.recv(1024)
    # while data : 
    #     print(data.decode() , end=" ")
    #     data = conn.recv(1024)    


# HTTP /1.1 200 OK 
# Content-Type: text/html; charset=UTF-8
# Etag: "3147526947"
# Accept-Ranges: bytes
# Server: ECS (nyb/1D07)
# X-Cache: HIT