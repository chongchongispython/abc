import pandas as pd
import openpyxl
import os
# excel 数据样式设置类
from openpyxl.styles import Font, PatternFill, Border, Side, Alignment
class Report:
    def __init__(self):
        self.empty_template='模版/空模版'
        self.formula_template='模版/模版公式'
        self.sheets_name={
            'D27':'D27',
            'D37': 'D37',
            'D74': 'D74',
        }
        self.c_file_name=''
        self.a_file_name=''

    def load_excel(self):
        self.c_file_name =os.listdir('中国机')[0]
        self.a_file_name =os.listdir('美国机')[0]
        self.c_D27 = pd.read_excel('中国机/'+self.c_file_name, sheet_name=self.sheets_name['D27'], header=None)  # 读取Excel文档
        self.c_D37= pd.read_excel('中国机/' + self.c_file_name, sheet_name=self.sheets_name['D37'], header=None)
        self.c_D74 = pd.read_excel('中国机/' + self.c_file_name, sheet_name=self.sheets_name['D74'], header=None)
        self.a_D27 = pd.read_excel('美国机/' + self.a_file_name, sheet_name=self.sheets_name['D27'],header=None)
        self.a_D37 = pd.read_excel('美国机/' + self.a_file_name, sheet_name=self.sheets_name['D37'], header=None)
        self.a_D74 = pd.read_excel('美国机/' + self.a_file_name, sheet_name=self.sheets_name['D74'], header=None)
        # 获取最大行，最大列
        rows = self.a_D27.shape[0]
        cols = self.a_D27.columns.size
        # 取值
        print(self.a_D27.iloc[0])  # 特定单元格



if __name__ == "__main__":
    r=Report()
    r.load_excel()
