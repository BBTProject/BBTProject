# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BaseWidget.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_BaseWidget(object):
    def setupUi(self, BaseWidget):
        BaseWidget.setObjectName(_fromUtf8("BaseWidget"))
        BaseWidget.setEnabled(True)
        BaseWidget.resize(600, 400)
        BaseWidget.setMaximumSize(QtCore.QSize(600, 400))
        BaseWidget.setToolTip(_fromUtf8(""))
        BaseWidget.setStyleSheet(_fromUtf8("#BaseWidget{background-color: rgb(85, 170, 255);\n"
"border-radius:10px;}"))
        self.FileWidgetButton = QtGui.QPushButton(BaseWidget)
        self.FileWidgetButton.setGeometry(QtCore.QRect(0, 0, 120, 100))
        self.FileWidgetButton.setAutoFillBackground(False)
        self.FileWidgetButton.setStyleSheet(_fromUtf8("#FileWidgetButton{background-color:#2C3E50;border:none;color:#ffffff;font-size:20px;border-top-left-radius:10px;}\n"
"#FileWidgetButton:hover{background-color:#333333;}"))
        self.FileWidgetButton.setObjectName(_fromUtf8("FileWidgetButton"))
        self.SQLWidgetButton = QtGui.QPushButton(BaseWidget)
        self.SQLWidgetButton.setGeometry(QtCore.QRect(0, 100, 120, 100))
        self.SQLWidgetButton.setAutoFillBackground(False)
        self.SQLWidgetButton.setStyleSheet(_fromUtf8("#SQLWidgetButton{background-color:#2C3E50;border:none;color:#ffffff;font-size:20px;}\n"
"#SQLWidgetButton:hover{background-color:#333333;}"))
        self.SQLWidgetButton.setObjectName(_fromUtf8("SQLWidgetButton"))
        self.HelpWidgetButton = QtGui.QPushButton(BaseWidget)
        self.HelpWidgetButton.setGeometry(QtCore.QRect(0, 200, 120, 100))
        self.HelpWidgetButton.setAutoFillBackground(False)
        self.HelpWidgetButton.setStyleSheet(_fromUtf8("#HelpWidgetButton{background-color:#2C3E50;border:none;color:#ffffff;font-size:20px;}\n"
"#HelpWidgetButton:hover{background-color:#333333;}"))
        self.HelpWidgetButton.setObjectName(_fromUtf8("HelpWidgetButton"))
        self.AboutWidgetButton = QtGui.QPushButton(BaseWidget)
        self.AboutWidgetButton.setGeometry(QtCore.QRect(0, 300, 120, 100))
        self.AboutWidgetButton.setAutoFillBackground(False)
        self.AboutWidgetButton.setStyleSheet(_fromUtf8("#AboutWidgetButton{background-color:#2C3E50;border:none;color:#ffffff;font-size:20px;border-bottom-left-radius:10px;}\n"
"#AboutWidgetButton:hover{background-color:#333333;}"))
        self.AboutWidgetButton.setObjectName(_fromUtf8("AboutWidgetButton"))
        self.CloseButton = QtGui.QPushButton(BaseWidget)
        self.CloseButton.setGeometry(QtCore.QRect(560, 0, 40, 25))
        self.CloseButton.setStyleSheet(_fromUtf8("#CloseButton{background-color: rgb(85, 170, 255);border-radius:10px;color:#ffffff;font-size:10px;\n"
"background-image: url(:/images/images/CloseButton.png);}\n"
"#CloseButton:hover{background-color:#333333;}"))
        self.CloseButton.setText(_fromUtf8(""))
        self.CloseButton.setObjectName(_fromUtf8("CloseButton"))
        self.MinButton = QtGui.QPushButton(BaseWidget)
        self.MinButton.setGeometry(QtCore.QRect(520, 0, 40, 25))
        self.MinButton.setStatusTip(_fromUtf8(""))
        self.MinButton.setStyleSheet(_fromUtf8("#MinButton{background-color: rgb(85, 170, 255);color:#ffffff;font-size:10px;border:none;\n"
"background-image: url(:/images/images/MinButton.png);\n"
"border-radius:10px;}\n"
"#MinButton:hover{background-color:#333333;}"))
        self.MinButton.setText(_fromUtf8(""))
        self.MinButton.setObjectName(_fromUtf8("MinButton"))
        self.FileWidget = QtGui.QWidget(BaseWidget)
        self.FileWidget.setGeometry(QtCore.QRect(120, 25, 480, 350))
        self.FileWidget.setObjectName(_fromUtf8("FileWidget"))
        self.FiletypesLabel = QtGui.QLabel(self.FileWidget)
        self.FiletypesLabel.setGeometry(QtCore.QRect(35, 60, 81, 20))
        self.FiletypesLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);  \n"
