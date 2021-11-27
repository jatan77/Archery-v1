import socket
import re,sys
from dnsdumpster.DNSDumpsterAPI import DNSDumpsterAPI
import urllib2


'''def conn():
    sokt= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    a=sokt.connect(('www.google.com',443))
    sokt.send('hello')
    data = sokt.recv(102400)
    print(data)'''

def dnsscan(domain):
    try:
        print"Domain"
        print"---------------------------------------------"
        print domain
        results = DNSDumpsterAPI().search(domain)
        print"\n\n"
        print"DNS server"
        print"---------------------------------------------"
        for dns in results['dns_records']['dns']:
            print(dns)
        print"\n\n"
        print"MX Records"
        print"---------------------------------------------"
        for mx in results['dns_records']['mx']:
            print(mx)
        print"\n\n"
        print"Sub Domain"
        print"---------------------------------------------"
        for subdomain in results['dns_records']['host']:
            print(subdomain)
        print"\n\n"
        print"TXT Records"
        print"---------------------------------------------"
        for txt in results['dns_records']['txt']:
            print(txt)
    except(KeyboardInterrupt):
            print("Some Things is Wrong")
