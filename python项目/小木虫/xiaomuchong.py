# encoding=gbk
import csv
import random
import time
import requests
import re
from lxml import etree
class XiaoMuChong(object):
    headers={
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': 'acw_tc=276082a716368121761425519e298b8055da0e68da75994d1dcaa52582c485; Hm_lvt_2207ecfb7b2633a3bc5c4968feb58569=1636812176; _ga=GA1.2.993140784.1636812182; _gat=1; _discuz_uid=27647705; _discuz_pw=03e8eedcc53d9c1e; last_ip=27.46.21.27_27647705; discuz_tpl=qing; _emuch_index=1; _discuz_cc=62361061866383282; view_tid=14828650; Hm_lpvt_2207ecfb7b2633a3bc5c4968feb58569=1636812388',
        'Host': 'muchong.com',
        'Referer': 'http://muchong.com/bbs/search.php?wd=%D6%B1%B2%A9&fid=198&search_type=&adfilter=0&page=2',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.159 Safari/537.36' ,
    }
    url=''
    detailurls=[]
    temp=0
    def __init__(self):
        self.csvwriter=csv.writer(open('dataxx.csv', 'a',encoding='gbk'))
    def getpage(self,page):
        self.url='http://muchong.com/bbs/search.php?wd=%D6%B1%B2%A9&fid=198&search_type=&adfilter=0&page={}'.format(page)
        response=requests.get(self.url,headers=self.headers)
        body=response.content.decode(encoding='gbk')
        hrefs=re.findall('<a href="(http://muchong.com/.*?)" target="_blank">',body)[:-1]
        print(hrefs)
        self.detailurls.extend(hrefs)
    def gettext(self,detailurl):
        time.sleep(random.randrange(0,2))
        try:
            response = requests.get(url=detailurl, headers=self.headers)
            body = response.content.decode(encoding='gbk')
            if 'Please contact QQ : 2862490480' in body:
                print('账号异常')
                return 0
            tree=etree.HTML(body)
        except Exception as e:
            if self.temp>2:
                self.temp = 0
                return
            self.temp+=1
            print(e)
            print('请求失败，再次重试')
            time.sleep(1)
            return self.gettext(detailurl)
        textlist=tree.xpath('//*[@id="pid1"]/tr[1]/td[2]/div/div[*]/table/tr/td/text()')
        '//*[@id="pid1"]/tr[1]/td[2]/div/div[2]/table/tbody/tr/td'
        text=''
        for i in textlist:
            text+=i.replace('\xa0', '').replace('\r', '').replace('\n','').replace('\u2022','').strip()
        # print(text)
        commentlist=[]
        commentlist1=tree.xpath('/html/body/div[4]/div[13]/div[2]/table/tbody[contains(@id,"pid")]/tr[1]/td[2]/div/div[2]/table/tr/td[1]')
        if len(commentlist1)>1:
            for e in commentlist1[1:]:
                comment= e.xpath('string(.)').replace('\xa0', '').replace('\r', '').replace('\n','').replace('\u2022','').strip()[:-15]
                if len(comment)>4:
                    commentlist.append(comment)
        contentlist=[]
        contentlist.append(text)
        contentlist.extend(commentlist)
        print('saveok')
        if len(contentlist)>0:
            try:
                print(commentlist)
                self.csvwriter.writerow(contentlist)
            except:
                print('存储失败')
        else:
            print('空内容')
    def savedate(self):
        for i in range(1,10):#调整页数
            self.getpage(i)
            time.sleep(1)
        print(len(self.detailurls))
        for index,detailurl in enumerate(self.detailurls):
            time.sleep(random.randrange(1,2))
            print(detailurl,index,'第{}页'.format(index//25))
            temp=self.gettext(detailurl)
            if temp==0:
                break

if __name__ == '__main__':
    domeObject=XiaoMuChong()
    domeObject.savedate()
