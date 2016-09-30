
#-*- coding:utf-8 -*-

from MainWidow import MainWindow
from ParaKeys import ParaKeys
import multiprocessing
import threading

from PyQt4 import QtCore,QtGui
from PyQt4.QtCore import Qt
import sys, time



def startCrawler(paraDict, resultQueue, flagQueue, pauseEvent):
	from Crawler import Crawler
	crawler = Crawler(paraDict, resultQueue, flagQueue, pauseEvent)
	crawlerProcess = multiprocessing.Process(target = crawler.start, daemon = True)
	crawlerProcess.start()
	return crawlerProcess




def mainProgram(paraDict, resultQueue, flagQueue, pauseEvent, mainwindow):
	while True:
		if flagQueue.get(True) == "START":
			pauseEvent.set()
			print("mainProgram start.......")
			crawlerProcess = startCrawler(paraDict, resultQueue, flagQueue, pauseEvent)
			monitorFlag(flagQueue, pauseEvent, crawlerProcess)
			mainwindow.resetSignal.emit()


def monitorFlag(flagQueue, pauseEvent, crawlerProcess):
	while True:
		flag = flagQueue.get(True)
		if flag == "STOP":
			if not pauseEvent.is_set():
				pauseEvent.set()
			print("stop the mainProgram.......")
			crawlerProcess.terminate()
			break
		elif flag == "PAUSE":
			pauseEvent.clear()
			print("pause the mainProgram.......")
		elif flag == "RESUME":
			pauseEvent.set()
			print("resume the mainProgram.......")


def monitorResult(resultQueue, mainwindow):
	while True:
		result = resultQueue.get(True)
		mainwindow.addItemSignal.emit(result)

def getParaDict():
	return dict()

def main():
    multiprocessing.freeze_support()
    
    paraDict = getParaDict()
    resultQueue = multiprocessing.Queue()
    flagQueue = multiprocessing.Queue()
    pauseEvent = multiprocessing.Event()
    
    app = QtGui.QApplication(sys.argv)    
    mainwindow = MainWindow(paraDict = paraDict, resultQueue = resultQueue, flagQueue = flagQueue)

    threadMain = threading.Thread(target = mainProgram, args = (paraDict, resultQueue, flagQueue, pauseEvent, mainwindow, ), daemon = True)
    threadMain.start()
    
    threadMonitor = threading.Thread(target = monitorResult, args = (resultQueue, mainwindow, ), daemon = True)
    threadMonitor.start()


    
    sys.exit(app.exec_()) 




if __name__ == '__main__':
	main()
