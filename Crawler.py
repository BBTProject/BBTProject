

class Crawler(object):
	"""docstring for Crawler"""
	def __init__(self, paraDict, resultQueue, flagQueue, pauseEvent):
		super(Crawler, self).__init__()
		self.paraDict = paraDict
		self.resultQueue = resultQueue
		self.flagQueue = flagQueue
		self.pauseEvent = pauseEvent

	def start(self):
		import time
		for i in range(20):
			time.sleep(1)
			self.resultQueue.put("filename" + str(i))
		self.flagQueue.put("STOP")

		