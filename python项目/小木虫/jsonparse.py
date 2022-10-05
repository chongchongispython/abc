import csv
import json
from jsonpath import jsonpath
def makejson(name):
    csvfile=open('baidutieba.csv','a',newline='',encoding='utf-8')
    writer=csv.writer(csvfile)
    file=open(f'{name}.dat', mode='r',encoding='utf-16')
    for line in file.readlines():
        if line.strip()!='':
            data= json.loads(line.strip())
            try:
                for body in jsonpath(data,'$..thread_list')[0]:
                    tile=jsonpath(body,'$..title')
                    text=jsonpath(body,'$..text')
                    if len(tile)>0:
                        tile=tile[0]
                    else:
                        tile=''
                    if len(text) > 0:
                        text = text[0]
                    else:
                        text = ''
                    if tile and text:
                        writer.writerow([tile,text])
                        print(tile,text)
                        csvfile.flush()
            except:
                pass


if __name__ == '__main__':
    name='baidutieba'
    makejson(name)