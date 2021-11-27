import urllib2
import dnsdumapi
import cms
import censho
import virustotal
import intro
import os
import subprocess as sp

def menu():
    intro.design()
    print("")
    print("Select Options")
    print("--------------------------------------------------------------------")
    print("0. FULL SCAN [1.  Ping, 2.  Dnslookup, 3.  Reverse-Dns, 4.  Whoise, 5.  Geo-Ip-Lookup , 6.  Reverse-Ip-Lookup, 7.  HTTP-Headers, 8.  Pages Links, 9.  AS-Lookup, 10. Subnet, 11. Host(Sub-Domain) Finder, 12. Port Scanner, 13. Zone Transfer, 14. Traceroute, 15. Host-Dns-Finder]")
    print("1.  Ping")
    print("2.  Dnslookup")
    print("3.  Reverse-Dns")
    print("4.  Whoise")
    print("5.  Geo-Ip-Lookup ")
    print("6.  Reverse-Ip-Lookup")
    print("7.  HTTP-Headers")
    print("8.  Pages Links")
    print("9.  AS-Lookup")
    print("10. Subnet")
    print("11. Host(Sub-Domain) Finder")
    print("12. Port Scanner")
    print("13. Zone Transfer")
    print("14. Traceroute")
    print("15. Host-Dns-Finder")
    print("16. Information Gathering with DNSDumpster API")
    print("17. Shodan Iformation Gathering")
    print("18. CMS Finder")
    print("19. Virus Total API")
    print("20. Mass subdomain DIG lookups and shortlisting by service names(helps to find subdomain takeovers)")
    print("")
    scan()

def menu1():
    print("")
    print("Select Options")
    print("--------------------------------------------------------------------")
    print("0. FULL SCAN [1.  Ping, 2.  Dnslookup, 3.  Reverse-Dns, 4.  Whoise, 5.  Geo-Ip-Lookup , 6.  Reverse-Ip-Lookup, 7.  HTTP-Headers, 8.  Pages Links, 9.  AS-Lookup, 10. Subnet, 11. Host(Sub-Domain) Finder, 12. Port Scanner, 13. Zone Transfer, 14. Traceroute, 15. Host-Dns-Finder]")
    print("1.  Ping")
    print("2.  Dnslookup")
    print("3.  Reverse-Dns")
    print("4.  Whoise")
    print("5.  Geo-Ip-Lookup ")
    print("6.  Reverse-Ip-Lookup")
    print("7.  HTTP-Headers")
    print("8.  Pages Links")
    print("9.  AS-Lookup")
    print("10. Subnet")
    print("11. Host(Sub-Domain) Finder")
    print("12. Port Scanner")
    print("13. Zone Transfer")
    print("14. Traceroute")
    print("15. Host-Dns-Finder")
    print("16. Information Gathering with DNSDumpster API")
    print("17. Shodan Iformation Gathering")
    print("18. CMS Finder")
    print("19. Virus Total API")
    print("20. Mass subdomain DIG lookups and shortlisting by service names(helps to find subdomain takeovers)")
    print("")
    scan()
    
