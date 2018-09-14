import json
import requests
import datetime
import sys
import xml
import re


apikey = '3d4db511-c803-4569-a638-e0babb6cbccc'
api_url_base = 'https://api.rasp.yandex.net/v3.0/search/'
api_url_base1 = 'https://api.rasp.yandex.net/v3.0/stations_list/'

format = 'json'
from1 = 's9612422'
to = 's9612418'
lang = 'ru'
date = datetime.datetime.now().strftime('%Y-%M-%d')#now.strftime("%Y-%m-%d %H:%M")
#url = api_url_base+'apikey='+apikey+'&'+'format='+format+'&'+'from='+from1+'&'+'to='+to+'&'+'lang='+lang+'&'+'date='+date
payload = {'apikey': apikey,'from':from1, 'to': to,  'format': format}
print(payload)

# input data
from_inp = input("Enter from:")
to_inp = input("Enter to: ")
#  download json with codes
with open('codes.json', 'r') as c:
     codes = json.load(c)
print(type(codes))
print(codes)
codes_dict={}
for i in codes:
    #codes_dict.fromkeys(i[0]:i[1])
    codes_dict.fromkeys(i[0],i[1])
    # print(i[0])
    # print(i[1])
mydict= {k: v for k, v in  codes[0][0]}
print(mydict.values())
print(type(codes_dict))
print(codes_dict.get('Уруссу'))
    # for v,k in i:
    #     print("V"+v+"  "+ "k"+k)
# codes_dict = dict()
# codes_dict[codes[0][0]:codes[0][1]]
# print(codes_dict)
r = requests.get(api_url_base, payload)
print(r)
resp = r.json()
print(resp)
#with open('data.json', 'w') as outfile:
#    json.dump(resp, outfile)

# request for station`s codes
# payload1 = {'apikey': apikey, 'format': json}
# # r1 = requests.get(api_url_base1, payload1)
# r1 = requests.get('https://api.rasp.yandex.net/v3.0/stations_list/?apikey=3d4db511-c803-4569-a638-e0babb6cbccc&lang=ru_ru&format=json')
# print(r1)
# # returns file with placw and codes
# with open('places.json', 'r') as f:
#     distros_dict = json.load(f)
# doc =list()
# res_cd=dict()
# print(type(res_cd))
# for cnt in distros_dict['countries']:
#     if cnt["title"]=='Россия':
#         print(cnt['title'])
#         for rg in cnt['regions']:
#             if rg['title']=='Республика Татарстан':
#                 for stl in rg['settlements']:
#                     for stn in stl['stations']:
#                         if (stn["title"]=='Бирюли' or stn["title"]=='Дербышки'):
#                         # if stn['transport_type']=='train':
#                             #print(type(stn['codes']))
#                             #print((stn['codes']).values())
#                             print(stn['title']+"  "+(stn['codes']).get('yandex_code'))
#                             res_cd = (stn['title'],(stn['codes']).get('yandex_code'))
#                             doc.append(res_cd)
# print(doc)
# with open('codes.json', 'w') as outfile:
#     json.dump(doc, outfile)
