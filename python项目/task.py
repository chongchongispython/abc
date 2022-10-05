# encoding=gbk
import random
import time
import csv
from multiprocessing.dummy import Pool
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys


# 无头浏览器
def task(name,username,password,keywords):
    row = 1
    csvfile = open(f'{name}.csv', 'a', newline='', encoding='gbk')
    writer = csv.writer(csvfile)
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
    #
    driver=webdriver.Chrome(options=options)
    starturl='https://www.jianweidata.com/Index'
    driver.implicitly_wait(1)
    driver.get(starturl)
    driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[2]').click()
    driver.find_element_by_xpath('//*[@id="username"]').send_keys(username)
    driver.find_element_by_xpath('//*[@id="password"]').send_keys(password)
    driver.find_element_by_xpath('//*[@id="login"]/div[4]/button[1]').click()
    time.sleep(1)

    driver.get('https://www.jianweidata.com/SearchMainFiling')
    for keyword1,keyword2 in keywords:
        print(keyword1,keyword2 )
        time.sleep(random.randrange(0,1))
        try:
            driver.find_element_by_xpath('//*[@id="guide_page"]/div/div[1]/div/div/span[2]').click()
            driver.find_element_by_xpath('//*[@id="guide_page"]/div/div[2]/div/div/span[2]').click()
            driver.find_element_by_xpath('//*[@id="guide_page"]/div/div[3]/div/div/span[1]').click()
        except:
            pass
        try:
            # //*[@id="searchInput"]/div[1]/div/div[1]/input
            # /html/body/div[1]/div/div[3]/div/section[1]/div[1]/div/div[1]/div[3]/div/div[3]/div[1]/div/input
            input1=driver.find_element_by_xpath('//*[@id="searchInput"]/div[1]/div/div[1]/input')
            input2= driver.find_element_by_xpath('//*[@id="searchInput"]/div[3]/div/div[3]/div[1]/div/input')
            time.sleep(random.randrange(0,1))
            input1.clear()
            input2.clear()
            input1.send_keys(keyword1)
            # input2.send_keys(Keys.CONTROL, 'a')
            # input.send_keys('2014/01/01 - 2021/01/23')
            input2.send_keys(keyword2)
            time.sleep(random.randrange(0,1))
            driver.find_element_by_xpath('//*[@id="btn_search"]').click()
            driver.find_element_by_xpath('//*[@id="div_document"]/div[1]/div/div/div[1]/div[5]/button[3]').click()
        except:
            print('程序出错')
            continue
        time.sleep(random.randrange(0,1))
        try:

            filename=driver.find_element_by_xpath('//*[@id="div_document"]/div[1]/div/div/div[2]/div[1]/div[1]/div/a').text
            date=driver.find_element_by_xpath('//*[@id="div_document"]/div[1]/div/div/div[2]/div[1]/div[1]/div/div[3]/span').text
            url=driver.find_element_by_xpath('//*[@id="div_document"]/div[1]/div/div/div[2]/div[2]/div[1]/div/div[3]/a[1]').get_attribute('href')
        except:
            continue
        print(row, filename, date, url)
        if  filename and date and url:
            writer.writerow([keyword1,keyword2,filename,date,url])
            csvfile.flush()
            row += 1
            print(row,filename,date,url)

if __name__ == '__main__':


    usernames=[
        '16534222035',
        '16570929507',
        '16798644142',
        '16798644034',
    ]

    passwords=[
        'sg123123',
        '123456789',
        '123456789',
        '123456789',
    ]
    # 创建csv

    keywordlist = []
    filereader = open('股权.csv', 'r', encoding='gbk')
    lines = csv.reader(filereader)
    for line in lines:
        keywordlist.append((line[1],line[0]))

    task('0',usernames[0],passwords[0],keywordlist[0:500])



