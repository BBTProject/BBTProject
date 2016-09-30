#-*- coding:utf-8 -*-

from Ui_Widgets.FiletypesWidget import Ui_FiletypesWidget
from PyQt4 import QtCore,QtGui
from PyQt4.QtCore import Qt
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class FiletypesWindow(QtGui.QDialog):
	def __init__(self, filetypesList, parent=None):
		QtGui.QWidget.__init__(self,parent)


		self.ui=Ui_FiletypesWidget()
		self.ui.setupUi(self)
		self.ui.retranslateUi(self)

		self.m_DragPosition=self.pos()
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setMouseTracking(True)

		self.connect(self.ui.OkButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.acceptedClose)
		self.connect(self.ui.CancelButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.rejectedClose)

		self.filetypesList = filetypesList

	def acceptedClose(self):
		self.geneFiletypesList()
		self.accept()

	def rejectedClose(self):
		self.reject()

	def geneFiletypesList(self):

		del self.filetypesList[:]
		
		checkBoxs = self.findChildren(QtGui.QCheckBox)
		for checkBox in checkBoxs:
			if checkBox.checkState() == Qt.Checked:
				text = checkBox.text()
				for t in text.split("/"):
					if t != "":
						self.filetypesList.append(t)
		otherText = self.ui.OtherLineEdit.text()
		for t in otherText.split(";"):
			if t != "":
				self.filetypesList.append(t)


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
	mainwindow = FiletypesWindow()
	mainwindow.show()
	sys.exit(app.exec_()) 


if __name__ == '__main__':
	main()