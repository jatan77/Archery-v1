import  urllib2
import dnsdumapi
import censho
import cms
import virustotal
import intro

Ips=["https://api.hackertarget.com/nping/?q=","https://api.hackertarget.com/dnslookup/?q=","https://api.hackertarget.com/reversedns/?q=",
     "https://api.hackertarget.com/whois/?q=","https://api.hackertarget.com/geoip/?q=","https://api.hackertarget.com/reverseiplookup/?q=",
     "https://api.hackertarget.com/httpheaders/?q=","https://api.hackertarget.com/pagelinks/?q=","https://api.hackertarget.com/aslookup/?q=",
     "https://api.hackertarget.com/subnetcalc/?q=","https://api.hackertarget.com/hostsearch/?q=","https://api.hackertarget.com/nmap/?q=",
     "https://api.hackertarget.com/zonetransfer/?q=","https://api.hackertarget.com/findshareddns/?q=","https://api.hackertarget.com/mtr/?q="]
lables=["Ping","Dnslookup","Reverse-Dns","Whoise","Geo-Ip-Lookup","Reverse-Ip-Lookup","HTTP-Headers","Pages Links","AS-Lookup","Subnet","Host(Sub-Domain) Finding",
        "Port Scanning","Zone Transfer","Traceroute","Host-Dns-Finding"]
adlables=["Dns Scanning via DNSDumpster","Shodan Searching","CMS Findind"]

#It Scan all Options
def fscan():
    try:
        intro.design()
        print("Full Scan Mode...")
        print("----------------------------------------------------------")
        domain = raw_input("Enter Your Domain: ")
        print("----------------------------------------------------------")
        j = 0
        for i in Ips:
            print lables[j]
            ip = urllib2.urlopen(i+domain).read()
            print ip+""
            print("------------------------------------------------------")
            j= j+1
#It scan DNSDumpster,Shodan & CMS
        print adlables[0]
        dnsdumapi.dnsscan(domain)
        print("")
        print adlables[1]
        censho.shodn(domain)
        print("")
        print adlables[2]
        cms.cmsscan(domain)
        print("")
        virustotal.virusto(domain)
        print("")
    except(KeyboardInterrupt):
        print("\nThank You...")

fscan()
