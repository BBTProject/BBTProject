#-*- coding:utf-8 -*-

import threading
from logs import LOG
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
mutex_res = threading.Lock()
mutex_link= threading.Lock()

class worker(threading.Thread):
    
    def run(self):
        
        self.times = 0
        self.work()
        
    def work(self):
        
        while 1:
            if  threadQueue.checkIfAlive(self.flag) != 1 :
                LOG.WriteLog("[*]Worker " + self.flag + " is dead.")
                if threadSettings.thread_debug:
                    print ("[*]Worker " + self.flag + " is dead.")
                #time for worker to have a rest
                break
            #print ("[*]Worker is working.")
            try:
                #Get url from threadqueue
                target_url = threadQueue.threadqueue.popleft()
                LOG.WriteLog("[*]" + self.flag + " working")
            except Exception as e:
                if threadSettings.thread_debug:
                    print ("[*]" + str(e))
                self.times += 1
                if self.times == threadSettings.SleepTimeBeforeEnd:
                    threadQueue.disableworker(self.flag)
                    break
                else:
                    time.sleep(threadSettings.WaitWhenQueueEmptyInterval)
                    continue
                #test
            try:
                self.process_url(target_url)
            except Exception as e:
                #If queue is empty currently, wait.
                if threadSettings.thread_debug:
                    print ("[*]" + str(e))
                try:
                    self.process_url(target_url)
                except:
                    time.sleep(threadSettings.WaitWhenQueueEmptyInterval)
                    continue
                #print ("[*]Queue is empty!")
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
        parser.set_same_domain(True)
        if parser.need2feed:
            parser.feed(searcher.text)
            
        #Example : img and pdf.
        next_links_url = parser.link_list
        resources_url  = parser.img_list + parser.pdf_list
        #Rearrange resources_url according to 
        #Needed resources types.
        self.generatenextlinks(next_links_url)
        self.deal_resources(resources_url)
        
    def setflag(self,flag):
        
        self.flag = flag
    
    def generatenextlinks(self,next_links):
        
        if len(next_links) == 0:
            return
        for url in next_links:
            mutex_link.acquire()
            if Requester.check_if_visited(url) == 1:
                #print ("[*]Link " + url + " has been visited.")
                mutex_link.release()
            else:   
                Requester.mark_as_visited(url)
                mutex_link.release()
                #print ("[*] Put " + url + " in Link , mark as visited.")
                try:
                    threadQueue.add(url)
                    #time.sleep(0.03)
                    if threadSettings.thread_debug:
                        print("worker" + self.flag + "[*]Put " + url + " in working_queue.")
                except Exception as e:
                    print (e) 
    
    def deal_resources(self, resources_list):
        
        if len(resources_list) == 0:
            return 
        for url in resources_list:
            mutex_res.acquire()
            if  Requester.check_if_resvisited(url) == 1:
                #print ("[*]Res: " + url + " has been visited.")
                mutex_res.release()
            else:
                Requester.mark_as_resvisited(url)
                mutex_res.release()
                #print ("[*] Put " + url + " in res , mark as visited.")
                try:
                    threadSettings.result_queue.put("filename: " + url)
                    if threadSettings.thread_debug:
                        print("worker" + self.flag + "[*]Put " + url + " in res_queue.")
                    #time.sleep(0.03)
                    
                except Exception as e:
                    print (e) 
        