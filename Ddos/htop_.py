from threading import Thread 
from os import system

def make_attack(data):
    while True:
        print("From {} ".format(data))
    # system("htop")

i=0
while i<10 : 
    Thread(target=make_attack , args=(i,)).start()
    i=i+1