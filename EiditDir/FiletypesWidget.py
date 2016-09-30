# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'FiletypesWidget.ui'
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

class Ui_FiletypesWidget(object):
    def setupUi(self, FiletypesWidget):
        FiletypesWidget.setObjectName(_fromUtf8("FiletypesWidget"))
        FiletypesWidget.resize(280, 325)
        FiletypesWidget.setMaximumSize(QtCore.QSize(280, 325))
        FiletypesWidget.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        FiletypesWidget.setStyleSheet(_fromUtf8("#FiletypesWidget{background-color: rgb(85, 170, 255);\n"
"border-style: inset;\n"
"border-width:1px;border-color:#2C3E50;}"))
        self.CloseButton = QtGui.QPushButton(FiletypesWidget)
        self.CloseButton.setGeometry(QtCore.QRect(250, 0, 25, 25))
        self.CloseButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.CloseButton.setStyleSheet(_fromUtf8("#CloseButton{border-radius:10px;color:#ffffff;font-size:10px;background-repeat:no-repeat;\n"
"background-image: url(:/images/images/CloseButton.png);}\n"
"#CloseButton:hover{\n"
"background-image: url(:/images/images/CloseButtonPress.png);}"))
        self.CloseButton.setText(_fromUtf8(""))
        self.CloseButton.setObjectName(_fromUtf8("CloseButton"))
        self.MinButton = QtGui.QPushButton(FiletypesWidget)
        self.MinButton.setGeometry(QtCore.QRect(220, 0, 25, 25))
        self.MinButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.MinButton.setStatusTip(_fromUtf8(""))
        self.MinButton.setStyleSheet(_fromUtf8("#MinButton{color:#ffffff;font-size:10px;border:none;\n"
"background-image: url(:/images/images/MinButton.png);background-repeat:no-repeat;\n"
"border-radius:10px;}\n"
"#MinButton:hover{background-image:url(:/images/images/MinButtonPress);}"))
        self.MinButton.setText(_fromUtf8(""))
        self.MinButton.setObjectName(_fromUtf8("MinButton"))
        self.TitleLabel = QtGui.QLabel(FiletypesWidget)
        self.TitleLabel.setGeometry(QtCore.QRect(10, 20, 151, 21))
        self.TitleLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);  \n"
"font-size: 15px;\n"
"text-align: center;"))
        self.TitleLabel.setObjectName(_fromUtf8("TitleLabel"))
        self.DocumentsLabel = QtGui.QLabel(FiletypesWidget)
        self.DocumentsLabel.setGeometry(QtCore.QRect(30, 60, 81, 21))
        self.DocumentsLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);  \n"
"font-size: 15px;\n"
"text-align: center;"))
        self.DocumentsLabel.setObjectName(_fromUtf8("DocumentsLabel"))
        self.DocCheckBox = QtGui.QCheckBox(FiletypesWidget)
        self.DocCheckBox.setGeometry(QtCore.QRect(50, 90, 101, 21))
        self.DocCheckBox.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);  \n"
"font-size: 15px;\n"
"text-align: center;"))
        self.DocCheckBox.setObjectName(_fromUtf8("DocCheckBox"))
        self.XlsCheckBox = QtGui.QCheckBox(FiletypesWidget)
        self.XlsCheckBox.setGeometry(QtCore.QRect(160, 90, 71, 21))
        self.XlsCheckBox.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);  \n"
"font-size: 15px;\n"
"text-align: center;"))
        self.XlsCheckBox.setObjectName(_fromUtf8("XlsCheckBox"))
        self.PPTCheckBox = QtGui.QCheckBox(FiletypesWidget)
        self.PPTCheckBox.setGeometry(QtCore.QRect(160, 120, 101, 21))
        self.PPTCheckBox.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);  \n"
"font-size: 15px;\n"
"text-align: center;"))
        self.PPTCheckBox.setObjectName(_fromUtf8("PPTCheckBox"))
        self.PdfCheckBox = QtGui.QCheckBox(FiletypesWidget)
        self.PdfCheckBox.setGeometry(QtCore.QRect(50, 120, 71, 21))
        self.PdfCheckBox.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);  \n"
"font-size: 15px;\n"
"text-align: center;"))
        self.PdfCheckBox.setObjectName(_fromUtf8("PdfCheckBox"))
        self.GraphicsLabel = QtGui.QLabel(FiletypesWidget)
        self.GraphicsLabel.setGeometry(QtCore.QRect(30, 150, 81, 21))
        self.GraphicsLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);  \n"
