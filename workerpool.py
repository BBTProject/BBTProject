#-*- coding:utf-8 -*-

from collections import deque
from threadQueue import threadQueue
import worker
import random
import time
from ThreadSettings import threadSettings
class workerpool:
    
    #Init working thread number
    init_worknum = threadSettings.Init_WorkerNum
    
    #Current Working threads number
    currworknum  = 0
    
    #Maximum working threads number
    maxnum  = threadSettings.WorkerMaximum
    
    def __init__(self,url=-1):
        #Add Url Element here.
        if url == -1:
            pass
        else:
            threadQueue.add(url)

    def createWorker(self,num):
        
        if  num <= 0:
            print ("[*]Worker number to create must >0")
        else:
            workerlist = []
            for i in range(num):
                worker_ = worker.worker()
                workerlist.append(worker_)
            return workerlist
        
    def workerstowork(self,workerlist):
        if len(workerlist) == 0:
            return
        for worker in workerlist:
            
            if workerpool.currworknum >= workerpool.maxnum:
                print ("[*]Worker num reaches maximum")
                break
            else:
                try:
                    flag = str(random.randint(0,threadSettings.WorkerMaximum))
                    while threadQueue.check_if_added(flag) == 1:
                        #Duplicated flag
                        flag = str(random.randint(0,threadSettings.WorkerMaximum))
                        
                    worker.setflag(flag)
                    threadQueue.mark_as_started(flag)
                    time.sleep(threadSettings.WorkerLaunchInterval)
                    worker.start()
                    workerpool.currworknum += 1
                except Exception as e:
                    print (e)
                    print ("[*]Worker starts failed")
                    
    def stopworkers(self, num):
        if num == 0:
            return
        alivenum = threadQueue.getaliveworkernum()
        if  num >= alivenum:
            num = alivenum
            
        flags = list(threadQueue.threadalive.keys())
        for i in range(num):
            token = random.randint(0,len(flags)-1)
            while threadQueue.checkIfAlive(flags[token])==0:
                token = random.randint(0,len(flags)-1)
            threadQueue.disableworker(flags[token])
            workerpool.currworknum -= 1
            time.sleep(threadSettings.WorkerStopInterval)
            