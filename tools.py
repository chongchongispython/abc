import json

import requests
def getprovs():
    with open('area.json','r') as file:
        areadict=json.load(file)
    provs=[]
    for prov in areadict['province']:
        provs.append(prov['name'])

    return provs

def getcitys(text):
    with open('area.json','r') as file:
        areadict=json.load(file)
    areadict['province']
    citys=[]
    for prov in areadict['province']:
        if text==prov['name']:
            for city in prov['city']:
                citys.append(city['name'])
            break

    return citys