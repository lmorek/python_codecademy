__author__ = 'lukasz'


import requests, json


weather_for_london =  json.loads(requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=Wroclaw?pl=524901&APPID=f5965238859871241783cd758d4c02f7').text)
pogoda= (weather_for_london[u'main'][u'temp'])-272
print (pogoda)


url = 'http://api.openweathermap.org/data/2.5/weather?q='
define_city = ["Wroclaw", "Warsaw","Poznan"]
api_id = '=524901&APPID=f5965238859871241783cd758d4c02f7'
for item in range(len(define_city)):
        create_url=url+define_city[item]+api_id
        weather_for_london = json.loads(requests.get(create_url).text)
        pogoda= (weather_for_london[u'main'][u'temp'])-272
        print pogoda


