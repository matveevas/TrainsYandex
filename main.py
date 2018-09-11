import json
import requests
import datetime
import sys
import xml


apikey = '3d4db511-c803-4569-a638-e0babb6cbccc'
api_url_base = 'https://api.rasp.yandex.net/v3.0/search/'
api_url_base1 = 'https://api.rasp.yandex.net/v3.0/stations_list/'

format = 'json'
from1 = 's9600396'
to = 's9600213'
lang = 'ru'
date = datetime.datetime.now().strftime('%Y-%M-%d')#now.strftime("%Y-%m-%d %H:%M")
#url = api_url_base+'apikey='+apikey+'&'+'format='+format+'&'+'from='+from1+'&'+'to='+to+'&'+'lang='+lang+'&'+'date='+date
payload = {'apikey': apikey,'from':from1, 'to': to,  'format': format}
print(payload)
r = requests.get(api_url_base, payload)
print(r)
resp = r.json()
# print(resp)
#with open('data.json', 'w') as outfile:
#    json.dump(resp, outfile)

payload1 = {'apikey': apikey, 'format': json}
# r1 = requests.get(api_url_base1, payload1)
r1 = requests.get('https://api.rasp.yandex.net/v3.0/stations_list/?apikey=3d4db511-c803-4569-a638-e0babb6cbccc&lang=ru_ru&format=json')
r1.encoding = 'utf-8'

print(r1)
resp1 = r1.json()
b=b'\u0421\u0443\u0440\u0430\u043c\u0438'
b1 = b.decode('utf-8')
print(b1)

# resp1 = r1.json()
# resp1.text
# print(resp1)
# with open('places.json', 'w') as outfile:
#     json.dump(resp1, outfile)

#'date': date,
#'https://api.rasp.yandex.net/v3.0/search/?apikey={ключ}&format=json&from=c146&to=c213&lang=ru&page=1&date=2015-09-02'