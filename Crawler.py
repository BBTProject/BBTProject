

class Crawler(object):
	"""docstring for Crawler"""
	def __init__(self, paraDict, resultQueue, flagQueue, pauseEvent):
		super(Crawler, self).__init__()
		self.paraDict = paraDict
		self.resultQueue = resultQueue
		self.flagQueue = flagQueue
		self.pauseEvent = pauseEvent

		print()
		print("In crawler:")
		print("paraDict: " + str(self.paraDict))			#see ParaKeys.py
		print("resultQueue: " + str(self.resultQueue))		#put the filename or problem url in the queue
		print("flagQueue: " + str(self.flagQueue))			#when finish the task put a string "STOP" in it
		print("pauseEvent: " + str(self.pauseEvent))		#use to pause the program (the usage: self.pauseEvent.wait())
		print()


	def start(self):
		import time
		for i in range(10):
			time.sleep(1)
			self.pauseEvent.wait()
			self.resultQueue.put("filename" + str(i))
		self.flagQueue.put("STOP")

		