from BaseWidget import Ui_BaseWidget
from PyQt4 import QtCore,QtGui
from PyQt4.QtCore import Qt

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QWidget.__init__(self,parent=None)
		self.ui=Ui_BaseWidget()
		self.ui.setupUi(self)
		self.ui.retranslateUi(self)

		self.m_DragPosition=self.pos()
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
		self.setMouseTracking(True)

		self.show()


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