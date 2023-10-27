import requests

import threading

import time

def make_request(self):
    print(self,"Helloc")
    r =requests.get('http://example.com/')
    # print((r.__dict__.keys()))
    print(self , r.status_code)
    
if  __name__ == "__main__":
    threads =55550;data=0
    while data < threads:
        data+=1
        threading.Thread(target=make_request,args=(threads,)).start()
        
        