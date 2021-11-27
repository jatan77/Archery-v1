import requests
import APIS

def cmsscan(domain):    
    response = requests.get("https://whatcms.org/APIEndpoint?key="+APIS.key+"&url="+domain)
    print "CMS Version: ",response.json()['result']['name'],response.json()['result']['version']
    print "Confidence of Scan: ",response.json()['result']['confidence']
    print "Status Code: ",response.json()['result']['code']
    print "Message: ",response.json()['result']['msg']



'''def google():
    test = "inurl:booking"
    reques = requests.get('https://www.googleapis.com/customsearch/v1?key=AIzaSyBu-9mkNYOFcX5scpKGRSpcgFL2zfD7AVs&cx=007953737740295957326:-jtgz281jge&q=inurl:skypicker.com '+test)
    print(reques).json()['items']
google()'''