def scan():
    try:
        choice=input("Enter Choice: ")
        if choice == 0:
            print("FULL SCAN SELECTED [enter host and Relex..]")
            domain=raw_input(' Enter IP Address :  ')
            print("[ping running]...")
            ping ="https://api.hackertarget.com/nping/?q="+domain
            ip = urllib2.urlopen(ping).read()
            print (ip)
            print("\n\n")
            print("[Dnslookup running]...")
            dns = "http://api.hackertarget.com/dnslookup/?q=" + domain
            ip = urllib2.urlopen(dns).read()
            print (ip)
            print("\n\n")
            print("[ReverseDNS running]...")
            rdns="https://api.hackertarget.com/reversedns/?q="+domain
            ip = urllib2.urlopen(rdns).read()
            print(ip)
            print("\n\n")
            print("[Whois running]...")
            whois = "http://api.hackertarget.com/whois/?q=" + domain
            ip = urllib2.urlopen(whois).read()
            print (ip)
            print("\n\n")
            print("[Geoip finder running]...")
            geo = "http://api.hackertarget.com/geoip/?q=" + domain
            ip = urllib2.urlopen(geo).read()
            print (ip)
            print("\n\n")
            print("[ReverseIp lookup running]...")
            revrse = "http://api.hackertarget.com/reverseiplookup/?q=" + domain
            ip = urllib2.urlopen(revrse).read()
            print (ip)
            print("\n\n")
            print("[Checking Http headers]...")
            hea = "http://api.hackertarget.com/httpheaders/?q=" + domain
            ip = urllib2.urlopen(hea).read()
            print (ip)
            print("\n\n")
            print("[AS-lookup running]...")
            aslookup = "http://api.hackertarget.com/aslookup/?q=" + domain
            ip = urllib2.urlopen(aslookup).read()
            print(ip)
            print("\n\n")
            print("[Pagelink finding]...")
            get = "https://api.hackertarget.com/pagelinks/?q=" + domain
            ip = urllib2.urlopen(get).read()
            print (ip)
            print("\n\n")
            print("[Subnet running]...")
            sub = "http://api.hackertarget.com/subnetcalc/?q=" + domain
            ip = urllib2.urlopen(sub).read()
            print (ip)
            print("\n\n")
            print("[Host search running]...")
            host = "http://api.hackertarget.com/hostsearch/?q=" + domain
            dns = urllib2.urlopen(host).read()
            print (dns)
            print("\n\n")
            print("[Nmap running]...")
            port = "http://api.hackertarget.com/nmap/?q=" + domain
            ip = urllib2.urlopen(port).read()
            print (ip)
            print("\n\n")
            print("[Zonetransfer running]...")
            zon = "http://api.hackertarget.com/zonetransfer/?q=" + domain
            tran = urllib2.urlopen(zon).read()
            print (tran)
            print("\n\n")
            print("[Host Dns running]...")
            fhost = "http://api.hackertarget.com/findshareddns/?q=" + domain
            dns = urllib2.urlopen(fhost).read()
            print (dns)
            print("\n\n")
            print("[Traceroute running]...")
            get = "https://api.hackertarget.com/mtr/?q=" + domain
            page = urllib2.urlopen(get).read()
            print(page)
            menu1()
        elif choice == 1:
            domain=raw_input(' Enter IP Address :  ')
            ping ="https://api.hackertarget.com/nping/?q="+domain
            ip = urllib2.urlopen(ping).read()
            print (ip)
            menu1()
        elif choice==2:
            domain=raw_input(' Enter IP Address :  ')
            dns = "http://api.hackertarget.com/dnslookup/?q=" + domain
            ip = urllib2.urlopen(dns).read()
            print (ip)
            menu1()
        elif choice==3:
            domain=raw_input(' Enter IP Address :  ')
            rdns="https://api.hackertarget.com/reversedns/?q="+domain
            ip = urllib2.urlopen(rdns).read()
            print(ip)
            menu1()
        elif choice==4:
            domain=raw_input(' Enter IP Address :  ')
            whois = "http://api.hackertarget.com/whois/?q=" + domain
            ip = urllib2.urlopen(whois).read()
            print (ip)
            menu1()
        elif choice==5:
            domain=raw_input(' Enter IP Address :  ')
            geo = "http://api.hackertarget.com/geoip/?q=" + domain
            ip = urllib2.urlopen(geo).read()
            print (ip)
            menu1()
        elif choice==6:
            domain=raw_input(' Enter IP Address :  ')
            revrse = "http://api.hackertarget.com/reverseiplookup/?q=" + domain
            ip = urllib2.urlopen(revrse).read()
            print (ip)
            menu1()
        elif choice==7:
            domain=raw_input(' Enter IP Address :  ')
            hea = "http://api.hackertarget.com/httpheaders/?q=" + domain
            ip = urllib2.urlopen(hea).read()
            print (ip)
            menu1()
        elif choice==8:
            domain=raw_input(' Enter IP Address :  ')
            get = "https://api.hackertarget.com/pagelinks/?q=" + domain
            ip = urllib2.urlopen(get).read()
            print (ip)
            menu1()
        elif choice==9:
            domain=raw_input(' Enter IP Address :  ')
            aslookup = "http://api.hackertarget.com/aslookup/?q=" + domain
            ip = urllib2.urlopen(aslookup).read()
            print (ip)
            menu1()
        elif choice==10:
            domain=raw_input(' Enter IP Address :  ')
            sub = "http://api.hackertarget.com/subnetcalc/?q=" + domain
            ip = urllib2.urlopen(sub).read()
            print (ip)
            menu1()
        elif choice==11:
            domain=raw_input(' Enter IP Address :  ')
            host = "http://api.hackertarget.com/hostsearch/?q=" + domain
            dns = urllib2.urlopen(host).read()
            print (dns)
            menu1()
        elif choice==12:
            domain=raw_input(' Enter IP Address :  ')
            port = "http://api.hackertarget.com/nmap/?q=" + domain
            ip = urllib2.urlopen(port).read()
            print (ip)
            menu1()
        elif choice==13:
            domain=raw_input(' Enter IP Address :  ')
            zon = "http://api.hackertarget.com/zonetransfer/?q=" + domain
            tran = urllib2.urlopen(zon).read()
            print (tran)
            menu1()
        elif choice==14:
            domain=raw_input(' Enter IP Address :  ')
            fhost = "http://api.hackertarget.com/findshareddns/?q=" + domain
            dns = urllib2.urlopen(fhost).read()
            print (dns)
            menu1()
        elif choice==15:
            domain=raw_input(' Enter IP Address :  ')
            get = "https://api.hackertarget.com/mtr/?q=" + domain
            page = urllib2.urlopen(get).read()
            print(page)
            menu1()
        elif choice==16:
            domain=raw_input("Enter your IP/Host: ")
            dnsdumapi.dnsscan(domain)
            print("")
            menu1()
        elif choice==17:
            ip = raw_input("Enter Your Domain Name Only: ")
            censho.shodn(ip)
            print("")
            menu1()
        elif choice==18:
            domain= raw_input("Enter Your Host/Ip: ")
            cms.cmsscan(domain)
            print("")
            menu1()
        elif choice==19:
            domain = raw_input("Enter Your Domain: ")
            virustotal.virusto(domain)
            print("")
            menu1()
        elif choice==20:
            domain = raw_input("First set hhh.txt file with subdomain list then hit enter : ")
            cmd="python3 nslookup.py"
            os.system(cmd) 
           # sp.Popen('gnome-terminal -e "'+cmd+'"', shell=True)
            print("")
            menu1()
        else:
            print("Dear Hacker Please Select b/w 1-17 Options...")
    except(KeyboardInterrupt):
        print("\nThank You...")
menu()
