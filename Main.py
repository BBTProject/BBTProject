from MainWidow import MainWindow
import multiprocessing
import threading

from PyQt4 import QtCore,QtGui
from PyQt4.QtCore import Qt
import sys
def mainProgram():
	pass

def monitor():
	pass


def main():
    multiprocessing.freeze_support()
    
    resultQueue = multiprocessing.Queue()
    flagQueue = multiprocessing.Queue()   
    pauseEvent = multiprocessing.Event()

    
    app = QtGui.QApplication(sys.argv)    
    
    # mainwindow = MainWindow(resultQueue,flagQueue)
    
            
    # threadMain = threading.Thread(target = mainProgram, args = (resultQueue,mainwindow,pauseEvent,flagQueue,), daemon = True)
    # threadMain.start()
    
    # threadMonitor = threading.Thread(target = monitor, args = (resultQueue,mainwindow,pauseEvent,flagQueue,), daemon = True)
    # threadMonitor.start()
    mainwindow = MainWindow()
    sys.exit(app.exec_()) 




if __name__ == '__main__':
	main()
    input()
