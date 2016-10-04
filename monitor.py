#-*- coding:utf-8 -*-

import threading
import time
import random
from threadQueue import threadQueue
from workerpool import workerpool
from ThreadSettings import threadSettings
from logs import LOG

#Dispatch threads num according to the 
#relationship between work_queue length and 
#workers .
#Print out relevant numbers currently.

class monitor(threading.Thread):
    
    def run(self):
        
        if threadSettings.Switch_Halt == True\
        and threadSettings.Switch_Stop == True:
            self.putendflag()
        #Monitoring system interval 2 seconds
        #time.sleep(threadSettings.Monitor_check_time)
        self.refresh()
        self.workerpool_ = workerpool()
        print ("[*]Running Monitor of worker: " + self.flag)
        LOG.WriteLog("[*]Running Monitor of worker: " + self.flag)
        self.LogCurrentParam()
        self.dispatcher(threadQueue.getaliveworkernum(), threadQueue.length())
        
    def LogCurrentParam(self):
        
        #LOG.WriteLog("[*]Current Monitors: " + str(monitor.curr_monitors))
        LOG.WriteLog("[*] Running Workers: " + str(workerpool.currworknum))
        LOG.WriteLog("[*] Elements in queue: " + str(threadQueue.length()))
        #threadQueue.showContent()
        
    def dispatcher(self, workernum, queuelen):
        
        #Maintain queue length approximately 3times smaller than worker number
        #A simple dispatcher example
        #Looking for better equipment ways with multiple experiments.
        
        #Dispatch once , plus one.
        if queuelen == 0:
            return
        lowerbound = queuelen*threadSettings.WorkervsQueueLowerBound
        upperbound = queuelen*threadSettings.WorkervsQueueUpperBound
        if  workernum < lowerbound:
            x = int(lowerbound - workernum)
            self.workerpool_.workerstowork(self.workerpool_.createWorker(x))
            LOG.WriteLog("[*] Adding" + str(x) + " workers")
            if threadSettings.thread_debug:
                print ("[*]Adding " + str(x) + " workers")
        elif upperbound <= workernum:
            x = int(workernum - upperbound)
            self.workerpool_.stopworkers(x)
            LOG.WriteLog("[*]Eliminating " + str(x) + "workers")
            if threadSettings.thread_debug:
                print ("[*]Eliminating " + str(x) + " workers")
        elif workernum > lowerbound and workernum < upperbound:
            
            temp = int(queuelen*threadSettings.WorkerSwing)
            middle = int(queuelen * ((threadSettings.WorkervsQueueLowerBound + 
                                     threadSettings.WorkervsQueueUpperBound)/2-
                                    threadSettings.WorkervsQueueLowerBound))
            if workernum < lowerbound + middle:
                
                LOG.WriteLog("[*] Adding " + str(temp) + " workers")
                if threadSettings.thread_debug:
                    print ("[*]Adding " + str(temp) + " workers")
                self.workerpool_.workerstowork(self.workerpool_.createWorker(temp))
            else:
                pass
        
    def refresh(self):
        
        currworknum_ = threadQueue.getaliveworkernum()
        workerpool.currworknum = currworknum_
        if threadSettings.Switch_Halt :
            if  currworknum_ < 3 :
                threadSettings.Switch_Stop = True
        else:
            if currworknum_ > 15:
                if threadSettings.thread_debug:
                    print ("[*]Monitor Running Properly")
                threadSettings.Switch_Halt = True
            else:
                pass
    
    def setflag(self,flag):
        
        self.flag = flag
        
    def putendflag(self):
        
        threadSettings.flag_queue.put("STOP")
        
    