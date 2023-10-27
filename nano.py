from threading import Thread 


class sample(Thread):
    def __init__(self, pname , pid ):
        Thread.__init__(self)
        self.pname = pname
        self.pid = pid 
    
    def run(self):
        print("Running")
        print("Pname : ", self.pname)
        print('Pid : ', self.pid)
        
        
        
data = sample("VsCode ","2345")
data.start()
    
    
