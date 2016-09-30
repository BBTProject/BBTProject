
#-*- coding:utf-8 -*-

from Ui_Widgets.LoginInfoWidget import Ui_LoginInfoWidget
from PyQt4 import QtCore,QtGui
from PyQt4.QtCore import Qt
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class LoginInfoWindow(QtGui.QDialog):
	def __init__(self, filePath, loginInfos, parent=None):
		QtGui.QWidget.__init__(self,parent)


		self.ui=Ui_LoginInfoWidget()
		self.ui.setupUi(self)
		self.ui.retranslateUi(self)

		self.m_DragPosition=self.pos()
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setMouseTracking(True)


		
		self.connect(self.ui.OkButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.acceptedClose)
		self.connect(self.ui.CancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.rejectedClose)

		self.filePath = filePath
		self.loginInfos = loginInfos;
		self.fileContentInfos = []
		self.showFileConten()


	def acceptedClose(self):
		for info in self.fileContentInfos:
			self.loginInfos.append(info)
		self.accept()

	def rejectedClose(self):
		self.reject()

	def showFileConten(self):
		with open(self.filePath) as file:
			fileConten = file.read()
		for infos in fileConten.split("\n"):
			info = infos.split(" ")
			account = info[0]
			password = info[1]
			self.fileContentInfos.append((account, password))
			rowPosition = self.ui.tableWidget.rowCount()
			self.ui.tableWidget.insertRow(rowPosition)
			self.ui.tableWidget.setItem(rowPosition, 0, QtGui.QTableWidgetItem(account))
			self.ui.tableWidget.setItem(rowPosition, 1, QtGui.QTableWidgetItem(password))


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



def main():
	app = QtGui.QApplication(sys.argv)
	mainwindow = LoginInfoWindow()
	mainwindow.show()
	sys.exit(app.exec_()) 


if __name__ == '__main__':
	main()