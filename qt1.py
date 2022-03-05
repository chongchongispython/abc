from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import qtawesome
from PyQt5.QtWidgets import QLabel, QLineEdit, QFrame, QSplitter


class MainUi(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setFixedSize(600, 700)
        self.main_widget = QtWidgets.QWidget()  # 创建窗口主部件
        self.main_layout = QtWidgets.QGridLayout()  # 创建主部件的网格布局
        self.main_widget.setLayout(self.main_layout)  # 设置窗口主部件布局为网格布局

        self.left_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.left_widget.setObjectName('left_widget')
        self.left_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.left_widget.setLayout(self.left_layout)  # 设置左侧部件布局为网格

        self.right_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.right_widget.setObjectName('right_widget')
        self.right_layout = QtWidgets.QGridLayout()
        self.right_widget.setLayout(self.right_layout)  # 设置右侧部件布局为网格

        self.main_layout.addWidget(self.left_widget, 0, 0, 12, 2)  # 左侧部件在第0行第0列，占8行3列
        self.main_layout.addWidget(self.right_widget, 0, 2, 12, 10)  # 右侧部件在第0行第3列，占8行9列
        self.setCentralWidget(self.main_widget)  # 设置窗口主部件

        self.left_close = QtWidgets.QPushButton("")  # 关闭按钮
        self.left_visit = QtWidgets.QPushButton("")  # 空白按钮
        self.left_mini = QtWidgets.QPushButton("")  # 最小化按钮

        self.left_label_1 = QtWidgets.QPushButton("文件处理")
        self.left_label_1.setObjectName('left_label')
        self.left_label_2 = QtWidgets.QPushButton("热榜爬取")
        self.left_label_2.setObjectName('left_label')
        self.left_label_3 = QtWidgets.QPushButton("天气查询")
        self.left_label_3.setObjectName('left_label')
        self.left_label_4 = QtWidgets.QPushButton("邮件收发")
        self.left_label_4.setObjectName('left_label')

        self.left_button_1 = QtWidgets.QPushButton(qtawesome.icon('fa.file',color='white'), "文件重命名")
        self.left_button_1.setObjectName('left_button')
        self.left_button_2 = QtWidgets.QPushButton(qtawesome.icon('fa.exchange', color='white'), "文件格式转化")
        self.left_button_2.setObjectName('left_button')
        self.left_button_3 = QtWidgets.QPushButton(qtawesome.icon('fa.file-excel-o', color='white'), "Excel搜索")
        self.left_button_3.setObjectName('left_button')
        self.left_button_4 = QtWidgets.QPushButton(qtawesome.icon('fa.file-pdf-o', color='white'), "PDF加解密")
        self.left_button_4.setObjectName('left_button')
        self.left_button_5 = QtWidgets.QPushButton(qtawesome.icon('fa.files-o', color='white'), "PDf合并")
        self.left_button_5.setObjectName('left_button')

        self.left_button_6 = QtWidgets.QPushButton(qtawesome.icon('fa.bold', color='white'), "百度热榜")
        self.left_button_6.setObjectName('left_button')
        self.left_button_7 = QtWidgets.QPushButton(qtawesome.icon('fa.weibo', color='white'), "微博热榜")
        self.left_button_7.setObjectName('left_button')

        self.left_button_8 = QtWidgets.QPushButton(qtawesome.icon('fa.sun-o', color='white'), "天气信息展示")
        self.left_button_8.setObjectName('left_button')

        self.left_button_9 = QtWidgets.QPushButton(qtawesome.icon('fa.share', color='white'), "SMTP发送功能")
        self.left_button_9.setObjectName('left_button')
        self.left_button_10 = QtWidgets.QPushButton(qtawesome.icon('fa.envelope-o', color='white'), "POP3接收功能")
        self.left_button_10.setObjectName('left_button')

        self.left_xxx = QtWidgets.QPushButton(" ")

        self.left_layout.addWidget(self.left_mini, 0, 0, 1, 1)
        self.left_layout.addWidget(self.left_close, 0, 2, 1, 1)
        self.left_layout.addWidget(self.left_visit, 0, 1, 1, 1)

        self.left_layout.addWidget(self.left_label_1, 1, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_1, 2, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_2, 3, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_3, 4, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_4, 5, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_5, 6, 0, 1, 3)

        self.left_layout.addWidget(self.left_label_2, 7, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_6, 8, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_7, 9, 0, 1, 3)

        self.left_layout.addWidget(self.left_label_3, 10, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_8, 11, 0, 1, 3)

        self.left_layout.addWidget(self.left_label_4, 12, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_9, 13, 0, 1, 3)
        self.left_layout.addWidget(self.left_button_10, 14, 0, 1, 3)

        # 窗口控制按钮
        self.left_close.setFixedSize(15, 15)  # 设置关闭按钮的大小
        self.left_visit.setFixedSize(15, 15)  # 设置按钮大小
        self.left_mini.setFixedSize(15, 15)  # 设置最小化按钮大小

        self.main_layout.setSpacing(0)
        self.setupStyle()

        #左側按鈕綁帶事件
        self.left_button_1.clicked.connect(self.createFileRename)

    def createFileRename(self):
        # self.chose_file_1 = QtWidgets.QPushButton(qtawesome.icon('fa.file', color='black'), "選擇文件")
        # self.right_layout.addWidget(self.chose_file_1, 1, 3, 1, 3)

        self.top_widget = QtWidgets.QWidget()  # 创建左侧部件
        self.top_widget.setObjectName('left_widget')
        self.top_layout = QtWidgets.QGridLayout()  # 创建左侧部件的网格布局层
        self.top_widget.setLayout(self.top_layout)  # 设置左侧部件布局为网格

        self.bottom_widget = QtWidgets.QWidget()  # 创建右侧部件
        self.bottom_widget.setObjectName('right_widget')
        self.bottom_layout = QtWidgets.QGridLayout()
        self.bottom_widget.setLayout(self.bottom_layout)  # 设置右侧部件布局为网格

        self.right_layout.addWidget(self.top_widget, 0, 0,4,3)  # 左侧部件在第0行第0列，占8行3列
        self.right_layout.addWidget(self.bottom_widget, 4, 0,4,3)  # 右侧部件在第0行第3列，占8行9列
        #
        self.top_widget.setWindowTitle('文件重命名')
        # self.label0 = QLabel(self)
        # self.label0.setText('文件重命名')
        # self.top_layout.addWidget(self.label0, 1, 1,)

        # self.lineEdit0 = QLineEdit(self)
        # self.top_layout.addWidget(self.lineEdit0, 1, 2, )

        self.label1 = QLabel(self)
        self.label1.setText('文件名:')
        self.top_layout.addWidget(self.label1, 2, 0,)

        self.lineEdit1 = QLineEdit(self)
        self.top_layout.addWidget(self.lineEdit1, 2,1,)

        self.chose_file_button = QtWidgets.QPushButton(qtawesome.icon('fa.file', color='white'), "選擇文件")
        self.top_layout.addWidget(self.chose_file_button, 2, 2,)

        self.label2 = QLabel(self)
        self.label2.setText('重命名:')
        self.top_layout.addWidget(self.label2, 3, 0,)

        self.lineEdit2 = QLineEdit(self)
        self.top_layout.addWidget(self.lineEdit2, 3, 1,)

        self.confirm_button = QtWidgets.QPushButton(qtawesome.icon('fa.file', ), "确认")
        self.top_layout.addWidget(self.confirm_button, 4,1,)





        self.label1 = QLabel(self)
        self.label1.setText('文件名:')
        self.bottom_layout.addWidget(self.label1, 2, 0, )

        self.lineEdit1 = QLineEdit(self)
        self.bottom_layout.addWidget(self.lineEdit1, 2, 1, )

        self.chose_file_button = QtWidgets.QPushButton(qtawesome.icon('fa.file', color='white'), "選擇文件")
        self.bottom_layout.addWidget(self.chose_file_button, 2, 2, )

        self.label2 = QLabel(self)
        self.label2.setText('重命名:')
        self.bottom_layout.addWidget(self.label2, 3, 0, )

        self.lineEdit2 = QLineEdit(self)
        self.bottom_layout.addWidget(self.lineEdit2, 3, 1, )

        self.confirm_button = QtWidgets.QPushButton(qtawesome.icon('fa.file', ), "确认")
        self.bottom_layout.addWidget(self.confirm_button, 4, 1, )


    def setupStyle(self):
        self.left_close.setStyleSheet(
            '''QPushButton{background:#F76677;border-radius:5px;}QPushButton:hover{background:red;}''')
        self.left_visit.setStyleSheet(
            '''QPushButton{background:#F7D674;border-radius:5px;}QPushButton:hover{background:yellow;}''')
        self.left_mini.setStyleSheet(
            '''QPushButton{background:#6DDF6D;border-radius:5px;}QPushButton:hover{background:green;}''')

        # 左侧菜单按钮
        self.left_widget.setStyleSheet('''
                 QPushButton{border:none;color:white;}
                 QPushButton#left_label{
                   border:none;
                   border-bottom:1px solid white;
                   font-size:18px;
                   font-weight:700;
                   font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                 }
                 QPushButton#left_button:hover{border-left:4px solid red;font-weight:700;}
               ''')

        # 右侧背景
        self.right_widget.setStyleSheet('''
                 QWidget#right_widget{
                   color:#232C51;
                   background:white;
                   border-top:1px solid darkGray;
                   border-bottom:1px solid darkGray;
                   border-right:1px solid darkGray;
                   border-top-right-radius:10px;
                   border-bottom-right-radius:10px;
                 }
                 QLabel#right_lable{
                   border:none;
                   font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
                 }
               ''')
        # 设置窗口背景透明
        # self.setAttribute(QtCore.Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        # # 去除窗口边框
        # self.setWindowFlag(QtCore.Qt.FramelessWindowHint)  # 隐藏边框
        self.main_widget.setStyleSheet('''
               QWidget#left_widget{
               background:gray;
               border-top:1px solid white;
               border-bottom:1px solid white;
               border-left:1px solid white;
               border-top-left-radius:10px;
               border-bottom-left-radius:10px;
               }
               ''')

        self.right_widget.setStyleSheet(
            '''QLineEdit{
                border:1px solid gray;
                border-radius:10px;
                padding:2px 4px;
            }''')
def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = MainUi()
    gui.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()