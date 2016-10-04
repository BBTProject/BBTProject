#-*- coding:utf-8 -*-

#Patch for the third time:
#Disable All prints
#Initiate Logs
#Eliminate Unnecessary tags

from logs import LOG
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
        threadSettings.filesearch_start_url = paraDict['FILESTARTURL']
        threadSettings.target_filetype      = paraDict['FILETYPESLIST']
        threadSettings.Login_Info           = paraDict['LOGININFOS']
        threadSettings.FileSearch_Mode      = paraDict['ISFILESEARCH']
        threadSettings.search_keywords      = paraDict['KEYWORDS']
        threadSettings.sql_start_url        = paraDict['SQLSTARTURL']
        threadSettings.flag_queue           = flagQueue
        threadSettings.result_queue         = resultQueue
        threadSettings.pauseEvent           = pauseEvent
        logger = LOG("","test.log")
        if  len(threadSettings.sql_start_url) != 0:
            threadSettings.SqlInjectionTest_Mode = True
        #Initiate the first worker
        if  threadSettings.SqlInjectionTest_Mode:
            self.workerpool_ = workerpool(threadSettings.sql_start_url)
            self.workerpool_.workerstowork(self.workerpool_.createWorker(threadSettings.Init_WorkerNum))
        else:
            self.workerpool_ = workerpool(threadSettings.filesearch_start_url)
            self.workerpool_.workerstowork(self.workerpool_.createWorker(threadSettings.Init_WorkerNum))
        
if __name__ == '__main__':
    
    dispatcher_ = dispatcher()
    dispatcher_.create_monitor()
    
    