# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'wt2.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(645, 726)
        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setEnabled(True)
        self.widget2.setGeometry(QtCore.QRect(90, 40, 511, 591))
        self.widget2.setMaximumSize(QtCore.QSize(16777208, 16777215))
        self.widget2.setToolTipDuration(-9)
        self.widget2.setInputMethodHints(QtCore.Qt.ImhNone)
        self.widget2.setObjectName("widget2")
        self.scrollArea_wt2_1 = QtWidgets.QScrollArea(self.widget2)
        self.scrollArea_wt2_1.setGeometry(QtCore.QRect(10, 50, 491, 31))
        self.scrollArea_wt2_1.setWidgetResizable(True)
        self.scrollArea_wt2_1.setObjectName("scrollArea_wt2_1")
        self.scrollAreaWidgetContents_w2_1 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_w2_1.setGeometry(QtCore.QRect(0, 0, 489, 29))
        self.scrollAreaWidgetContents_w2_1.setObjectName("scrollAreaWidgetContents_w2_1")
        self.label_wt2_2 = QtWidgets.QLabel(self.scrollAreaWidgetContents_w2_1)
        self.label_wt2_2.setGeometry(QtCore.QRect(10, 0, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_wt2_2.setFont(font)
        self.label_wt2_2.setObjectName("label_wt2_2")
        self.scrollArea_wt2_1.setWidget(self.scrollAreaWidgetContents_w2_1)
        self.groupBox_wt2 = QtWidgets.QGroupBox(self.widget2)
        self.groupBox_wt2.setGeometry(QtCore.QRect(10, 450, 491, 131))
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
        self.groupBox_wt2.setPalette(palette)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_wt2.setFont(font)
        self.groupBox_wt2.setTitle("")
        self.groupBox_wt2.setObjectName("groupBox_wt2")
        self.label_wt2_4 = QtWidgets.QLabel(self.groupBox_wt2)
        self.label_wt2_4.setGeometry(QtCore.QRect(20, 30, 81, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_wt2_4.setFont(font)
        self.label_wt2_4.setAlignment(QtCore.Qt.AlignCenter)
        self.label_wt2_4.setObjectName("label_wt2_4")
        self.lineEdit_wt2_1 = QtWidgets.QLineEdit(self.groupBox_wt2)
        self.lineEdit_wt2_1.setGeometry(QtCore.QRect(100, 30, 181, 31))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.lineEdit_wt2_1.setFont(font)
        self.lineEdit_wt2_1.setObjectName("lineEdit_wt2_1")
        self.pushButton_wt2_1 = QtWidgets.QPushButton(self.groupBox_wt2)
        self.pushButton_wt2_1.setGeometry(QtCore.QRect(290, 30, 71, 41))
        self.pushButton_wt2_1.setCheckable(False)
        self.pushButton_wt2_1.setObjectName("pushButton_wt2_1")
        self.label_wt2_5 = QtWidgets.QLabel(self.groupBox_wt2)
        self.label_wt2_5.setGeometry(QtCore.QRect(10, 70, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_wt2_5.setFont(font)
        self.label_wt2_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_wt2_5.setObjectName("label_wt2_5")
        self.pushButton_wt2_2 = QtWidgets.QPushButton(self.groupBox_wt2)
        self.pushButton_wt2_2.setGeometry(QtCore.QRect(290, 70, 71, 41))
        self.pushButton_wt2_2.setCheckable(False)
        self.pushButton_wt2_2.setObjectName("pushButton_wt2_2")
        self.comboBox_wt2 = QtWidgets.QComboBox(self.groupBox_wt2)
        self.comboBox_wt2.setGeometry(QtCore.QRect(100, 60, 181, 53))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(False)
        font.setWeight(50)
        self.comboBox_wt2.setFont(font)
        self.comboBox_wt2.setObjectName("comboBox_wt2")
        self.comboBox_wt2.addItem("")
        self.comboBox_wt2.addItem("")
        self.comboBox_wt2.addItem("")
        self.comboBox_wt2.addItem("")
        self.label_wt2_1 = QtWidgets.QLabel(self.widget2)
        self.label_wt2_1.setEnabled(True)
        self.label_wt2_1.setGeometry(QtCore.QRect(210, 10, 121, 28))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_wt2_1.setFont(font)
        self.label_wt2_1.setObjectName("label_wt2_1")
        self.textEdit_w2_1 = QtWidgets.QTextEdit(self.widget2)
        self.textEdit_w2_1.setEnabled(True)
        self.textEdit_w2_1.setGeometry(QtCore.QRect(10, 80, 491, 321))
        self.textEdit_w2_1.setObjectName("textEdit_w2_1")
        self.scrollArea_wt2_2 = QtWidgets.QScrollArea(self.widget2)
        self.scrollArea_wt2_2.setGeometry(QtCore.QRect(10, 420, 491, 31))
        self.scrollArea_wt2_2.setWidgetResizable(True)
        self.scrollArea_wt2_2.setObjectName("scrollArea_wt2_2")
        self.scrollAreaWidgetContents_w2_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_w2_2.setGeometry(QtCore.QRect(0, 0, 489, 29))
        self.scrollAreaWidgetContents_w2_2.setObjectName("scrollAreaWidgetContents_w2_2")
        self.label_wt2_3 = QtWidgets.QLabel(self.scrollAreaWidgetContents_w2_2)
        self.label_wt2_3.setGeometry(QtCore.QRect(10, 0, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_wt2_3.setFont(font)
        self.label_wt2_3.setObjectName("label_wt2_3")
        self.scrollArea_wt2_2.setWidget(self.scrollAreaWidgetContents_w2_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label_wt2_2.setText(_translate("Form", "?????????"))
        self.label_wt2_4.setText(_translate("Form", "????????????:"))
        self.pushButton_wt2_1.setText(_translate("Form", "??????"))
        self.label_wt2_5.setText(_translate("Form", "????????????:"))
        self.pushButton_wt2_2.setText(_translate("Form", "??????"))
        self.comboBox_wt2.setItemText(0, _translate("Form", "xls"))
        self.comboBox_wt2.setItemText(1, _translate("Form", "xlsx"))
        self.comboBox_wt2.setItemText(2, _translate("Form", "doc"))
        self.comboBox_wt2.setItemText(3, _translate("Form", "docx"))
        self.label_wt2_1.setText(_translate("Form", "??????????????????"))
        self.label_wt2_3.setText(_translate("Form", "?????????"))
