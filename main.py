import json
import requests
import datetime
import sys
import xml
import re

# input station tite and return station code
def find_code(to_inp):
    code = codes_dict.get(to_inp)
    print("code = "+ code)
    return code

def sch_between_routes(api_key,api_url,to_code,from_code):

    format = 'json'
    from1 = from_code
    to = to_code
    lang = 'ru'
    date = datetime.datetime.now().strftime('%Y-%M-%d')#now.strftime("%Y-%m-%d %H:%M")
    #url = api_url_base+'apikey='+apikey+'&'+'format='+format+'&'+'from='+from1+'&'+'to='+to+'&'+'lang='+lang+'&'+'date='+date
    payload = {'apikey': api_key,'from':from1, 'to': to,  'format': format}
    print(payload)
    r = requests.get(api_url, payload)
    # print(r)
    resp = r.json()
    # print(resp)
    return resp

def req_station_codes():
    #request for station`s codes
    payload1 = {'apikey': apikey, 'format': json}
    # r1 = requests.get(api_url_base1, payload1)
    r1 = requests.get('https://api.rasp.yandex.net/v3.0/stations_list/?apikey=3d4db511-c803-4569-a638-e0babb6cbccc&lang=ru_ru&format=json')
    print(r1)
    # returns file with placw and codes
    with open('places.json', 'r') as f:
        distros_dict = json.load(f)
    doc =list()
    res_cd=dict()
    print(type(res_cd))
    for cnt in distros_dict['countries']:
        if cnt["title"]=='Россия':
            print(cnt['title'])
            for rg in cnt['regions']:
                if rg['title']=='Республика Татарстан':
                    for stl in rg['settlements']:
                        for stn in stl['stations']:
                            if (stn["title"]=='Бирюли' or stn["title"]=='Дербышки'):
                            # if stn['transport_type']=='train':
                                #print(type(stn['codes']))
                                #print((stn['codes']).values())
                                print(stn['title']+"  "+(stn['codes']).get('yandex_code'))
                                res_cd = (stn['title'],(stn['codes']).get('yandex_code'))
                                doc.append(res_cd)
    print(doc)
    with open('codes.json', 'w') as outfile:
        json.dump(doc, outfile)

#input parameters for API
apikey = '3d4db511-c803-4569-a638-e0babb6cbccc'
api_url_base = 'https://api.rasp.yandex.net/v3.0/search/'
api_url_base1 = 'https://api.rasp.yandex.net/v3.0/stations_list/'

# input data
from_inp = input("Enter from:")
to_inp = input("Enter to: ")
#  download json with codes
with open('codes.json', 'r') as c:
     codes = json.load(c)

#create dictionary with codes
codes_dict={}
for i in codes:
    codes_dict[i[0]] = i[1]

# find_code(to_inp)
# find_code(from_inp)

# sch_between_routes(apikey, api_url_base, find_code(from_inp),find_code(to_inp))
l = list()
lres = list()
l.append(sch_between_routes(apikey, api_url_base, find_code(from_inp),find_code(to_inp)))
print(l)
res = dict()
for i in l:
    for sg in i['segments']:
        #print(sg)
        res['arrival']=sg['arrival']
        res['departure']=sg['departure']
        res['duration']=sg['duration']/60
        res['title']=sg['thread'].get('short_title')
        lres.append(res)
print(lres)

        # print(sg['arrival'], sg['departure'],sg['duration']/60)
        # print(sg['thread'].get('short_title'))

        # for th in sg['thread']:
        #     print(th['short_title'])

