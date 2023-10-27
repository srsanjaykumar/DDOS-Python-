import sys

def pr():
    for i in range(100):
        if i %2 ==0 :
            print(i,file=sys.stderr)
        else : 
            print(i)
        if i==50 : 
            raise Exception("Reached 50 ")
        
try:
    pr()
except Exception as e :
    print(e)