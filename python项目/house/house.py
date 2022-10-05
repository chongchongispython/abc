import csv
import random
import re
import time
from multiprocessing.dummy import Pool
import requests
from lxml import etree

# 获取房屋id
def getid(page,name):
    csvfile=open(f'{name}.csv','a',newline='',encoding='utf-8')
    writer = csv.writer(csvfile)
    session=requests.session()

    headers={
        'Accept': 'text/html, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.9',
    'Connection': 'keep-alive',
    'Cookie': getidcookie(),
    'Host': 'rpp.rpdata.com',
    'Referer': 'https://rpp.rpdata.com/rpp/search/address/property/summary.html?q=Cremorne+NSW&qt=address&view=property&newSearch=true&quickSearch=true&searchWindowId=200716020-INTERIM',
    'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
    }
    for i in range(1,page):
        time.sleep(random.randrange(3,8))
        url = f'https://rpp.rpdata.com/rpp/search/address/property/summary.html?q=Cremorne+NSW&qt=address&_qt=address&offset={i}&sort=last_sale_date&limit=20&view=property&mode=&radius=1.0Km&landuse=All&propertyType=HOUSE&exclusiveCriteria=false&searchWindowId=200827175&_=1612333624479&search_type_param=address'
        resonse=session.get(url=url,headers=headers)
        print(resonse.status_code)
        idlist=re.findall(r"open_property_detail\('(\d*)', '.*?', .*?\)",resonse.content.decode())
        print(idlist)
        print(len(idlist))
        writer.writerow(idlist)
        csvfile.flush()

#获取详情页数据并写入csv
def getdate(id,writer):
    headers={
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Connection': 'keep-alive',
        'Cookie': getdetailcookie(),
        'Host': 'rpp.rpdata.com',
        'Referer': 'https://rpp.rpdata.com/rpp/search/address/property/summary.html?q=Cremorne+NSW&qt=address&_qt=address&offset=64&sort=last_sale_date&limit=20&view=property&mode=&radius=1.0Km&landuse=All&propertyType=HOUSE&exclusiveCriteria=false&searchWindowId=200827175',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
    }
    url=f'https://rpp.rpdata.com/rpp/property/detail.html?propertyId={id}&index=0&_qt=address&q=Cremorne+NSW&qt=address&offset=1&sort=last_sale_date&limit=20&view=property&mode=&radius=1.0Km&landuse=All&propertyType=HOUSE'
    try:
        response=requests.get(url=url,headers=headers,proxies=ipagent())
        print(response.status_code)
    except:
        print('请求失败')
        getdate(id,writer)
    tree=etree.HTML(response.content.decode())
    try:
        address=tree.xpath('//*[@id="expandedAddress_icons"]/text()')
        if address:
            address=address[0]
        rpd=tree.xpath('//*[@id="legalPanel"]/div/ul/li[1]/text()')
        if rpd:
            rpd=rpd[0].strip()
        zoning=tree.xpath('//*[@id="lastSalePanel"]/div/ul[2]/li/text()')
        if zoning:
            zoning=zoning[0]
        area=tree.xpath('//*[@id="expandedAddress"]/div/div/ul/li[5]/span[1]/text()')
        if area:
            area=area[0]
        bedroom=tree.xpath('//*[@id="overview"]/div/div[1]/div/ul[1]/li[1]/span/text()')
        if bedroom[0].strip()!='-':
            bedroom=bedroom[0]
        else:
            bedroom=0
        toilet=tree.xpath('//*[@id="overview"]/div/div[1]/div/ul[1]/li[2]/span/text()')
        if toilet[0].strip() != '-':
            toilet = toilet[0]
        else:
            toilet = 0
        parking=tree.xpath('//*[@id="overview"]/div/div[1]/div/ul[1]/li[3]/span/text()')
        if parking[0].strip() != '-':
            parking = parking[0]
        else:
            parking = 0
        yearbuilt=tree.xpath('//*[@id="overview"]/div/div[2]/ul/li[2]/label/following::text()')
        if yearbuilt:
            yearbuilt=yearbuilt[0].strip()
        else:
            yearbuilt=0
        transferdates=tree.xpath('//*[@id="saleHistoryPanel"]/table/tbody/tr[*]/td[1]/text()')
        saleprices=tree.xpath('//*[@id="saleHistoryPanel"]/table/tbody/tr[*]/td[3]/text()')
        SalesHistory=''
        for t,s in zip(transferdates,saleprices):
            if s!='Not Disclosed':
                SalesHistory=SalesHistory+t+':'+s+'、'
    except:
        print('解析失败')
        return

    print(address,rpd,zoning,area,bedroom,toilet,parking,yearbuilt,SalesHistory)
    writer.writerow([address,rpd,zoning,area,bedroom,toilet,parking,yearbuilt,SalesHistory])
    csvfilew.flush()