"font-size: 15px;\n"
"text-align: center;"))
        self.GraphicsLabel.setObjectName(_fromUtf8("GraphicsLabel"))
        self.JpgCheckBox = QtGui.QCheckBox(FiletypesWidget)
        self.JpgCheckBox.setGeometry(QtCore.QRect(50, 180, 101, 21))
        self.JpgCheckBox.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);  \n"
"font-size: 15px;\n"
"text-align: center;"))
        self.JpgCheckBox.setObjectName(_fromUtf8("JpgCheckBox"))
        self.PngCheckBox = QtGui.QCheckBox(FiletypesWidget)
        self.PngCheckBox.setGeometry(QtCore.QRect(160, 180, 71, 21))
        self.PngCheckBox.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);  \n"
"font-size: 15px;\n"
"text-align: center;"))
        self.PngCheckBox.setObjectName(_fromUtf8("PngCheckBox"))
        self.OtherLabel = QtGui.QLabel(FiletypesWidget)
        self.OtherLabel.setGeometry(QtCore.QRect(30, 220, 81, 21))
        self.OtherLabel.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);  \n"
"font-size: 15px;\n"
"text-align: center;"))
        self.OtherLabel.setObjectName(_fromUtf8("OtherLabel"))
        self.OtherLineEdit = QtGui.QLineEdit(FiletypesWidget)
        self.OtherLineEdit.setGeometry(QtCore.QRect(50, 250, 221, 21))
        self.OtherLineEdit.setStyleSheet(_fromUtf8("font-size:13px;border-radius: 10px;"))
        self.OtherLineEdit.setObjectName(_fromUtf8("OtherLineEdit"))
        self.CancelButton = QtGui.QPushButton(FiletypesWidget)
        self.CancelButton.setGeometry(QtCore.QRect(216, 290, 60, 25))
        self.CancelButton.setObjectName(_fromUtf8("CancelButton"))
        self.OkButton = QtGui.QPushButton(FiletypesWidget)
        self.OkButton.setGeometry(QtCore.QRect(150, 290, 60, 25))
        self.OkButton.setObjectName(_fromUtf8("OkButton"))
        self.label = QtGui.QLabel(FiletypesWidget)
        self.label.setGeometry(QtCore.QRect(60, 270, 171, 16))
        self.label.setObjectName(_fromUtf8("label"))

        self.retranslateUi(FiletypesWidget)
        QtCore.QObject.connect(self.MinButton, QtCore.SIGNAL(_fromUtf8("clicked()")), FiletypesWidget.showMinimized)
        QtCore.QObject.connect(self.CloseButton, QtCore.SIGNAL(_fromUtf8("clicked()")), FiletypesWidget.close)
        QtCore.QMetaObject.connectSlotsByName(FiletypesWidget)

    def retranslateUi(self, FiletypesWidget):
        FiletypesWidget.setWindowTitle(_translate("FiletypesWidget", "Form", None))
        self.CloseButton.setToolTip(_translate("FiletypesWidget", "close", None))
        self.MinButton.setToolTip(_translate("FiletypesWidget", "minimize", None))
        self.TitleLabel.setText(_translate("FiletypesWidget", "Choose file types:", None))
        self.DocumentsLabel.setText(_translate("FiletypesWidget", "Documents:", None))
        self.DocCheckBox.setText(_translate("FiletypesWidget", ".doc/.docx", None))
        self.XlsCheckBox.setText(_translate("FiletypesWidget", ".xls", None))
        self.PPTCheckBox.setText(_translate("FiletypesWidget", ".ppt/.pptx", None))
        self.PdfCheckBox.setText(_translate("FiletypesWidget", ".pdf", None))
        self.GraphicsLabel.setText(_translate("FiletypesWidget", "Graphics:", None))
        self.JpgCheckBox.setText(_translate("FiletypesWidget", ".jpg/.jpeg", None))
        self.PngCheckBox.setText(_translate("FiletypesWidget", ".png", None))
        self.OtherLabel.setText(_translate("FiletypesWidget", "Other:", None))
        self.CancelButton.setText(_translate("FiletypesWidget", "Cancel", None))
        self.OkButton.setText(_translate("FiletypesWidget", "OK", None))
        self.label.setText(_translate("FiletypesWidget", "split by semicolon", None))

import res_rc
