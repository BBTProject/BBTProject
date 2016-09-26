

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
		print("paraDict: " + str(self.paraDict))
		print("resultQueue: " + str(self.resultQueue))
		print("flagQueue: " + str(self.flagQueue))
		print("pauseEvent: " + str(self.pauseEvent))
		print()


	def start(self):
		import time
		for i in range(10):
			time.sleep(1)
			self.resultQueue.put("filename" + str(i))
		self.flagQueue.put("STOP")

		