"font-size: 15px;\n"
"text-align: center;"))
        self.FiletypesLabel.setObjectName(_fromUtf8("FiletypesLabel"))
        self.FiletypesLineEdit = QtGui.QLineEdit(self.FileWidget)
        self.FiletypesLineEdit.setGeometry(QtCore.QRect(180, 55, 281, 25))
        self.FiletypesLineEdit.setStyleSheet(_fromUtf8("border-radius: 10px;"))
        self.FiletypesLineEdit.setObjectName(_fromUtf8("FiletypesLineEdit"))
        self.UserInfosLineEdit = QtGui.QLineEdit(self.FileWidget)
        self.UserInfosLineEdit.setGeometry(QtCore.QRect(180, 95, 281, 25))
        self.UserInfosLineEdit.setStyleSheet(_fromUtf8("border-radius: 10px;"))
        self.UserInfosLineEdit.setObjectName(_fromUtf8("UserInfosLineEdit"))
        self.UserInfomationsLabel = QtGui.QLabel(self.FileWidget)
        self.UserInfomationsLabel.setGeometry(QtCore.QRect(35, 100, 121, 20))
        self.UserInfomationsLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font-size: 15px;\n"
"text-align: center;"))
        self.UserInfomationsLabel.setObjectName(_fromUtf8("UserInfomationsLabel"))
        self.StartUrlLabel = QtGui.QLabel(self.FileWidget)
        self.StartUrlLabel.setGeometry(QtCore.QRect(35, 140, 81, 20))
        self.StartUrlLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font-size: 15px;\n"
"text-align: center;"))
        self.StartUrlLabel.setObjectName(_fromUtf8("StartUrlLabel"))
        self.FilterKeyWordsLabel = QtGui.QLabel(self.FileWidget)
        self.FilterKeyWordsLabel.setGeometry(QtCore.QRect(35, 180, 111, 20))
        self.FilterKeyWordsLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"font-size: 15px;\n"
"text-align: center;"))
        self.FilterKeyWordsLabel.setObjectName(_fromUtf8("FilterKeyWordsLabel"))
        self.FilterKeyWordLineEdit = QtGui.QLineEdit(self.FileWidget)
        self.FilterKeyWordLineEdit.setGeometry(QtCore.QRect(180, 175, 281, 25))
        self.FilterKeyWordLineEdit.setStyleSheet(_fromUtf8("border-radius: 10px;"))
        self.FilterKeyWordLineEdit.setObjectName(_fromUtf8("FilterKeyWordLineEdit"))
        self.StartUrlLineEdit = QtGui.QLineEdit(self.FileWidget)
        self.StartUrlLineEdit.setGeometry(QtCore.QRect(180, 135, 281, 25))
        self.StartUrlLineEdit.setStyleSheet(_fromUtf8("border-radius: 10px;"))
        self.StartUrlLineEdit.setObjectName(_fromUtf8("StartUrlLineEdit"))
        self.RunButton = QtGui.QPushButton(self.FileWidget)
        self.RunButton.setGeometry(QtCore.QRect(90, 260, 120, 50))
        self.RunButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.RunButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color:rgb(70, 150, 255);\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"    font-family: Verdana;\n"
