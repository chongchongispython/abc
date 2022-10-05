import csv
import json
import random
import re
import time
from multiprocessing.dummy import Pool
import requests
from jsonpath import jsonpath
from lxml import etree

#获取详情页数据并写入csv
def getdate(ip,writer):
    print(ip)
    seeeion=requests.session()
    headers = {
        #     ':authority': 'pro.similarweb.com'
        # ':method': 'GET'
        # ':path': '/widgetApi/WebsiteOverviewDesktop/TrafficSourcesOverview/PieChart?country=999&from=2020%7C10%7C01&includeSubDomains=true&isDaily=false&isWindow=false&keys=bebe.com&timeGranularity=Monthly&to=2020%7C12%7C31&webSource=Desktop'
        # ':scheme': 'https'
        'accept': 'application/json, text/plain, */*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'zh-CN,zh;q=0.9',
        'cookie': getdetailcookie(),
        'referer': 'https://pro.similarweb.com/',
        'sec-ch-ua': '"Chromium";v="88", "Google Chrome";v="88", ";Not A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': getua(),
        'x-requested-with': 'XMLHttpRequest',
        'x-sw-page': 'https://pro.similarweb.com/#/website/worldwide-overview/baidu.com/*/999/2020.10-2020.12?webSource=Total',
            # 'https://pro.similarweb.com/#/website/worldwide-overview/bebe.com/*/999/2020.10-2020.12?webSource=Total',
        'x-sw-page-view-id': '8bdb0a84-0849-4f6b-a27b-6e4899e6670b',
    }
    proxies = ipagent()
    TotalVisitsurl=f'https://pro.similarweb.com/widgetApi/WebsiteOverview/EngagementVisits/SingleMetric?ShouldGetVerifiedData=false&country=999&from=2020%7C10%7C01&includeSubDomains=true&isDaily=false&isWindow=false&keys={ip}&timeGranularity=Monthly&to=2020%7C12%7C31&webSource=Total'
    # 'https://pro.similarweb.com/widgetApi/WebsiteOverviewDesktop/TrafficDestinationAds/Table?country=999&from=2020%7C01%7C01&includeSubDomains=true&isDaily=false&isWindow=false&keys=babbel.com&orderBy=TotalShare+desc&pageSize=5&timeGranularity=Monthly&to=2020%7C03%7C31&webSource=Desktop'
    try:
        time.sleep(random.randrange(1,3))
        response=requests.get(url=TotalVisitsurl,headers=headers,proxies=proxies)
        print(response.status_code)
        if response.status_code!=200:
            getdate(ip, writer)
            print('cookie失效')
    except:
        time.sleep(1)
        print('请求失败')
        getdate(ip,writer)
    jsonobj=json.loads(response.content.decode())
    TotalVisits=int(jsonpath(jsonobj,'$..TotalVisits')[0])
    print(TotalVisits)
    marketshareurl=f'https://pro.similarweb.com/widgetApi/WebsiteOverview/EngagementDesktopVsMobileVisits/PieChart?ShouldGetVerifiedData=false&country=999&from=2020%7C10%7C01&includeSubDomains=true&isDaily=false&isWindow=false&keys={ip}&timeGranularity=Monthly&to=2020%7C12%7C31&webSource=Total'
    try:
        time.sleep(random.randrange(1,2))
        response=requests.get(url=marketshareurl,headers=headers,proxies=proxies)
        print(response.status_code)
        if response.status_code!=200:
            getdate(ip,writer)
            print('cookie失效')
    except:
        time.sleep(1)
        print('请求失败')
        getdate(ip,writer)
    jsonobj=json.loads(response.content.decode())
    Desktop=jsonpath(jsonobj,'$..Desktop')[0]
    MobileWeb=jsonpath(jsonobj,'$..Mobile Web')[0]
    Desktoppercentage="%.2f%%" % (Desktop/(Desktop+MobileWeb) * 100)
    MobileWebpercentage="%.2f%%" % (MobileWeb/(Desktop+MobileWeb) * 100)
    print(Desktoppercentage,MobileWebpercentage)

    marketingchannelsurl=f'https://pro.similarweb.com/widgetApi/WebsiteOverviewDesktop/TrafficSourcesOverview/PieChart?country=999&from=2020%7C10%7C01&includeSubDomains=true&isDaily=false&isWindow=false&keys={ip}&timeGranularity=Monthly&to=2020%7C12%7C31&webSource=Desktop'
    try:
        time.sleep(random.randrange(1,2))
        response=requests.get(url=marketingchannelsurl,headers=headers,proxies=proxies)
        print(response.status_code)
        if response.status_code!=200:
            getdate(ip,writer)
            print('cookie失效')
    except:
        time.sleep(1)
        print('请求失败')
        getdate(ip,writer)
    jsonobj=json.loads(response.content.decode())
    Direct=jsonpath(jsonobj,'$..Direct')
    if Direct:
        Direct=Direct[0]
    else:
        Direct=0

    Mail = jsonpath(jsonobj, '$..Mail')
    if Mail:
        Mail = Mail[0]
    else:
        Mail = 0

    OrganicSearch = jsonpath(jsonobj, '$..Organic Search')
    if OrganicSearch:
        OrganicSearch = OrganicSearch[0]
    else:
        OrganicSearch = 0

    PaidReferrals = jsonpath(jsonobj, '$..Paid Referrals')
    if PaidReferrals:
        PaidReferrals = PaidReferrals[0]
    else:
        PaidReferrals = 0

    PaidSearch = jsonpath(jsonobj, '$..Paid Search')
    if PaidSearch:
        PaidSearch = PaidSearch[0]
    else:
        PaidSearch = 0

    Referrals = jsonpath(jsonobj, '$..Referrals')
    if Referrals:
        Referrals = Referrals[0]
    else:
        Referrals = 0

    Social = jsonpath(jsonobj, '$..Social')
    if Social:
        Social = Social[0]
    else:
        Social = 0
    sum=Direct+Mail+OrganicSearch+PaidReferrals+PaidSearch+Referrals+Social

    Directpercentage = "%.2f%%" % (Direct / sum * 100)
    Mailpercentage = "%.2f%%" % (Mail / sum * 100)
    OrganicSearchpercentage = "%.2f%%" % (OrganicSearch / sum * 100)
    PaidReferralspercentage = "%.2f%%" % (PaidReferrals / sum * 100)
    PaidSearchpercentage = "%.2f%%" % (PaidSearch / sum * 100)
    Referralspercentage = "%.2f%%" % (Referrals / sum * 100)
    Socialcentage = "%.2f%%" % (Social / sum * 100)
    print(Directpercentage,Mailpercentage,OrganicSearchpercentage,PaidReferralspercentage,PaidSearchpercentage,Referralspercentage,Socialcentage)
    writer.writerow([TotalVisits,Desktoppercentage,MobileWebpercentage,Directpercentage,Mailpercentage,OrganicSearchpercentage,PaidReferralspercentage,PaidSearchpercentage,Referralspercentage,Socialcentage,ip])
    csvfilew.flush()
