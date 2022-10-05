import httpx as webSpider  #导入httpx包用于对网页发起请求
import csv  #用于将数据保存到csv文件中
import json #由于拿到的数据大都为json类型的数据因此
from lxml import etree #进行xpath解析
import requests
from selenium import webdriver

class Spider:
    #进行UA伪装
    headers = {
        'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Mobile Safari/537.36 Edg/93.0.961.38'
    }

    parse_message_url = 'https://ir.p5w.net/roadshow/getAllRoadshowList.shtml'#抓取第一个界面的数据

    page_index = 0  #起始页为第0页

    data_parse_message = {  #第一个界面请求的post提交表单
        'page':page_index,
        'row':9  #每个界面9个内容
    }
    parse_more_message_url = 'https://wxly.p5w.net/Roadshow/getLiveInteraction.html'#爬起详情页的数据
    data_parse_more_message = {
        'companyRoadshowID':'', #pid参数由上一个界面获得用于请求第二个json数据包
        'start':'0'
    }
    load_url = 'https://wxly.p5w.net/login/dologin2.html'
    load_data = {
        'mobileArea': '0086',
        'areaMobile': '0086',
        'mobile': '18857444392',
        'password': 'rhd1614581879'
    }
    session = requests.session() #进行模拟登陆
    session.post(url=load_url,data=load_data,headers=headers).json()
    print("模拟登陆成功")

    def parse_message(self):
        while self.page_index <= 0:  #爬到第910页刚刚好
            parse_message_json = webSpider.post(url=self.parse_message_url,data=self.data_parse_message,headers=self.headers).json()
            for row in parse_message_json['rows']:
                message_dict = {}
                message_dict['companyRoadshowID'] = row['pid']
                message_dict['perRealname'] = row['perRealname'] #路演主体
                message_dict['roadshowTitle'] = row['roadshowTitle'] #路演标题
                message_dict['roadshowDates'] = row['roadshowDates'] #发布时间
                self.parse_more_message(message_dict)  #调用第二个方法
            print("页数：",self.page_index)
            self.page_index += 1

    def parse_more_message(self,message_dict):
        self.data_parse_more_message['companyRoadshowID'] = message_dict['companyRoadshowID']
        parse_more_message_json =self.session.post(url=self.parse_more_message_url,data=self.data_parse_more_message,headers=self.headers).json()
        print(parse_more_message_json)
        input_into_csv_list = []
        input_into_csv_list.append(message_dict['perRealname'])
        input_into_csv_list.append(message_dict['roadshowTitle'])
        input_into_csv_list.append(message_dict['roadshowDates'])
        try:
            for row in parse_more_message_json['data']['rows']:
                input_into_csv_list.append(row['replyList']['speakUserName'])
                input_into_csv_list.append(row['speakContent'])
                input_into_csv_list.append(row['replyList']['speakContent'])
        except:
            pass
        print(input_into_csv_list)
        csvOpen = open('data.csv','a',encoding='utf-8',newline='')
        csvWrite = csv.writer(csvOpen)
        csvWrite.writerow(input_into_csv_list)
        csvOpen.close()

if __name__ == '__main__':
    # spider = Spider()
    # spider.parse_message()
    # url = 'https://wxly.p5w.net/Roadshow/getLiveInteraction.html'
    # data = {
    #     'companyRoadshowID':'0001D811F2B605D543079F8ECF58FC99880D', #pid参数由上一个界面获得用于请求第二个json数据包
    #     'start':'0'
    # }
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Mobile Safari/537.36 Edg/93.0.961.38',
    #     'Cookie': 'think_var=zh-cn; PHPSESSID=4gtf1rkbmlv9kk2gsbo0m5va65; Hm_lvt_ed9dac8a2b525df95dc69c97bbcda470=1630857299,1630939055; mw_fp=2X9Vyo3Wz9kfSdfHl11ahj9BVhCW4QaB; uvCookie=b7e6e43d-7194-4c0f-8753-6bd33e4d0d5b; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%220001CED432DB1BA14A298328FE971D4E9762%22%2C%22first_id%22%3A%2217bb6ab82fe4e4-0067601c5d2458-5734174f-2073600-17bb6ab82ff6cc%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_referrer%22%3A%22%22%7D%2C%22%24device_id%22%3A%2217bb6ab82fe4e4-0067601c5d2458-5734174f-2073600-17bb6ab82ff6cc%22%7D; Hm_lpvt_ed9dac8a2b525df95dc69c97bbcda470=1631012160'
    # }
    # print(requests.post(url=url,headers=headers,data=data).json())
    r = webdriver.Chrome()
    r.get('https://rs.p5w.net/html/128870.shtml')

