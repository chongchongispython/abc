# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt11.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(655, 684)
        self.widget11 = QtWidgets.QWidget(Form)
        self.widget11.setEnabled(True)
        self.widget11.setGeometry(QtCore.QRect(60, 20, 511, 591))
        self.widget11.setMaximumSize(QtCore.QSize(16777208, 16777215))
        self.widget11.setToolTipDuration(-9)
        self.widget11.setInputMethodHints(QtCore.Qt.ImhNone)
        self.widget11.setObjectName("widget11")
        self.scrollArea_wt11_1 = QtWidgets.QScrollArea(self.widget11)
        self.scrollArea_wt11_1.setGeometry(QtCore.QRect(10, 50, 491, 31))
        self.scrollArea_wt11_1.setWidgetResizable(True)
        self.scrollArea_wt11_1.setObjectName("scrollArea_wt11_1")
        self.scrollAreaWidgetContents_w11_1 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_w11_1.setGeometry(QtCore.QRect(0, 0, 489, 29))
        self.scrollAreaWidgetContents_w11_1.setObjectName("scrollAreaWidgetContents_w11_1")
        self.label_wt11_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_w11_1)
        self.label_wt11_2.setGeometry(QtCore.QRect(10, 0, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_wt11_2.setFont(font)
        self.label_wt11_2.setObjectName("label_wt11_2")
        self.scrollArea_wt11_1.setWidget(self.scrollAreaWidgetContents_w11_1)
        self.groupBox_wt11 = QtWidgets.QGroupBox(self.widget11)
        self.groupBox_wt11.setGeometry(QtCore.QRect(10, 410, 491, 171))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(139, 139, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 139, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(139, 139, 139))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(249, 249, 249))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        self.groupBox_wt11.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_wt11.setFont(font)
        self.groupBox_wt11.setTitle("")
        self.groupBox_wt11.setObjectName("groupBox_wt11")
        self.label_wt11_4 = QtWidgets.QLabel(self.groupBox_wt11)
        self.label_wt11_4.setGeometry(QtCore.QRect(30, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_wt11_4.setFont(font)
        self.label_wt11_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_wt11_4.setObjectName("label_wt11_4")
        self.lineEdit_wt11_1 = QtWidgets.QLineEdit(self.groupBox_wt11)
        self.lineEdit_wt11_1.setGeometry(QtCore.QRect(100, 40, 121, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_wt11_1.setFont(font)
        self.lineEdit_wt11_1.setText("")
        self.lineEdit_wt11_1.setObjectName("lineEdit_wt11_1")
        self.lineEdit_wt11_2 = QtWidgets.QLineEdit(self.groupBox_wt11)
        self.lineEdit_wt11_2.setGeometry(QtCore.QRect(310, 40, 131, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_wt11_2.setFont(font)
        self.lineEdit_wt11_2.setText("")
        self.lineEdit_wt11_2.setObjectName("lineEdit_wt11_2")
        self.label_wt11_5 = QtWidgets.QLabel(self.groupBox_wt11)
        self.label_wt11_5.setGeometry(QtCore.QRect(240, 40, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_wt11_5.setFont(font)
        self.label_wt11_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_wt11_5.setObjectName("label_wt11_5")
        self.label_wt11_6 = QtWidgets.QLabel(self.groupBox_wt11)
        self.label_wt11_6.setGeometry(QtCore.QRect(40, 100, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_wt11_6.setFont(font)
        self.label_wt11_6.setAlignment(QtCore.Qt.AlignCenter)
        self.label_wt11_6.setObjectName("label_wt11_6")
        self.comboBox_wt11 = QtWidgets.QComboBox(self.groupBox_wt11)
        self.comboBox_wt11.setGeometry(QtCore.QRect(120, 100, 221, 26))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_wt11.setFont(font)
        self.comboBox_wt11.setObjectName("comboBox_wt11")
        self.pushButton_wt11_1 = QtWidgets.QPushButton(self.groupBox_wt11)
        self.pushButton_wt11_1.setGeometry(QtCore.QRect(360, 90, 81, 41))
        self.pushButton_wt11_1.setObjectName("pushButton_wt11_1")
        self.label_wt11_1 = QtWidgets.QLabel(self.widget11)
        self.label_wt11_1.setEnabled(True)
        self.label_wt11_1.setGeometry(QtCore.QRect(220, 10, 81, 28))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_wt11_1.setFont(font)
        self.label_wt11_1.setObjectName("label_wt11_1")
        self.textEdit_w10_1 = QtWidgets.QTextEdit(self.widget11)
        self.textEdit_w10_1.setEnabled(True)
        self.textEdit_w10_1.setGeometry(QtCore.QRect(10, 80, 491, 281))
        self.textEdit_w10_1.setObjectName("textEdit_w10_1")
        self.scrollArea_wt11_2 = QtWidgets.QScrollArea(self.widget11)
        self.scrollArea_wt11_2.setGeometry(QtCore.QRect(10, 380, 491, 31))
        self.scrollArea_wt11_2.setWidgetResizable(True)
        self.scrollArea_wt11_2.setObjectName("scrollArea_wt11_2")
        self.scrollAreaWidgetContents_w11_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_w11_2.setGeometry(QtCore.QRect(0, 0, 489, 29))
        self.scrollAreaWidgetContents_w11_2.setObjectName("scrollAreaWidgetContents_w11_2")
        self.label_wt11_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_w11_2)
        self.label_wt11_3.setGeometry(QtCore.QRect(10, 0, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_wt11_3.setFont(font)
        self.label_wt11_3.setObjectName("label_wt11_3")
        self.scrollArea_wt11_2.setWidget(self.scrollAreaWidgetContents_w11_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_wt11_2.setText(_translate("Form", "控制台"))
        self.label_wt11_4.setText(_translate("Form", "邮箱:"))
        self.label_wt11_5.setText(_translate("Form", "授权码:"))
        self.label_wt11_6.setText(_translate("Form", "选择邮件:"))
        self.pushButton_wt11_1.setText(_translate("Form", "刷新"))
        self.label_wt11_1.setText(_translate("Form", "接收邮件"))
        self.label_wt11_3.setText(_translate("Form", "功能区"))