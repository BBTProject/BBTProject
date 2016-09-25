from BaseWidget import Ui_BaseWidget
from PyQt4 import QtCore,QtGui
from PyQt4.QtCore import Qt

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QWidget.__init__(self,parent=None)


		self.ui=Ui_BaseWidget()
		self.ui.setupUi(self)
		self.ui.retranslateUi(self)

		self.m_DragPosition=self.pos()
		self.setWindowFlags(Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
		self.setMouseTracking(True)

		self.oldScrollBarValue = 0
		self.connect(self.ui.verticalScrollBar, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.scrollFileWidget)
		self.ui.SQLInputWidget.hide()

		
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


	def scrollFileWidget(self, position):
		y = self.oldScrollBarValue - position
		self.ui.ScrollWidget.scroll(0, y)
		self.oldScrollBarValue = position

	# def paintEvent(self, e):

	# 	bmp = QtGui.QBitmap(self.size())
	# 	bmp.fill()
	# 	p = QtGui.QPainter()
	# 	p.begin(self)
	# 	p.setPen(Qt.NoPen)
	# 	p.setBrush(Qt.black)
	# 	p.drawRoundedRect(bmp.rect(), 10, 10);
	# 	p.end()
	# 	self.setMask(bmp)
		