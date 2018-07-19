import requests
import json


url = 'https://cloud.culture.tw/frontsite/trans/SearchShowAction.do?method=doFindTypeJ&category=5'

r=requests.get(url)
response = (r.json())

with open('music_show.json','w',encoding='utf-8-sig') as f:
    json.dump(response,f)

with open('music_show.json','r',encoding='utf-8-sig') as f:
    music=json.loads(f.read())
    n=len(music)
    n1=n-1
    print(n)
    with open('music_show.text','w',encoding='utf-8-sig') as fw:
        for i in range(0,n1):
            title=music[i]['title']
            startDate=music[i]['startDate']
            endDate=music[i]['endDate']
            fw.write(title)
            fw.write(':')
            fw.write(startDate)
            fw.write('~')
            fw.write(endDate)
            fw.write('\n')
