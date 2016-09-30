#-*- coding:utf-8 -*-

from collections import deque
import logs

class threadQueue:
    
    threadqueue = deque()
    threadalive = {}
    
    @staticmethod
    def add(element):
        
        threadQueue.threadqueue.append(element)
        
    @staticmethod
    def isEmpty():
        
        if threadQueue.threadqueue:
            #Not Empty
            return 1
        else:
            #Empty
            return 0

    @staticmethod
    def clear():
        
        #Clear Queue
        threadQueue.threadqueue.clear()
    
    @staticmethod 
    def length():
        
        return len(threadQueue.threadqueue)
    
    @staticmethod
    def showContent():
        
        print (threadQueue.threadqueue)
    
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
    