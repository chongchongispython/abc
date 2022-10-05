#coding=utf-8
import os
import re
from dbfread import DBF
import xlwt,xlrd
def compare(excelname,txtname1,txtname2):
    try:
        readbook=xlrd.open_workbook('文件/gz{}.xlsx'.format(excelname))#打开xlsx文件
    except:
        # print(excelname,'该文件不存在')
        return None
    sheet=readbook.sheet_by_index(0)  #表序号
    nrows = sheet.nrows  #行
    excel_a,excel_b,excel_c,excel_d=0,0,0,0
    for row in range(0,nrows):#获取表三个核对参数
        if sheet.cell(row,1).value=='10210402':
            excel_a=sheet.cell(row,4).value
        elif sheet.cell(row,1).value=='10310401':
            excel_b=sheet.cell(row,4).value
        elif sheet.cell(row,1).value=='10210418':
            excel_c= sheet.cell(row,4).value
        elif sheet.cell(row,1).value=='10310418':
            excel_d= sheet.cell(row,4).value
    # print(excel_a,excel_b,excel_c)
    result='一致'
    if txtname1 != '':
        try:
            with open('文件/{}'.format(txtname1),'r',encoding='gbk') as txtfile:#打开txt文件
                content=txtfile.read().strip().replace('\r','').replace('\n','')#处理文本空字符
        except:
            # print(excelname, '该文件不存在')
            result='不一致'
        # 正则匹配txt文本对应参数
        txt_a=float(re.findall('可用资金 Fund Avail\.：.*?(-?\d+\.\d+)',content)[0])
        txt_b=float(re.findall('保证金占用 Margin Occupied：.*?(-?\d+\.\d+)',content)[0])
        # 判断excel参数与txt是否一致
        if txt_a!=excel_a or txt_b!=excel_b:
            result='不一致'
    if txtname2!='':
        try:
            with open('文件/{}'.format(txtname2), 'r', encoding='gbk') as txtfile:  # 打开txt文件
                content = txtfile.read().strip().replace('\r', '').replace('\n', '')  # 处理文本空字符
        except:
            result='不一致'
        # 正则匹配txt文本对应参数
        txt_a = float(re.findall('可用资金 Fund Avail\.：.*?(-?\d+\.\d+)', content)[0])
        txt_b = float(re.findall('保证金占用 Margin Occupied：.*?(-?\d+\.\d+)', content)[0])
        # 判断excel参数与txt是否一致
        if txt_a != excel_c or  txt_b != excel_d :
            result='不一致'
    return result
def save():
    txtlist=os.listdir('文件')#获取所有文件
    for name in txtlist:
        if name.split('.')[1]=='dbf':#获取dbf文件
            dbftoxlsx('文件/{}'.format(name))#将dbf文件转成xlsx

    readbook = xlrd.open_workbook('产品关联信息.xls')
    sheet = readbook.sheet_by_index(0)  # 表序号
    nrows = sheet.nrows  # 行
    workbook = xlwt.Workbook(encoding='utf-8')# 创建写入文本
    sheetwriter = workbook.add_sheet('no1')#创建表
    row1 = sheetwriter.row(0)#创建表头
    row1.write(0, '组合代码')#写入表头
    row1.write(1, '产品名称')
    row1.write(2,'核对结果')
    wrow=1
    flag=''
    for row in range(1,nrows):
        if flag!=sheet.cell(row, 1).value:
            zuhedaima = sheet.cell(row, 1).value  # 获取单元格内容
            chanping = sheet.cell(row, 2).value
            txtname1,txtname2,result='','',''
            if sheet.cell(row, 1).value==sheet.cell(row+1,1).value:
                zijinzhanghao1 = sheet.cell(row, 3).value
                zijinzhanghao2 = sheet.cell(row+1, 3).value

                for txtname in txtlist:#遍历文件
                    if zijinzhanghao1 in txtname:#获取匹配文件名
                        txtname1=txtname
                    elif zijinzhanghao2 in txtname:#获取匹配文件名
                        txtname2 = txtname
                if zijinzhanghao1[0:1]==8:
                    result=compare(zuhedaima,txtname1, txtname2)
                else:
                    result=compare(zuhedaima, txtname2,txtname1)
            else:
                zijinzhanghao = sheet.cell(row, 3).value
                for txtname in txtlist:  # 遍历文件
                    if zijinzhanghao in txtname:  # 获取匹配文件名
                        txtname1 = txtname
                if zijinzhanghao[0:1] == 8:
                    result=compare(zuhedaima, txtname1, txtname2)
                else:
                    result=compare(zuhedaima, txtname2, txtname1)
            sheetwriter.write(wrow,0,zuhedaima)#将数据写入单元格
            sheetwriter.write(wrow,1,chanping)
            sheetwriter.write(wrow,2,result)
            wrow+=1
        flag=sheet.cell(row, 1).value
    workbook.save('result.xls')#保存数据表

def dbftoxlsx(dbf_filename):
    # dbf_filename = r'gz1961.dbf'
    xls_filename = dbf_filename.replace('dbf', 'xlsx')
    # 数据表文件名
    table = DBF(dbf_filename, encoding='GBK')
    all_sheet = []
    book = xlwt.Workbook()  # 新建一个excel
    sheet = book.add_sheet('all_sheet')  # 添加一个sheet页
    row = 0  # 控制行数
    write_row = 0
    sheet_list = []
    for record in table:
        col = 0
        if all_sheet == []:  # 这个为了控制只读取字段名一次
            sheet_dict = record.keys()
            # print(type(sheet_dict))         # <class 'odict_keys'>
            # sheet_list = list(set(sheet_dict))  # 将odict_keys转化为列表进行操作,这样xls的表头(第一行)会和原来的dbf顺序不一致
            sheet_list = list(sheet_dict)  # 将odict_keys转化为列表进行操作,这样操作顺序和原来的一样
            all_sheet = sheet_list
        if write_row == 0:  # 为了控制只将字段名写入一次
            col = 0
            for i in range(len(sheet_list)):
                sheet.write(row, col, sheet_list[i])
                col += 1
            col = 0
            row += 1
            write_row += 1
        for field in record:
            sheet.write(row, col, record[field])
            # print(field,'=',record[field],end='')
            col += 1
        row += 1
    book.save(xls_filename)  # 保存到指定目录下的指定文件

if __name__ == '__main__':
    save()
