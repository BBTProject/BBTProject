# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'LoginInfoWidget.ui'
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

class Ui_LoginInfoWidget(object):
    def setupUi(self, LoginInfoWidget):
        LoginInfoWidget.setObjectName(_fromUtf8("LoginInfoWidget"))
        LoginInfoWidget.resize(310, 370)
        LoginInfoWidget.setMaximumSize(QtCore.QSize(310, 370))
        LoginInfoWidget.setStyleSheet(_fromUtf8("#LoginInfoWidget{background-color: rgb(85, 170, 255);\n"
"border-style: inset;\n"
"border-width:1px;border-color:#2C3E50;}"))
        self.tableWidget = QtGui.QTableWidget(LoginInfoWidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 50, 291, 281))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)
        self.label = QtGui.QLabel(LoginInfoWidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 141, 16))
        self.label.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);  \n"
"font-size: 15px;\n"
"text-align: center;"))
        self.label.setObjectName(_fromUtf8("label"))
        self.CloseButton = QtGui.QPushButton(LoginInfoWidget)
        self.CloseButton.setGeometry(QtCore.QRect(280, 0, 25, 25))
        self.CloseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CloseButton.setStyleSheet(_fromUtf8("#CloseButton{border-radius:10px;color:#ffffff;font-size:10px;background-repeat:no-repeat;\n"
"background-image: url(:/images/images/CloseButton.png);}\n"
"#CloseButton:hover{\n"
"background-image: url(:/images/images/CloseButtonPress.png);}"))
        self.CloseButton.setText(_fromUtf8(""))
        self.CloseButton.setObjectName(_fromUtf8("CloseButton"))
        self.MinButton = QtGui.QPushButton(LoginInfoWidget)
        self.MinButton.setGeometry(QtCore.QRect(255, 0, 25, 25))
        self.MinButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MinButton.setStatusTip(_fromUtf8(""))
        self.MinButton.setStyleSheet(_fromUtf8("#MinButton{color:#ffffff;font-size:10px;border:none;\n"
"background-image: url(:/images/images/MinButton.png);background-repeat:no-repeat;\n"
"border-radius:10px;}\n"
"#MinButton:hover{background-image:url(:/images/images/MinButtonPress);}"))
        self.MinButton.setText(_fromUtf8(""))
        self.MinButton.setObjectName(_fromUtf8("MinButton"))
        self.OkButton = QtGui.QPushButton(LoginInfoWidget)
        self.OkButton.setGeometry(QtCore.QRect(174, 340, 60, 25))
        self.OkButton.setObjectName(_fromUtf8("OkButton"))
        self.CancelButton = QtGui.QPushButton(LoginInfoWidget)
        self.CancelButton.setGeometry(QtCore.QRect(240, 340, 60, 25))
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))

        self.retranslateUi(LoginInfoWidget)
        QtCore.QObject.connect(self.MinButton, QtCore.SIGNAL(_fromUtf8("clicked()")), LoginInfoWidget.showMinimized)
        QtCore.QObject.connect(self.CloseButton, QtCore.SIGNAL(_fromUtf8("clicked()")), LoginInfoWidget.close)
        QtCore.QMetaObject.connectSlotsByName(LoginInfoWidget)

    def retranslateUi(self, LoginInfoWidget):
        LoginInfoWidget.setWindowTitle(_translate("LoginInfoWidget", "Form", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("LoginInfoWidget", "Account", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("LoginInfoWidget", "Password", None))
        self.label.setText(_translate("LoginInfoWidget", "Login Infomation:", None))
        self.CloseButton.setToolTip(_translate("LoginInfoWidget", "close", None))
        self.MinButton.setToolTip(_translate("LoginInfoWidget", "minimize", None))
        self.OkButton.setText(_translate("LoginInfoWidget", "OK", None))
        self.CancelButton.setText(_translate("LoginInfoWidget", "Cancel", None))

import res_rc