# 获取代理ip
def ipagent():
    # 购买代理网址   http://sem.ipidea.net/getapi/
    # 把本机ip加入白名单接口
    # url='http://api.ipidea.net/index/index/save_white?neek=208925&appkey=9a08fec16e774b5d5d2edd393a27ffe0&white=***'
    # response=requests.get(url=url)
    url1='http://tiqu.linksocket.com:81/abroad?num=1&regions=us&type=3&flow=1&lb=1'
    response1=requests.get(url=url1)
    ip_port=response1.content.decode().strip()
    print(ip_port)
    proxies = {
        "http": "%s" % ip_port,
        "https": "%s" % ip_port
    }
    return proxies

# 获取详情页cookie
def getdetailcookie():
    # 详情页cookie需要更换
    cookie='JSESSIONID=8D4191E1DC740E17368E8C0A9B92F5E8; TS01d46e42=011156f97e88ff64947d2eff7fc7147879c867d82ee895784edf3962f999819fae750ebe3acc906b232560fc9588f066cb9e7915e91237482035b3ffb4c67f63335f0ac959; RPDataCookie=3556788234.36895.0000; __utmc=124425417; ajs_user_id=%22paulsong%22; ajs_anonymous_id=%22cfe3ae6b-d3ca-4d17-83bd-a90c5c668f0d%22; _hjTLDTest=1; _hjid=e801d196-55b7-4b12-8dc0-70ea617c9d8e; __zlcmid=12SjmWj4yriQXnH; __utmz=124425417.1612428601.5.2.utmcsr=access-api.corelogic.asia|utmccn=(referral)|utmcmd=referral|utmcct=/; TS01978196_77=0899b1feb5ab28004ad7d65e1725391992990738c143891bd1635332627a4411342867a38469d88105fd39d4c53c014d08b2a014228238009a4d7e9949df21d04a303dc975671339e2ca44b0eab458a1d0ccc874475c7f352178aa07f744212efa2a6010fb7030f922e4dff3c8261d4a; prev_url=https%3A%2F%2Frpp.rpdata.com%2Frpp%2Fsearch%2Faddress%2Fproperty%2Fsummary.html%3Fq%3DCremorne%2BNSW%26qt%3Daddress%26_qt%3Daddress%26offset%3D1%26sort%3Dlast_sale_date%26limit%3D20%26view%3Dproperty%26mode%3D%26radius%3D1.0Km%26landuse%3DAll%26propertyType%3DHOUSE%26exclusiveCriteria%3Dfalse%26searchWindowId%3D200957468; __utma=124425417.235612930.1612289861.1612430669.1612436511.7; __utmt=1; __utmb=124425417.3.8.1612436516838; TS01978196=011156f97e60e98504a59c658724f4001d9fbed410d0cbfce4b90c063dbd474bf59a9470931a5c3ff50964bfab00d961acb5a82fbc031fd90c5db55f88fdabe7a604f653960e6ac17b5c4eaef35d81dccb841e9127bc4a4f779994893981861fc904f6b4182bcd9188ff7c9bf742ac240fd0b5e90517ab5e4181a57d6c45dea4064f1f637a5f070026d5800081c3caf4278916b992; _hjAbsoluteSessionInProgress=1'
    return cookie

