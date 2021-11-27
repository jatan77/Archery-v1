import json
import requests
import APIS
def virusto(domain):
    url ="https://www.virustotal.com/vtapi/v2/domain/report?apikey="+APIS.apikey+"&domain="+domain
    #ip = urllib2.urlopen(url).read()
    response = requests.get(url)
    #print(response.json()['whois'])
    print "\n"+"------------------------------------------------------------------------"
    print "Subdomain: "
    for i in response.json()['subdomains']:
        print i
