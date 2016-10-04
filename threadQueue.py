#-*- coding:utf-8 -*-

from queue import Queue
from logs  import LOG
from ThreadSettings import threadSettings

class threadQueue:
    
    threadqueue = Queue(maxsize=threadSettings.MaxQueuelength)
    threadalive = {}
    
    @staticmethod
    def add(element):
        
        #If queue itself is full
        #Do not add anymore elements 
        #and block anyone who wanna put things inside.
        threadQueue.threadqueue.put(element)
        
    @staticmethod
    def isEmpty():
        
        if threadQueue.threadqueue.empty():
            #Empty
            return 1
        else:
            #Not Empty
            return 0
        
    @staticmethod 
    def length():
        
        return threadQueue.threadqueue.qsize()
    
    @staticmethod
    def check_if_added(flag):
            
        if flag in threadQueue.threadalive :
            return 1
        else:
            return 0
        
    @staticmethod
    def mark_as_started(flag):
        
        threadQueue.threadalive[flag] = 1
        
    @staticmethod
    def checkIfAlive(flag):
        
        if threadQueue.threadalive[flag] == 1:
            return 1
        else:
            return 0
        
    @staticmethod
    def disableworker(flag):
        
        threadQueue.threadalive[flag] = 0
        
    @staticmethod
    def getaliveworkernum():
        
        num = 0
        flags = list(threadQueue.threadalive.keys())
        for flag in flags:
            if threadQueue.checkIfAlive(flag) == 1:
                num += 1
        return num
    
    @staticmethod
    def workertotalnum():
        
        return len(threadQueue.threadalive)
    