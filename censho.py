import shodan
import socket
import APIS

def shodn(ip):
    api = shodan.Shodan(APIS.API_KEY)
    ip=socket.gethostbyname(ip)
    host = api.host(ip)
    print("IP: {}  \nOrganization: {}  \nOperating System: {} ".format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))
    for item in host['data']:
            print("Port: {} \nBanner: {}".format(item['port'], item['data']))

'''

for service in result['matches']:
        print "Host: "+service['http']['host']
        print "IP: "+ str(service['ip_str'])
        print "Port: "+ str(service['port'])
        print "Location: "+ str(service['location'])
        print service['data']
        print("-------------------------------------------------------------------------------")
'''
