__author__ = 'lukasz'


import requests, json

weather_for_london =  json.loads(requests.get(
        'http://api.openweathermap.org/data/2.5/weather?q=London?id=524901&APPID=f5965238859871241783cd758d4c02f7').text)
print (weather_for_london)