# 获取列表页cookie
def getidcookie():
    # 列表页cookie需要更换
    cookie='csvShowHeader=false; csvHeaderLabel=NOT%20SELECTED; total_counter=1277; BACK_PARAMS=q%3DCremorne%2BNSW%26qt%3Daddress%26_qt%3Daddress%26offset%3D4%26sort%3Dlast_sale_date%26limit%3D20%26view%3Dproperty%26mode%3D%26radius%3D1.0Km%26landuse%3DAll%26propertyType%3DHOUSE%26exclusiveCriteria%3Dfalse; BACK_URL=%2Frpp%2Fsearch%2Faddress%2Fproperty%2Fsummary.html%3Fq%3DCremorne%2BNSW%26qt%3Daddress%26_qt%3Daddress%26offset%3D4%26sort%3Dlast_sale_date%26limit%3D20%26view%3Dproperty%26mode%3D%26radius%3D1.0Km%26landuse%3DAll%26propertyType%3DHOUSE%26exclusiveCriteria%3Dfalse%26searchWindowId%3D200827175; JSESSIONID=B2F7419AF28FC69C76FF516936DECF8F; TS01d46e42=011156f97ed8ef6d998a4ac811890b936d1427b851e895784edf3962f999819fae750ebe3afb2c747ef8021f286103fa23de492bcc9828a45b7012614ae99b238236925091; RPDataCookie=3556788234.36895.0000; __utmc=124425417; __utmz=124425417.1612289861.1.1.utmcsr=access-api.corelogic.asia|utmccn=(referral)|utmcmd=referral|utmcct=/; ajs_user_id=%22paulsong%22; ajs_anonymous_id=%22cfe3ae6b-d3ca-4d17-83bd-a90c5c668f0d%22; _hjTLDTest=1; _hjid=e801d196-55b7-4b12-8dc0-70ea617c9d8e; __zlcmid=12SjmWj4yriQXnH; _hjAbsoluteSessionInProgress=0; __utma=124425417.235612930.1612289861.1612328340.1612332564.3; TS01978196_77=0899b1feb5ab2800e993b1250e278404c88d08bdfa1152293ecff7ea5b2d211c3756cc956fe614c62814f1709d949c15088ab1ebbd82c800a5827dfd2244c01f5396bf0a489398f6d6d0749d97aaf7f90aa15f63358ed53860cb5a49d898f569d2809ff2f3565686b91f9a8d169c04749973ead4f833e7042c85b9ac3493ca7b0480022f0958a5a3f3514974187208b716241ac6bdabdf127cfd8a4400191fdeba589ededbf2b82f16d07953128ec9ae760fa48376b78decd0fab88312f51fe6140b7163b26c3b2df939b685294a555aa06277845a6eb4750891d5869358a85829f2b767a45a1c146d3f173963c46fd454aba453a602061e49bf9dc95d472334; prev_url=https%3A%2F%2Frpp.rpdata.com%2Frpp%2Fsearch%2Faddress%2Fproperty%2Fsummary.html%3Fq%3DCremorne%2BNSW%26qt%3Daddress%26view%3Dproperty%26newSearch%3Dtrue%26quickSearch%3Dtrue%26searchWindowId%3D200716020-INTERIM; __utmt=1; __utmb=124425417.7.8.1612333579801; TS01978196=011156f97ef8e3045fb2628ddaa6c906cde9f929248c83e19782d49eb9fe1f7456eb218b8834bea7f7db8f01037a9334c2cac87b7cb6a2f6b71fc2907ab571340337122a42e5ba888d370a61c07ad02919aaacb195eb4bc2a9da182755d26e5f8ce98dfdcf3db6f45b339f31df51fad567ea97233f98eb6b7d0f21de0a95c9c56256fccaec3216773056d3870375d04905ceae4a4a'
    return cookie


if __name__ == '__main__':
    csvidname='id'
    # 总页数
    page=65
    # 写入house的id
    getid(page,csvidname)
    # 打开写入文件
    csvfilew=open('date.csv','a',newline='',encoding='utf-8')
    writer = csv.writer(csvfilew)
    # 打开id文件
    csvflier=open(f'{csvidname}.csv','r',newline='',encoding='utf-8')
    reader=csv.reader(csvflier)
    # 开启多线程
    threadPool=Pool(processes=5)
    i=1
    for line in reader:
        for id in line:
            print(id)
            threadPool.apply_async(getdate, (id,writer))
            i+=1
            print(i)
    threadPool.close()
    threadPool.join()