# 获取代理ip
# def ipagent():
#     # 购买代理网址   http://sem.ipidea.net/getapi/
#     # 把本机ip加入白名单接口
#     # url='http://api.ipidea.net/index/index/save_white?neek=208925&appkey=9a08fec16e774b5d5d2edd393a27ffe0&white=***'
#     # response=requests.get(url=url)
#     url1='http://tiqu.linksocket.com:81/abroad?num=1&regions=us&type=3&flow=1&lb=1'
#     response1=requests.get(url=url1)
#     ip_port=response1.content.decode().strip()
#     print(ip_port)
#     proxies = {
#         "http": "%s" % ip_port,
#         "https": "%s" % ip_port
#     }
#     return proxies
def ipagent():
    # changeurl = 'https://tps.kdlapi.com/api/changetpsip?orderid=901254554189658&signature=0i9gvh854eemdvshbfytk9y7osp7gart'
    # response= requests.get(changeurl)
    # print('更换ip',response.content.decode())

    # searchurl='https://tps.kdlapi.com/api/gettpsip?orderid=901254554189658&signature=0i9gvh854eemdvshbfytk9y7osp7gart'
    # response= requests.get(searchurl)
    # print('当前ip',response.content.decode())

    apis = "https://tps.kdlapi.com/api/gettps/?orderid=901254554189658&num=1&format=json&sep=1"
    response = requests.get(apis)
    ip_port = json.loads(response.text)['data']['proxy_list'][0]
    # 'https': 'tps173.kdlapi.com:15818'
    proxies = {
        "http": "%s" % ip_port,
        "https": "%s" % ip_port
    }
    # 'https': 'tps173.kdlapi.com:15818'
    return proxies


