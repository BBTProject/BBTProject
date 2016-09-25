from Ui_Widgets.BaseWidget import Ui_BaseWidget
from PyQt4 import QtCore,QtGui
from PyQt4.QtCore import Qt
from FiletypesWindow import FiletypesWindow
from LoginInfoWindow import LoginInfoWindow
import sys

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

class MainWindow(QtGui.QMainWindow):
	def __init__(self):
		QtGui.QWidget.__init__(self,parent=None)


		self.paraDict = dict()

		self.ui=Ui_BaseWidget()
		self.ui.setupUi(self)
		self.ui.retranslateUi(self)

		self.m_DragPosition=self.pos()
		self.setWindowFlags(Qt.FramelessWindowHint)
		self.setMouseTracking(True)


		self.connectAllSlot()		

		self.ui.SQLInputWidget.hide()
		self.show()

		self.filetypesList = []
		self.loginInfos = []
		self.fileStartUrl = ""
		self.sqlStartUrl = ""
		self.keyWords = []

		self.ISFILESEARCH = "ISFILESEARCH"
		self.FILETYPESLIST = "FILETYPESLIST"
		self.LOGININFOS = "LOGININFOS"
		self.FILESTARTURL = "FILESTARTURL"
		self.SQLSTARTURL = "SQLSTARTURL"
		self.KEYWORDS = "KEYWORDS"

	def connectAllSlot(self):

		#connect scrollBar to scroll the fileWidget
		self.oldScrollBarValue = 0
		self.connect(self.ui.verticalScrollBar, QtCore.SIGNAL(_fromUtf8("valueChanged(int)")), self.scrollFileWidget)

		self.connect(self.ui.AddFiletypesButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.openFiletypesWindow)

		self.connect(self.ui.OpenFileButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.openLoginInfoFile)

		self.connect(self.ui.RunButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.run)

		self.connect(self.ui.PauseButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.pause)

		self.connect(self.ui.StopButton, QtCore.SIGNAL(_fromUtf8("clicked()")), self.stop)

	def scrollFileWidget(self, position):
		y = self.oldScrollBarValue - position
		self.ui.ScrollWidget.scroll(0, y)
		self.oldScrollBarValue = position

	def openLoginInfoFile(self):
		homepath = QtCore.QDir.homePath()        
		filePath = QtGui.QFileDialog.getOpenFileName(self, "chose file", homepath, "*.txt")
		if filePath:
			self.openLoginInfoWindow(filePath)

	def openFiletypesWindow(self):
		self.filetypesWindow = FiletypesWindow(self.filetypesList)
		if(self.filetypesWindow.exec() == QtGui.QDialog.Accepted):
			print(self.filetypesList)
			self.ui.FiletypesLineEdit.setText(str(self.filetypesList))
		else:
			print(2)
		print(3)


	def openLoginInfoWindow(self, filePath):

		self.loginInfoWindow = LoginInfoWindow(filePath, self.loginInfos)

		if(self.loginInfoWindow.exec() == QtGui.QDialog.Accepted):
			print(self.loginInfos)
			self.ui.UserInfosLineEdit.setText(str(self.loginInfos))
		else:
			print(2)
		print(3)


	def run(self):
		if self.ui.FileWidget.isHidden():
			self.runSQLDetect()
		else:
			self.runFileSearch()

	def pause(self):
		pass

	def stop(self):
		pass

	def runFileSearch(self):
		if not self.hasFiletypes():
			QtGui.QMessageBox.information(self, "Warning", "Please input some file types!")
			return
		elif not self.hasFileStartUrl():
			QtGui.QMessageBox.information(self, "Warning", "Please input the startUrl!")
			return

		self.setParaDict(True)

	def runSQLDetect(self):
		if not self.hasSQLStartUrl():
			QtGui.QMessageBox.information(self, "Warning", "Please input some file types!")
			return
		self.setParaDict(False)

	def hasFiletypes(self):
		return len(self.filetypesList) != 0

	def hasFileStartUrl(self):
		self.fileStartUrl = self.ui.FileStartUrlLineEdit.text()
		return self.fileStartUrl != ""

	def hasSQLStartUrl(self):
		self.sqlStartUrl = self.ui.SQLStartUrlLineEdit.text()
		return self.sqlStartUrl != ""

	def setParaDict(self, isFileSearch):
		self.paraDict[self.ISFILESEARCH] = isFileSearch
		self.paraDict[self.FILESTARTURL] = self.fileStartUrl
		self.paraDict[self.SQLSTARTURL] = self.sqlStartUrl
		self.paraDict[self.FILETYPESLIST] = self.filetypesList
		self.paraDict[self.KEYWORDS] = self.ui.FilterKeyWordLineEdit.text()
		self.paraDict[self.LOGININFOS] = self.loginInfos

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
    mainwindow = MainWindow()
    sys.exit(app.exec_()) 


if __name__ == '__main__':
	main()