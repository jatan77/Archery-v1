import socket
print(socket.gethostbyname('bpccs.org')


'''[from googleapiclient.discovery import build
import pprint
my_api_key = "AIzaSyBu-9mkNYOFcX5scpKGRSpcgFL2zfD7AVs"
my_cse_id = "007953737740295957326:-jtgz281jge"
search_term="site:skypicker.com inurl:api"
def google_search(search_term, my_api_key, my_cse_id):
    service = build("customsearch", "v1", developerKey=my_api_key)
    res = service.cse().list(q=search_term, cx=cse_id).execute()
    return res['items']

results = google_search()

for result in results:
    pprint.pprint(result)

    title = result['title']
    link = result['formattedUrl']
    #dis = result['snippet']
    print (title)
    print (link)
    #print (dis)
]'''
