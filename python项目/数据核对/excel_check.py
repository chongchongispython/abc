#coding=utf-8
import os
import xlwt,xlrd

def savedata():
    workbook = xlwt.Workbook(encoding='utf-8')  # 创建写入文本
    sheetwriter = workbook.add_sheet('no1')  # 创建表
    row1 = sheetwriter.row(0)  # 创建表头
    row1.write(0, '文件名')  # 写入表头
    row1.write(1, '核对结果')
    wrow = 1
    txtlist=os.listdir('文件夹')#获取所有文件
    for filename in txtlist:
        name=filename.split('.')[0]
        try:
            readbook = xlrd.open_workbook('文件夹/{}'.format(filename))  # 打开xlsx文件
        except:
            # print(excelname,'该文件不存在')
            return None
        sheet = readbook.sheet_by_index(0)  # 表序号
        result=''
        # print(sheet.cell(30, 2).value)
        nrows = sheet.nrows
        for row in range(0,nrows):
            # print(sheet.cell(row,0).value)
            if str(sheet.cell(row,0).value).strip()=='资产合计:':

                if sheet.cell(row, 2).value != sheet.cell(row, 5).value or sheet.cell(row, 2).value=='' or sheet.cell(row, 5).value=='':
                    result+= '年初不一致,'
                if sheet.cell(row, 1).value!=sheet.cell(row, 4).value or sheet.cell(row, 1).value=='' or sheet.cell(row, 4).value=='' :
                    result+= '期末不一致,'
                if result=='':
                    result='一致'
        sheetwriter.write(wrow, 0, name)  # 将数据写入单元格
        sheetwriter.write(wrow, 1, result)
        wrow += 1
    workbook.save('核对结果.xls')  # 保存数据表

if __name__ == '__main__':
    savedata()
