import random
import time
import csv
from multiprocessing.dummy import Pool
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

# 创建csv


# 无头浏览器
def task(name,username,password,keywords,datatimes):
    # 写入csv文件
    csvfile = open(f'{name}.csv', 'a', newline='', encoding='gbk')
    writer = csv.writer(csvfile)
    row = 1
    options = webdriver.ChromeOptions()
    # options.add_argument('--headless')
    options.add_argument('--disable-gpu')
    options.add_argument('--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36')
    # ip='49.70.89.90'
    # port='99999'
    # options.add_argument(f"--proxy-server={ip}:{port}")
    prefs = {
                'profile.default_content_setting_values': {
                    'images': 2,
                }
            }
    options.add_experimental_option('prefs', prefs)
    driver=webdriver.Chrome(options=options)
    # 打开初始页面
    starturl='https://www.jianweidata.com/Index'
    driver.implicitly_wait(1)
    driver.get(starturl)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[2]').click()
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="login"]/div[4]/button[1]').click()
    time.sleep(1)
    # 进入搜索页面
    driver.get('https://www.jianweidata.com/SearchMainFiling')
    # 获取内容
    keyword1, keyword2, keyword3=keywords
    for datetime in datetimes:
        print(keyword1,keyword2 )
        time.sleep(1)
        try:
            driver.find_element_by_xpath('//*[@id="guide_page"]/div/div[1]/div/div/span[2]').click()
            driver.find_element_by_xpath('//*[@id="guide_page"]/div/div[2]/div/div/span[2]').click()
            driver.find_element_by_xpath('//*[@id="guide_page"]/div/div[3]/div/div/span[1]').click()
        except:
            pass
        # 获取输入框
        input1=driver.find_element_by_xpath('//*[@id="searchInput"]/div[3]/div/div[3]/div[1]/div/input')
        input2=driver.find_element_by_xpath('//*[@id="searchInput"]/div[1]/div/div[1]/input')
        input3 = driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div/section[1]/div[1]/div/div[1]/div[3]/div/div[1]/div/div[1]/div/input')
        time.sleep(random.randrange(0,1))
        # 清空输入框
        input1.clear()
        input2.clear()
        input1.send_keys(keyword1)
        input2.send_keys(keyword2)
        # 输入关键字
        input3.send_keys(Keys.CONTROL, 'a')
        input3.send_keys(keyword3)
        time.sleep(random.randrange(0,1))
        input = driver.find_element_by_xpath('//*[@id="input_date"]')
        input.clear()
        time.sleep(0.5)
        input.send_keys('2014/01/01 - 2021/01/23')

        # 点击查询
        driver.find_element_by_xpath('//*[@id="btn_search"]').click()
        time.sleep(random.randrange(0,1))


        # 翻页
        driver.find_elements_by_xpath('//*[@id="div_document"]/div[1]')
        try:
            buttonlist=driver.find_elements_by_xpath('//*[@id="div_document"]/div[3]/div[1]/div/button')
        except:
            return
        # driver.close()
        # windows = driver.window_handles
        # driver.switch_to.window(windows[1])
        for button in buttonlist:
            time.sleep(1)
            try:
                button.click()
            except Exception:
                pass
        #     '//*[@id="div_document"]/div[1]/div/div/div[2]/div[3]/div[1]/div/div[3]/a[1]'
        #     '//*[@id="div_document"]/div[1]/div/div/div[2]/div[2]/div[1]/div/div[3]/a[1]'
        # emlist=driver.find_elements_by_xpath('//*[@id="div_document"]/div[1]/div/div/div[2]/div[*]/div[1]/div/a')

        # 获取页面信息
            namelist=driver.find_elements_by_xpath('/html/body/div[1]/div/div[3]/div/section[1]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[*]/div[1]/div/a')
            datelist=driver.find_elements_by_xpath('/html/body/div[1]/div/div[3]/div/section[1]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[*]/div[1]/div/div[3]/span')
            urlems=driver.find_elements_by_xpath('/html/body/div[1]/div/div[3]/div/section[1]/div[2]/div/div/div[1]/div[1]/div/div/div[2]/div[*]/div[1]/div/div[3]/a[1]')
            # 获取pdf url,名称，日期
            for url,name,date in zip(urlems,namelist,datelist):
                url=url.get_attribute('href')
                name=name.text
                date=date.text
                if  name and date  and url:
                    # 写入csv文件
                    writer.writerow([keyword1,keyword2,name,date,url])
                    csvfile.flush()
                    row += 1
                    print(username,row,name,date,url)

            # print(urllist)
            # for em,url in zip(emlist,urllist):
            #     em.click()
            #     time.sleep(random.randrange(0,1))
            #     windows=driver.window_handles
            #     driver.switch_to.window(windows[-1])
            #     time.sleep(random.randrange(0,1))
            #     try:
            #         # element = WebDriverWait(driver,1).until(lambda x: x.find_element_by_xpath('//*[@id="wrap"]/div[1]/div[1]/div/div/a[1]'))
            #         id=driver.find_element_by_xpath('//*[@id="wrap"]/div[1]/div[1]/div/div/a[1]').text
            #         name = driver.find_element_by_xpath('//*[@id="wrap"]/div[1]/div[1]/div/div/a[2]').text
            #         date = driver.find_element_by_xpath('//*[@id="wrap"]/div[1]/div[1]/div/div/div/span').text
            #         contents = driver.find_element_by_xpath('//div[@class="detail"]').text
            #
            #         if  id and name and date and contents and url:
            #             writer.writerow([str(id),name,date,contents,url])
            #             csvfile.flush()
            #             row += 1
            #             print('第几页',str(id),name,date,url)
            #     except:
            #         pass
            #
            #     # print(id,name,date)
            #     # print(contents)
            #
            #     driver.close()
            #     driver.switch_to.window(windows[0])
            #     time.sleep(random.randrange(0,2))
            # csvfile.flush()

if __name__ == '__main__':
    usernames=[
                    'QL001'
                    # '16798643942',
                    # '16570929507',
                    # '16798644142',
                    # '16798644034',
    ]

    passwords=[
                    'cnn654321'
                    # '123456789',
                    # '123456789',
                    # '123456789',
                    # '123456789',

    ]
    keywordlist = []
    # 读取csv文件
    filereader = open('PDF1.csv', 'r', encoding='gbk')
    lines = csv.reader(filereader)
    # 增发：可行性分析报告
    # 首发：招股说明书
    # 配股：可行性分析报告
    # 发行可转债：可行性分析报告
    next(lines)
    for line in lines:
        key = '可行性'
        if line[4].strip() == '首发':
            key = '招股'
        keywordlist.append((line[0],line[1],key))
    # 开启线程池
    threadPool = Pool(processes=2)
    lists=[keywordlist[0:500],keywordlist[500:1000],keywordlist[1000:1500],keywordlist[1500:]]
    j=0
    for name,username,password,list in zip(j,usernames,passwords,lists):
        future = threadPool.apply_async(task, (name,username,password,list))
        j+=1
    threadPool.close()
    threadPool.join()

    # list=[
    #     ('','002237.SZ',''),
    #     ('','688557.SH',''),
    #     ('','300911.SZ',''),
    #     ('','605068.SH',''),
    # ]
    # task('text', usernames[0], passwords[0], list)

