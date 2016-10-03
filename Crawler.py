
#-*- coding:utf-8 -*-

from dispatcher import dispatcher
import time 

class Crawler(object):
	"""docstring for Crawler"""
	def __init__(self, paraDict, resultQueue, flagQueue, pauseEvent):
		super(Crawler, self).__init__()
		self.paraDict = paraDict
		self.resultQueue = resultQueue
		self.flagQueue = flagQueue
		self.pauseEvent = pauseEvent

		#print()

		print("In crawler:")
		print("paraDict: " + str(self.paraDict))			#see ParaKeys.py
		print("resultQueue: " + str(self.resultQueue))		#put the filename or problem url in the queue
		print("flagQueue: " + str(self.flagQueue))			#when finish the task put a string "STOP" in it
		print("pauseEvent: " + str(self.pauseEvent))		#use to pause the program (the usage: self.pauseEvent.wait())

	def start(self):
		
		dispatcher_ = dispatcher(self.paraDict, self.resultQueue, self.flagQueue, self.pauseEvent)
		time.sleep(15)
		dispatcher_.create_monitor()
		