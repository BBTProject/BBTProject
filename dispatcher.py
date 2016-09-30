#-*- coding:utf-8 -*-

import logs
from monitor import monitor
from workerpool import workerpool
import time
from ThreadSettings import threadSettings

#py : for adding urls.
#logger     :  for documenting loggs.
#filter    :   for parsing things needed.
#Requester:    for launching requests.
#res for resources-url list:
res = []

class dispatcher:
    
    def __init__(self,paraDict, resultQueue, flagQueue, pauseEvent):
        
        #Redirect Settings
        threadSettings.target_filetype = paraDict['FILETYPESLIST']
        threadSettings.Login_Info      = paraDict['LOGININFOS']
        threadSettings.ISFILESEARCH    = paraDict['ISFILESEARCH']
        threadSettings.search_keywords = paraDict['KEYWORDS']
        threadSettings.sql_start_url   = paraDict['SQLSTARTURL']
        threadSettings.flag_queue      = flagQueue
        threadSettings.result_queue    = resultQueue
        threadSettings.pauseEvent      = pauseEvent
        
        #Initiate a worker
        self.workerpool_ = workerpool(paraDict['FILESTARTURL'])
        self.workerpool_.workerstowork(self.workerpool_.createWorker(threadSettings.Init_WorkerNum))
        
    def create_monitor(self):
        
        self.monitor_ = monitor()
        self.monitor_.start()
        monitor.curr_monitors += 1
        
    
        
if __name__ == '__main__':
    
    dispatcher_ = dispatcher()
    dispatcher_.create_monitor()
    
    