# 获取详情页cookie
def getdetailcookie():
    # 详情页cookie需要更换
    # cookiepool=[
    #
    # ]
    # cookie=random.choice(cookiepool)
    cookie='locale=zh-cn; .DEVICETOKEN.SIMILARWEB.COM=9sioKctfPe4QCUslDyMSMIbGSR3Oreto; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=JFD5391CEB0044598999A1A57CB13ABA9; _vwo_ds=3%241612690476%3A90.87523187%3A%3A; _vwo_uuid_v2=D88E5CAE304784E2F6CF370662AA16931|8be5cf0bab5439404e051feaebeaae49; _ga=GA1.2.448942785.1612690477; _gid=GA1.2.1691564322.1612690477; _gcl_au=1.1.822603106.1612690477; _wingify_pc_uuid=ab653ed923d84c6f97f44bcd74212ef3; _sp_ses.614e=*; _pk_ses.1.fd33=*; wingify_donot_track_actions=0; _sp_id.614e=8cefcd20-c4ac-44f5-b09a-8ea59c0756f5.1612690489.1.1612690510.1612690489.78d16408-7359-4023-b82d-07e7f3655eb7; .SGTOKEN.SIMILARWEB.COM=8qGLKwePN7tl7FYDYG7dXOTf2s63teyVa479ll5FrnP0D5Ex8DQ814bVxhgJwmKugqIJ40ZzacoiHg78m_FrGjaks7aSKNmbIOXNJeZZ3NgHNB4iNmwJ_XoKIP20k4i1ERv0sunLNBFzFHWbQubNNDyQn3wI62JQMaiHVZjEz0czuIdFLhjKK_Y0N2fOW_SWfhMqZrC4aHEPCGQOx7bi1ztsM2eDZx63Gicu_OCCL32Mtq3oTBiGONIlqozGehAYPVwMvPoaS4v6aLpJhAiYvJFQrcfWzjamDWlkMHC9dQiH3ZvAQiXwGt4dgVI67G3V4iU8CByznIrdTXddu9BmOdjEDZePCTam20Yi3wfyunHWUpysnHwLkg0e3f4LovVvYVIFDnSKqWGMJdtVPEJE_XZckpkSW9MepcfoGM5-1WrO3k8YiXWnNcMia4eifrak; _pk_id.1.fd33=b74b28aff349b85e.1612690478.1.1612690522.1612690478.; _vis_opt_exp_350_combi=2; RESET_PRO_CACHE=False; sgID=9a5b0810-691b-4e01-a092-56402279b8fb; _pk_ses.1.3432=*; _gat=1; _vwo_sn=0%3A9%3A%3A%3A1; _pk_id.1.3432=4905f165447d34c1.1612690650.1.1612692204.1612690650.; mp_7ccb86f5c2939026a4b5de83b5971ed9_mixpanel=%7B%22distinct_id%22%3A%20%228914774%22%2C%22%24device_id%22%3A%20%221777bd83c9657e-0a5b06472c88b8-33e3567-1fa400-1777bd83c97834%22%2C%22site_type%22%3A%20%22Pro%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22session_id%22%3A%20%223b1db764-274b-48ad-b91e-964dbb5b4529%22%2C%22session_first_event_time%22%3A%20%222021-02-07T09%3A35%3A05.038Z%22%2C%22url%22%3A%20%22https%3A%2F%2Fpro.similarweb.com%2F%23%2Fwebsite%2Fworldwide-overview%2Fthekitchen.bedbathandbeyond.com%2F*%2F999%2F3m%3FwebSource%3DTotal%22%2C%22is_sw_user%22%3A%20false%2C%22language%22%3A%20%22zh-cn%22%2C%22section%22%3A%20%22websiteAnalysis%22%2C%22sub_section%22%3A%20%22overview%22%2C%22sub_sub_section%22%3A%20%22websitePerformance%22%2C%22page_id%22%3A%20%22analysis.overview.performance.title%22%2C%22last_event_time%22%3A%201612692203883%2C%22%24user_id%22%3A%20%228914774%22%2C%22sgId%22%3A%20%229a5b0810-691b-4e01-a092-56402279b8fb%22%2C%22ui_generation%22%3A%20%22%22%2C%22subscription_id%22%3A%20%2246789520%22%2C%22base_product%22%3A%20%22FRO%20-%20After%20Trial%22%2C%22user_id%22%3A%208914774%2C%22account_id%22%3A%2010000019%2C%22email%22%3A%20%22wuhanxiang%40dahetouzi.com.cn%22%2C%22country%22%3A%20999%2C%22web_source%22%3A%20%22TOTAL%22%2C%22date_range%22%3A%20%223m%22%2C%22entity_id%22%3A%20%22thekitchen.bedbathandbeyond.com%22%2C%22entity_name%22%3A%20%22thekitchen.bedbathandbeyond.com%22%2C%22domain_type%22%3A%20%22WITH_SUBDOMAINS%22%2C%22main_category%22%3A%20%22Food%20and%20Drink%22%2C%22sub_category%22%3A%20%22Groceries%22%2C%22custom_category_id%22%3A%20null%7D'
    # cookie='locale=zh-cn; .DEVICETOKEN.SIMILARWEB.COM=6rFn22zM47JQKORHNogOXITCgRI4R3e4; _vis_opt_s=1%7C; _vis_opt_test_cookie=1; _vwo_uuid=J5769C472DAC45A2900CA9B54A25046D9; _vwo_ds=3%241612535279%3A90.7015129%3A%3A; _vwo_uuid_v2=D8BAF58A5B4D34A14E4F8B442087B5022|f734c59971bcd8dcff8d6926f69fb542; _ga=GA1.2.1410250873.1612535281; _gid=GA1.2.1657680770.1612535281; _gcl_au=1.1.9241612.1612535282; _hjTLDTest=1; _hjid=80e44844-3e5a-4895-b2bf-e15032bc8843; .SGTOKEN.SIMILARWEB.COM=8qGLKwePN7tl7FYDYG7dXOTf2s63teyVa479ll5FrnP0D5Ex8DQ814bVxhgJwmKugqIJ40ZzacoiHg78m_FrGgT8m6dD7wfjPShvcOBQUHaP7E4XNFkAoVsq8Lxww_uXzYbHA5n2_wrlUuqsMLki6EgCzg3uWGX-7YKKCXTtwicgfUB6TjgeGXlTFiqgiTrjfaRD-Oh2a3MRoJk1IE_LJF8sYjiiUH1vYaCueocvAYwzXwOt1IQ8RstUOhnY452waWjHyPkzjrJ8drUllYhS8zfFuWfOmxGINEO_eTylsAwmZcseg2HLoeWnt2gLbYQVhEPfcOkI5WK5yJ_fadnJElZK7sJJsgGOl89KiubB1ThxZ10rt1-catqtxGhf5y-1IzmQfOgEpc4UGZ0iyAHu9Wjd62h0T0GpVwpQZBQUjIk_xIJV553J9UG6zKQLEl2C; _pk_id.1.fd33=3a9c76321e496f5d.1612535281.1.1612535287.1612535281.; _vis_opt_exp_350_combi=2; RESET_PRO_CACHE=False; sgID=1d259332-4dab-45ea-a137-369086d20b5d; _fbp=fb.1.1612535311559.490150447; _pk_ses.1.3432=*; intercom-session-e74067abd037cecbecb0662854f02aee12139f95=d1hhOStMM1pVdkhJSktYK2w2QkkrczRxZi9MQ2RJN3VYUUlmd0tKREhIUnNIbTFHd3JjUUhwempmTTQrTUlFcS0tQVFaYmxmdzEwSHQzOVd3L0UxOG9xUT09--f7e2b0eda97b58973f56a0024662262e80823f6b; _gat=1; _vwo_sn=0%3A9%3A%3A%3A1; _pk_id.1.3432=4905f165447d34c1.1612535307.2.1612540099.1612535382.; mp_7ccb86f5c2939026a4b5de83b5971ed9_mixpanel=%7B%22distinct_id%22%3A%20%228914774%22%2C%22%24device_id%22%3A%20%221777297b2b9806-0e3951418f3bec-33e3567-1fa400-1777297b2ba7f5%22%2C%22url%22%3A%20%22https%3A%2F%2Fpro.similarweb.com%2F%23%2Fwebsite%2Fworldwide-overview%2Fcettire.com%2F*%2F999%2F2020.10-2020.12%3FwebSource%3DTotal%22%2C%22is_sw_user%22%3A%20false%2C%22language%22%3A%20%22zh-cn%22%2C%22section%22%3A%20%22websiteAnalysis%22%2C%22sub_section%22%3A%20%22overview%22%2C%22sub_sub_section%22%3A%20%22websitePerformance%22%2C%22page_id%22%3A%20%22analysis.overview.performance.title%22%2C%22last_event_time%22%3A%201612540098580%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%2C%22site_type%22%3A%20%22Pro%22%2C%22session_id%22%3A%20%2298589563-13ab-4357-bcb1-f6fbd563c034%22%2C%22session_first_event_time%22%3A%20%222021-02-05T15%3A09%3A18.634Z%22%2C%22%24user_id%22%3A%20%228914774%22%2C%22sgId%22%3A%20%221d259332-4dab-45ea-a137-369086d20b5d%22%2C%22ui_generation%22%3A%20%22%22%2C%22country%22%3A%20999%2C%22web_source%22%3A%20%22TOTAL%22%2C%22subscription_id%22%3A%20%2246789520%22%2C%22base_product%22%3A%20%22FRO%20-%20After%20Trial%22%2C%22user_id%22%3A%208914774%2C%22account_id%22%3A%2010000019%2C%22email%22%3A%20%22wuhanxiang%40dahetouzi.com.cn%22%2C%22date_range%22%3A%20%222020.10-2020.12%22%2C%22entity_id%22%3A%20%22cettire.com%22%2C%22entity_name%22%3A%20%22cettire.com%22%2C%22domain_type%22%3A%20%22WITH_SUBDOMAINS%22%2C%22main_category%22%3A%20%22Lifestyle%22%2C%22sub_category%22%3A%20%22Fashion%20and%20Apparel%22%2C%22custom_category_id%22%3A%20null%7D'
    return cookie

def getua():

#     uapool = [
#     '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.6.2840.99 Safari/537.36',
#     '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.5.2840.99 Safari/537.36',
#     '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.4.2840.99 Safari/537.36',
#     '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.3.2840.99 Safari/537.36',
#     '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.2.2840.99 Safari/537.36',
#     '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.1.2840.99 Safari/537.36',
#
# ]
    ua=f'--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{random.randint(66,85)}.{random.randint(1,9)}.{random.randint(1000,3000)}.99 Safari/537.36'
    return ua
if __name__ == '__main__':
    csvidname='domain1'
    # 打开写入文件
    csvfilew=open(f'{csvidname}date.csv','a',newline='',encoding='utf-8')
    writer = csv.writer(csvfilew)
    # 打开id文件
    csvflier=open(f'{csvidname}.csv','r',newline='',encoding='utf-8')
    reader=csv.reader(csvflier)
    cookiepool=[
        ''
    ]
    # 开启多线程
    threadPool=Pool(processes=1)
    i=1
    for ip in reader:
        if i<200:
            i+=1
            continue
        ip=ip[0].strip()
        threadPool.apply_async(getdate, (ip,writer))
        i+=1
        print(i)
    threadPool.close()
    threadPool.join()
