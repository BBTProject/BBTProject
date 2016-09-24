#!/usr/bin/env python
# -*- coding:utf-8 -*-
 
"""
PyQt实验室
"""
 
#system imports
import sys
 
#pyqt imports
from PyQt4 import QtCore,QtGui
from PyQt4.QtCore import Qt
 
 
class MainWindow(QtGui.QWidget):
    def __init__(self):
 
        QtGui.QWidget.__init__(self)
 
        #初始化position
        self.m_DragPosition=self.pos()
 
        self.resize(600,400)
        self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
        self.setMouseTracking(True)
        self.setStyleSheet("background-color:#66ccff;")
 
        #按钮一
        self.ButtonFileWidget=QtGui.QPushButton(u"File",self)
        self.ButtonFileWidget.setGeometry(0,0,120,100)
        self.ButtonFileWidget.setStyleSheet("QPushButton{background-color:#2C3E50;border:none;color:#ffffff;font-size:20px;}"
                               "QPushButton:hover{background-color:#333333;}")
        self.ButtonSQLWidget=QtGui.QPushButton(u"SQL",self)
        self.ButtonSQLWidget.setGeometry(0,100,120,100)
        self.ButtonSQLWidget.setStyleSheet("QPushButton{background-color:#2C3E50;border:none;color:#ffffff;font-size:20px;}"
                               "QPushButton:hover{background-color:#333333;}")
        self.ButtonHelpWidget=QtGui.QPushButton(u"Help",self)
        self.ButtonHelpWidget.setGeometry(0,200,120,100)
        self.ButtonHelpWidget.setStyleSheet("QPushButton{background-color:#2C3E50;border:none;color:#ffffff;font-size:20px;}"
                               "QPushButton:hover{background-color:#333333;}")
        self.ButtonAboutWidget=QtGui.QPushButton(u"About",self)
        self.ButtonAboutWidget.setGeometry(0,300,120,100)
        self.ButtonAboutWidget.setStyleSheet("QPushButton{background-color:#2C3E50;border:none;color:#ffffff;font-size:20px;}"
                               "QPushButton:hover{background-color:#333333;}")
        self.ButtonMin=QtGui.QPushButton(u"min",self)
        self.ButtonMin.setGeometry(520,0,40,25)
        self.ButtonMin.setStyleSheet("QPushButton{background-color:#D35400;border:none;color:#ffffff;font-size:10px;}"
                                 "QPushButton:hover{background-color:#333333;}")        
        self.ButtonClose=QtGui.QPushButton(u"close",self)
        self.ButtonClose.setGeometry(560,0,40,25)
        self.ButtonClose.setStyleSheet("QPushButton{background-color:#D35400;border:none;color:#ffffff;font-size:10px;}"
                                 "QPushButton:hover{background-color:#333333;}")
 
        #注册事件
        self.connect(self.ButtonClose,QtCore.SIGNAL("clicked()"),QtGui.qApp,QtCore.SLOT("quit()"))
 
 
    #支持窗口拖动,重写两个方法
    def mousePressEvent(self, event):
        if event.button()==Qt.LeftButton:
            self.m_drag=True
            self.m_DragPosition=event.globalPos()-self.pos()
            event.accept()
 
    def mouseMoveEvent(self, QMouseEvent):
        if QMouseEvent.buttons() and Qt.LeftButton:
            self.move(QMouseEvent.globalPos()-self.m_DragPosition)
            QMouseEvent.accept()
 
    def mouseReleaseEvent(self, QMouseEvent):
        self.m_drag=False
 
 
 
if __name__=="__main__":
 
    mapp=QtGui.QApplication(sys.argv)
    mw=MainWindow()
    mw.show()
    sys.exit(mapp.exec_())