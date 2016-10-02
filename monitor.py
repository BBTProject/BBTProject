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
    
    #Counting the initiate one.
    curr_monitors = 0
    
    def run(self):
        
        self.workerpool_ = workerpool()
        while 1:
            #Monitoring system interval 2 seconds
            #time.sleep(threadSettings.Monitor_check_time)
            if threadQueue.checkIfmonAlive(self.flag) != 1:
                break
            self.refresh()
            self.monit()
            print ("[*]Running Monitor " + self.flag)
            LOG.WriteLog("[*]Running Monitor " + self.flag)
            self.printoutCurr()
            self.dispatcher(workerpool.currworknum, threadQueue.length())
            
    def printoutCurr(self):
        
        LOG.WriteLog("[*]Current Monitors: " + str(monitor.curr_monitors))
        LOG.WriteLog("[*] Running Workers: " + str(workerpool.currworknum))
        LOG.WriteLog("[*] Elements in queue: " + str(threadQueue.length()))
        threadQueue.showContent()
        
    def dispatcher(self, workernum, queuelen):
        
        #Maintain queue length approximately 3times smaller than worker number
        #A simple dispatcher example
        #Looking for better equipment ways with multiple experiments.
        self.monit()
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
    
    def monit(self):
        
        if threadSettings.Switch_Halt == True and threadSettings.Switch_Stop==True:
            threadSettings.flag_queue.put("STOP")
        target_num = int(workerpool.currworknum/threadSettings.WorkerPer_Monitor)
        if target_num > monitor.curr_monitors:
            temp = target_num - monitor.curr_monitors
            for i in range(temp):
                self.create_monitor()
        elif target_num <= monitor.curr_monitors:
            temp = monitor.curr_monitors - target_num
            self.disablemonitor(temp)
    
    def create_monitor(self):
        
        monitor_ = monitor()
        t = random.randint(0,threadSettings.MonitorMaximum)
        flag = str(t)
        while threadQueue.check_if_monadded(flag) == 1:
            t = (t+1) % threadSettings.MonitorMaximum
            flag = str(t)
        monitor_.setflag(flag)
        threadQueue.mark_as_monstarted(flag)
        monitor.curr_monitors += 1
        monitor_.start()
        
    def refresh(self):
        
        currworknum_ = threadQueue.getaliveworkernum()
        workerpool.currworknum = currworknum_
        if currworknum_ > 15:
            if threadSettings.thread_debug:
                print ("[*]Monitor Running Properly")
            threadSettings.Switch_Halt = True
        if threadSettings.Switch_Halt == True and currworknum_<3:
            threadSettings.Switch_Stop = True
    
    def setflag(self,flag):
        
        self.flag = flag
        
    def disablemonitor(self,num):
        
        if num <= 0 :
            return 
        #If there's 100 , disable 99.
        if num >= monitor.curr_monitors:
            num = monitor.curr_monitors - 1
        
        flags = list(threadQueue.monitors.keys())
        for i in range(num):
            token = random.randint(0,len(flags)-1)
            while threadQueue.checkIfmonAlive(flags[token]) == 0:
                token = (token+1)%(len(flags)-1)
            threadQueue.disablemonitor(flags[token])
            monitor.curr_monitors -= 1
            
    