import subprocess as sp
from threading import Thread
from queue import Queue
import http.client, sys
import requests
from colorama import Fore, Back, Style
import os
import time

from time import sleep

def progress(percent=0, width=30):
    hashes = width * percent // 100
    blanks = width - hashes

    print('\r', f' Total Scaned domain count : {percent:.0f} :=', sep='',
        end='', flush=True)

print('This will take a moment')

print()

concurrent = 50

def doWork():
    while True:
        url = q.get()
        cmd="dig -t A "+url+""
        output = sp.getoutput(cmd)
        if "cloudapp.azure.com" in output:
            print("[cloudapp.azure.com]: Found in Url Dig of : "+url)
            file = open('ns-out/azurecloudapp-lookups.txt','a') 
            file.write(url+"------------->\n") 
            file.write(output+"\n") 
            file.write("*********************************\n")
            file.close()
            file = open('ns-out/azurecloudapp-lookups-url.txt','a') 
            file.write(url) 
            file.close()
        if "azurewebsites.net" in output:
            print("[azurewebsites.net]: Found in Url Dig of : "+url)
            file = open('ns-out/azurewebsites-lookups.txt','a') 
            file.write(url+"------------->\n") 
            file.write(output+"\n") 
            file.write("*********************************\n")
            file.close()
            file = open('ns-out/azurewebsites-lookups-url.txt','a') 
            file.write(url) 
            file.close()
        if "trafficmanager.net" in output:
            print("[trafficmanager.net]: Found in Url Dig of : "+url)
            file = open('ns-out/trafficmanager-lookups.txt','a') 
            file.write(url+"------------->\n") 
            file.write(output+"\n") 
            file.write("*********************************\n")
            file.close()
            file = open('ns-out/trafficmanager-lookups-url.txt','a') 
            file.write(url) 
            file.close()
        if "cloudapp.net" in output:
            print("[cloudapp.net]: Found in Url Dig of : "+url)
            file = open('ns-out/cloudapp-lookups.txt','a') 
            file.write(url+"------------->\n") 
            file.write(output+"\n") 
            file.write("*********************************\n")
            file.close()
            file = open('ns-out/cloudapp-lookups-url.txt','a') 
            file.write(url) 
            file.close()
        if "amazonaws.com" in output:
            print("[amazonaws.com]: Found in Url Dig of : "+url)
            file = open('ns-out/amazonaws-lookups.txt','a') 
            file.write(url+"------------->\n") 
            file.write(output+"\n") 
            file.write("*********************************\n")
            file.close()
            file = open('ns-out/amazonaws-lookups-all-url.txt','a') 
            file.write(url) 
            file.close()
        if "fastly.net" in output:
            print("[fastly.com]: Found in Url Dig of : "+url)
            file = open('ns-out/fastly-lookups.txt','a') 
            file.write(url+"------------->\n") 
            file.write(output+"\n") 
            file.write("*********************************\n")
            file.close()
            file = open('ns-out/fastly-lookups-all-url.txt','a') 
            file.write(url) 
            file.close()
        if "s3-website" in output:
            print("[s3-website ]: Found in Url Dig of : "+url)
            file = open('ns-out/s3-website-lookups.txt','a') 
            file.write(url+"------------->\n") 
            file.write(output+"\n") 
            file.write("*********************************\n")
            file.close()
            file = open('ns-out/s3-website-lookups-all-url.txt','a') 
            file.write(url) 
            file.close()
        if "herokudns.com" in output:
            print("[herokudns ]: Found in Url Dig of : "+url)
            file = open('ns-out/herokudns-lookups.txt','a') 
            file.write(url+"------------->\n") 
            file.write(output+"\n") 
            file.write("*********************************\n")
            file.close()
            file = open('ns-out/herokudns-lookups-all-url.txt','a') 
            file.write(url) 
            file.close()
        if "NXDOMAIN" in output:
            if "CNAME" in output:
                file = open('ns-out/NXDOMAIN-lookups.txt','a') 
                file.write(url+"------------->\n") 
                file.write(output+"\n") 
                file.write("*********************************\n")
                file.close()
                file = open('ns-out/NXDOMAIN-lookups-all-url.txt','a') 
                file.write(url) 
                file.close()
        if "CNAME" in output:
            file = open('ns-out/all-dig-lookups.txt','a') 
            file.write(url+"------------->\n") 
            file.write(output+"\n") 
            file.write("*********************************\n")
            file.close()
        cmd1="nslookup "+url+""
        output1 = sp.getoutput(cmd1)
        if "canonical name" in output1:
            file = open('ns-out/nslookup-entrys.txt','a') 
            file.write(url+"------------->\n") 
            file.write(output1+"\n") 
            file.write("*********************************\n")
            file.close()
        q.task_done()

q = Queue(concurrent * 2)
for i in range(concurrent):
    t = Thread(target=doWork)
    t.daemon = True
    t.start()
try:
    la=1
    with open("hhh.txt") as f:
        for line in f:
            progress(la)
            la+=1
            q.put(line)
    q.join()
except KeyboardInterrupt:
    sys.exit(1)
