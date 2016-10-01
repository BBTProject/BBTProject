#-*- coding:utf-8 -*-

import threading
import time
import random
from threadQueue import threadQueue
from workerpool import workerpool
from ThreadSettings import threadSettings

#Dispatch threads num according to the 
#relationship between work_queue length and 
#workers .
#Print out relevant numbers currently.

class monitor(threading.Thread):
    
    #Counting the initiate one.
    curr_monitors = 0
    
    def run(self):
        
        self.workerpool_ = workerpool()
        while 1:
            #Monitoring system interval 2 seconds
            #time.sleep(threadSettings.Monitor_check_time)
            self.refresh()
            self.monit()
            print ("[*]Running Monitor Process")
            self.printoutCurr()
            self.dispatcher(workerpool.currworknum, threadQueue.length())
            
    def printoutCurr(self):
        
        print ("[*]Current Monitors: " + str(monitor.curr_monitors))
        print ("[*] Running Workers: " + str(workerpool.currworknum))
        print ("[*] Elements in queue: " + str(threadQueue.length()))
        threadQueue.showContent()
        
    def dispatcher(self, workernum, queuelen):
        
        #Maintain queue length approximately 3times smaller than worker number
        #A simple dispatcher example
        #Looking for better equipment ways with multiple experiments.
        
        lowerbound = queuelen*threadSettings.WorkervsQueueLowerBound
        upperbound = queuelen*threadSettings.WorkervsQueueUpperBound
        if  workernum < lowerbound:
            x = int(lowerbound - workernum)
            self.workerpool_.workerstowork(self.workerpool_.createWorker(x))
            if threadSettings.thread_debug:
                print ("[*]Adding " + str(x) + " workers")
        elif upperbound <= workernum:
            x = int(workernum - upperbound)
            self.workerpool_.stopworkers(x)
            if threadSettings.thread_debug:
                print ("[*]Eliminating " + str(x) + " workers")
        elif workernum > lowerbound and workernum < upperbound:
            
            temp = int(queuelen*threadSettings.WorkerSwing)
            middle = int(queuelen * ((threadSettings.WorkervsQueueLowerBound + 
                                     threadSettings.WorkervsQueueUpperBound)/2-
                                    threadSettings.WorkervsQueueLowerBound))
            if workernum < lowerbound + middle:
                
                if threadSettings.thread_debug:
                    print ("[*]Adding " + str(temp) + " workers")
                self.workerpool_.workerstowork(self.workerpool_.createWorker(temp))
            else:
                pass
    
    def monit(self):
        
        if threadSettings.Switch_Halt == True and threadSettings.Switch_Stop==True:
            threadSettings.flag_queue.put("STOP")
        target_num = int(workerpool.currworknum/threadSettings.WorkerPer_Monitor)
        if target_num > monitor.curr_monitors:
            temp = target_num - monitor.curr_monitors
            for i in range(temp):
                self.create_monitor()
        else:
            pass
    
    def create_monitor(self):
        
        monitor_ = monitor()
        monitor_.start()
        monitor.curr_monitors += 1
    
    def refresh(self):
        
        currworknum_ = threadQueue.getaliveworkernum()
        workerpool.currworknum = currworknum_
        if currworknum_ > 20:
            if threadSettings.thread_debug:
                print ("[*]System Running Properly")
            threadSettings.Switch_Halt = True
        if threadSettings.Switch_Halt == True and currworknum_<3:
            threadSettings.Switch_Stop = True
        