import os , subprocess , threading , keyboard , time
import concurrent , requests
from concurrent import futures
from colorama import Fore , init
init()
G = Fore.LIGHTGREEN_EX  # Defining colors
R = Fore.LIGHTRED_EX
Cyn = Fore.LIGHTCYAN_EX
Ylw = Fore.LIGHTYELLOW_EX

banner = """
 █   ▄▀█ █▄ █   █ █▀█   █▀ █▀▀ ▄▀█ █▄ █ █▄ █ █▀▀ █▀█
 █▄▄ █▀█ █ ▀█   █ █▀▀   ▄█ █▄▄ █▀█ █ ▀█ █ ▀█ ██▄ █▀▄
------------------- [+] GHOSTH4CK3R ------------------
 """
def print_banner():
    print(Cyn + banner)

print_banner()

input("Press \'Enter\' To Scan > ")

def anim() :                # Scanning animation
    os.system('cls')
    print_banner()
    print("\nScanning.../ ")
    time.sleep(0.1)
    os.system('cls')
    print_banner()
    print("\nScanning...- ")
    time.sleep(0.1)
    os.system('cls')
    print_banner()
    print("\nScanning...\ ")
    time.sleep(0.1)
    os.system('cls')
    print_banner()
    print("\nScanning...| ")
    time.sleep(0.1)
    os.system('cls')

def anim2() :
    print_banner()
    print("Scan complete...")

def ping_range(start,count) :


    prefix = "192.168.1."
    condition = "Destination host unreachable" 
    condition2 = "Request timed out"
    list1 = []
    #list2 = []

    for xxx in range(start,start+count) :
        
        if keyboard.is_pressed('space') == True :
            exit()
        ip = prefix + str(xxx)
        code = "ping " + ip + " -n 1 -l 1"    
        code2 = "arp -a " + ip
        ping = os.popen(code).read()            
       
        if condition not in ping and condition2 not in ping:  # Checking if IP's are alive
            #print(G + ip)               
            #list1.append(ip)
            try:
                arp = os.popen(code2).read().split('\n')  # Getting MAC Address
                arpS = str(arp[3])
                mac_loc = arpS.find('-')
                mac = arpS[(mac_loc-2):(mac_loc+15)]

                macsite_url = "https://macvendors.com/query/" + mac
                vendor_res = requests.get(macsite_url)   # Getting MAC Vendor

                if vendor_res.status_code == 200 :
                    vendor = vendor_res.text
                else:
                    vendor = "[Not Found]"

                IPnMACnVendor = ip + "  " + mac + "  " + vendor
                list1.append(IPnMACnVendor)
            
            except Exception as e :             # If error occurs
                IPnNon = ip + "  [Not Found]"
                list1.append(IPnNon)

    return list1 


tasks = []

with concurrent.futures.ThreadPoolExecutor(max_workers=30) as executor :  # Multi Threading
    for start in [0,11]:
        tasks.append(executor.submit(ping_range,start,10))
        
    for start in [21,31]:
        tasks.append(executor.submit(ping_range,start,10))
        
    for start in [41,51]:
        tasks.append(executor.submit(ping_range,start,10))
        
    for start in [61,71]:
        tasks.append(executor.submit(ping_range,start,10))
        
    for start in [81,91]:
        tasks.append(executor.submit(ping_range,start,10))
        
    for start in [101,111]:
        tasks.append(executor.submit(ping_range,start,10))
        
    for start in [121,131]:
        tasks.append(executor.submit(ping_range,start,10))
        #GH0STH4CK3R
    for start in [141,151]:
        tasks.append(executor.submit(ping_range,start,10))
        
    for start in [161,171]:
        tasks.append(executor.submit(ping_range,start,10))
        
    for start in [181,191]:
        tasks.append(executor.submit(ping_range,start,10))

    for start in [201,211]:
        tasks.append(executor.submit(ping_range,start,10))

    for start in [221,231]:
        tasks.append(executor.submit(ping_range,start,10))

    for start in [241,248]:
        tasks.append(executor.submit(ping_range,start,7))
        for v in range(40):
            anim()
        
anim2()    

print(Cyn + "\nResults :")
print(G + "")

empty_tsk = 0

for task in tasks:  # Outputting Returned Values From each thread
    if len(task.result()) == 1 :  
        print(task.result()[0])
    elif len(task.result()) > 1 :
        for elmnt in range(len(task.result())) :
            print(task.result()[elmnt])
    elif len(task.result()) == 0 :
        empty_tsk += 1

if empty_tsk >= 254 :
    print(R + "No IP's Found !")
    
print(Cyn + "")    
input("Exit >>")
