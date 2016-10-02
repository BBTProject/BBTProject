#-*- coding:utf-8 -*-

import os
import time
from ThreadSettings import threadSettings
ISOTIMEFORMAT = '%Y-%m-%d %X'

class LOG:
    
    Filepath = ''
    Filename = ''
    dolog    = threadSettings.log_open
    
    def __init__(self,FilePath ,FileName):
        
        LOG.Filename = FileName
        LOG.Filepath = FilePath
        if len(LOG.Filepath) == 0:
            pass
        else:
            if not os.path.exists(FilePath):
                os.makedirs(FilePath)
        
        if  LOG.dolog:
            LOG.fp = open(FilePath + FileName, 'a')
            LOG.fp.write('[*] Logger Initiate At : ' + time.strftime(ISOTIMEFORMAT) + '\n\n')
        
    @staticmethod
    def WriteLog(content):
        if LOG.dolog:
            LOG.fp.write(content + '\n')
        
    @staticmethod
    def close():
        if LOG.dolog:
            LOG.fp.close()

if __name__ == '__main__':
    
    logger = LOG('C:\\', "moduletester.log")
    
        
        
        
        
        



