#-*- coding:utf-8 -*-

import threading
import logs
#from filter import filter
import time
import random
from threadQueue import threadQueue
from Requester import Requester
from ThreadSettings import threadSettings
from Mparser import Myparser
import Search
#py : for adding urls.
#logger     :  for documenting loggs.
#filter    :   for parsing things needed.
#Requester:    for launching requests.
mutex = threading.Lock()

class worker(threading.Thread):
    
    def run(self):
        
        self.times = 0
        self.work()
        
    def work(self):
        
        while 1:
            if  threadQueue.checkIfAlive(self.flag) != 1 :
                print ("[*]Worker is dead.")
                #time for worker to have a rest
                break
            #print ("[*]Worker is working.")
            try:
                #Get url from threadqueue
                target_url = threadQueue.threadqueue.popleft()
                if threadSettings.thread_debug :
                    print("worker " + self.flag + "[*] Get " + str(target_url) + " from queue")
                #test
                self.process_url(target_url)
            except Exception as e:
                #If queue is empty currently, wait.
                if threadSettings.thread_debug:
                    print ("[*] " + e)
                self.times += 1
                if self.times == threadSettings.SleepTimeBeforeEnd:
                    #Time to get off work
                    threadQueue.disableworker(self.flag)
                    break
                time.sleep(threadSettings.WaitWhenQueueEmptyInterval)
                #print ("[*]Queue is empty!")
                continue
            '''
            if  'http' in target_url:
                #incase if url cannot open or timeout
                try:
                #incase if url is broken
                    self.process_url(target_url)
                except:
                    try:
                        #maybe surely cannot open
                        self.process_url(target_url)
                    except:
                        continue
                    
            else:
                #broken url
                continue
                '''
            
    def process_url(self,target_url):
        
        #acquire content first
        searcher =  Search.search()
        searcher.get(target_url)
        parser   = Myparser(target_url)
        parser.check_response(searcher.response)
        if parser.need2feed:
            parser.feed(searcher.text)
        
        next_links_url = parser.link_list
        resources_url  = parser.img_list + parser.pdf_list
        for resource in resources_url :
            threadSettings.result_queue.put("filename: " + resource)
        
        self.generatenext(next_links_url)
    def setflag(self,flag):
        
        self.flag = flag
    
    def generatenext(self,next_links):
        
        for url in next_links:
            mutex.acquire()
            if Requester.check_if_visited(url) == 1:
                print ("[*] " + url + " has been visited.")
                mutex.release()
            else:   
                Requester.mark_as_visited(url)
                mutex.release()
                print ("[*] Put " + url + " in dic , mark as visited.")
                try:
                    threadQueue.add(url)
                    time.sleep(0.05)
                    if threadSettings.thread_debug:
                        print("worker" + self.flag + "[*]Put " + url + " in queue.")
                except Exception as e:
                    print (e) 
                
            
        