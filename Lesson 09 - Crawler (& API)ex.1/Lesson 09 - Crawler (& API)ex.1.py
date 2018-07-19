import requests
import json

url='https://www.metaweather.com/api/location/search/?query=taipei'
r=requests.get(url)
r.encoding='utf-8'
data=json.loads(r.text)
woeid=data[0]['woeid']

location='https://www.metaweather.com/api/location/'+str(woeid)+'/'
r=requests.get(location)
r.encoding='utf-8'
data=json.loads(r.text)
weather=data['consolidated_weather'][0]['weather_state_name']
print(weather)