"    font-size: 15px;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"    background-color:#2C3E50;\n"
"    text-align: right;\n"
"    padding-right: 30px;\n"
"    font-weight:100\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-image: url(:/images/images/RunButtonHover.png);\n"
"    background-repeat:no-repeat;\n"
"    background-position: center left;\n"
"}\n"
"QPushButton:pressed, QPushButton:checked\n"
"{\n"
"    background-image: url(:/images/images/RunButtonPress.png);\n"
"    background-repeat:no-repeat;\n"
"    background-position: center left;\n"
"}"))
        self.RunButton.setObjectName(_fromUtf8("RunButton"))
        self.StopButton = QtGui.QPushButton(self.FileWidget)
        self.StopButton.setGeometry(QtCore.QRect(250, 260, 120, 50))
        self.StopButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"    color: rgb(255, 255, 255);\n"
"    background-color: rgb(70, 150, 255);\n"
"    border:none;\n"
"    border-radius:10px;\n"
"    padding:2px 4px;\n"
"    font-family: Verdana;\n"
"    font-size: 15px;\n"
"    text-align: center;\n"
"}\n"
"QPushButton:hover, QPushButton:pressed , QPushButton:checked\n"
"{\n"
"    background-color:#2C3E50;\n"
"    text-align: right;\n"
"    padding-right: 30px;\n"
"    font-weight:100\n"
"}\n"
"QPushButton:hover\n"
"{\n"
"    background-image: url(:/images/images/StopButtonHover.png);\n"
"    background-repeat:no-repeat;\n"
"    background-position: center left;\n"
"}\n"
"QPushButton:pressed, QPushButton:checked\n"
"{\n"
"    background-image: url(:/images/images/StopButtonPress.png);\n"
"    background-repeat:no-repeat;\n"
"    background-position: center left;\n"
"}"))
        self.StopButton.setObjectName(_fromUtf8("StopButton"))
        self.OutputButton = QtGui.QPushButton(BaseWidget)
        self.OutputButton.setGeometry(QtCore.QRect(550, 373, 50, 25))
        self.OutputButton.setStyleSheet(_fromUtf8("QPushButton{\n"
"    border-radius:10px;\n"
"    color: rgb(255, 255, 255);\n"
"    border:none;\n"
"    background-color:rgb(70, 150, 255);}\n"
"QPushButton:hover{\n"
"background-color: #2C3E50;}"))
        self.OutputButton.setObjectName(_fromUtf8("OutputButton"))

        self.retranslateUi(BaseWidget)
        QtCore.QObject.connect(self.CloseButton, QtCore.SIGNAL(_fromUtf8("clicked()")), BaseWidget.close)
        QtCore.QObject.connect(self.MinButton, QtCore.SIGNAL(_fromUtf8("clicked()")), BaseWidget.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(BaseWidget)

    def retranslateUi(self, BaseWidget):
        BaseWidget.setWindowTitle(_translate("BaseWidget", "Form", None))
        self.FileWidgetButton.setText(_translate("BaseWidget", "File", None))
        self.SQLWidgetButton.setText(_translate("BaseWidget", "SQL", None))
        self.HelpWidgetButton.setText(_translate("BaseWidget", "Help", None))
        self.AboutWidgetButton.setText(_translate("BaseWidget", "About", None))
        self.CloseButton.setToolTip(_translate("BaseWidget", "close", None))
        self.MinButton.setToolTip(_translate("BaseWidget", "minimize", None))
        self.FiletypesLabel.setText(_translate("BaseWidget", "Filetypes", None))
        self.UserInfomationsLabel.setText(_translate("BaseWidget", "UserInfomations", None))
        self.StartUrlLabel.setText(_translate("BaseWidget", "StartUrl", None))
        self.FilterKeyWordsLabel.setText(_translate("BaseWidget", "FilterKeyWords", None))
        self.RunButton.setText(_translate("BaseWidget", "Run", None))
        self.StopButton.setText(_translate("BaseWidget", "Stop", None))
        self.OutputButton.setText(_translate("BaseWidget", "Output", None))

import res_rc
