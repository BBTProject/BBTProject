#-*- coding:utf-8 -*-

import os
import time

ISOTIMEFORMAT = '%Y-%m-%d %X'

class LOG:
    
    Filepath = ''
    Filename = ''
    
    def __init__(self,FilePath,FileName):
        
        LOG.Filename = FileName
        LOG.Filepath = FilePath
        
        if not os.path.exists(FilePath):
            
            os.makedirs(FilePath)
            
        LOG.fp = open(FilePath + FileName, 'a')
        LOG.fp.write('[*] Logger Initiate At : ' + time.strftime(ISOTIMEFORMAT) + '\n\n')
        
    @staticmethod
    def WriteLog(content):
        
        LOG.fp.write(content + '\n')
        
    @staticmethod
    def close():
        
        LOG.fp.close()

if __name__ == '__main__':
    
    logger = LOG('C:\\', "moduletester.log")
    
        
        
        
        
        



