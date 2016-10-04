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
from SqliTester import Sqlitester
import monitor
import urllib.parse

#py : for adding urls.
#logger     :  for documenting loggs.
#filter    :   for parsing things needed.
#Requester:    for launching requests.
mutex_res = threading.Lock()
mutex_link= threading.Lock()
mutex_test= threading.Lock()

class worker(threading.Thread):
    
    def run(self):
        
        self.times = 0
        self.work()
        
    def work(self):
        
        while 1:
            #Move counter to counter + 1
            self.runtime_counter()
            #Time to run Monitor for this worker.
            if  self.counter == threadSettings.WorkerPer_Monitor:
                #reset counter.
                self.counter = 0
                monitor_ = monitor.monitor()
                monitor_.setflag(self.flag)
                monitor_.start()
            if  threadQueue.checkIfAlive(self.flag) != 1 :
                LOG.WriteLog("[*]Worker " + self.flag + " is dead.")
                if threadSettings.thread_debug:
                    print ("[*]Worker " + self.flag + " is dead.")
                #time for worker to have a rest
                break
            #print ("[*]Worker is working.")
            try:
                #Get url from threadqueue
                target_url = threadQueue.threadqueue.get(False)
                LOG.WriteLog("[*]" + self.flag + " working")
            except Exception as e:
                if threadSettings.thread_debug:
                    print ("[*]" + str(e))
                self.times += 1
                if  self.times == threadSettings.SleepTimeBeforeEnd:
                    threadQueue.disableworker(self.flag)
                    break
                else:
                    time.sleep(threadSettings.WaitWhenQueueEmptyInterval)
                    continue
            try:
                self.process_url(target_url)
            except Exception as e:
            #If queue is empty currently, wait.
                if threadSettings.thread_debug:
                    #print ("[*]Processurl Wrong!!!")
                    print ("[*]Worker Error: " + str(e))
                LOG.WriteLog("[*]Worker Error: " + str(e))
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
        parser   = Myparser(searcher.url)
        parser.check_response(searcher.response)
        if threadSettings.SqlInjectionTest_Mode:
            parser.set_same_domain(False)
        else:
            parser.set_same_domain(threadSettings.IS_SAME_DOMAIN)
        #parser.set_same_domain(True)
        if parser.need2feed:
            parser.feed(searcher.text)
        
        #Example : img and pdf.
        next_links_url = parser.link_list
        test_lst = []
        self.generatenextlinks(next_links_url)
        if  threadSettings.SqlInjectionTest_Mode:
        #resources_url  = parser.img_list + parser.pdf_list
            temp_urls       = parser.link_list +\
            parser.pdf_list + parser.doc_list + parser.other_list
            for url in temp_urls:
                if self.sqlifilter(url) == True:
                    test_lst.append(url)
            #Rearrange resources_url according to
            #Needed resources types.
            #print ("[*]Sqli Run here.")
            self.launchsqlitest(test_lst)
            #self.deal_resources(resources_url)
        else:
            resources_lst = []
            Res           = []
            #Divide resources more clearly
            for element in threadSettings.target_filetype:
                if 'pdf' in element:
                    resources_lst += parser.pdf_list
                if 'jpg' in element:
                    resources_lst += parser.img_list
                if 'doc' in element:
                    resources_lst += parser.doc_list
            if  len(threadSettings.search_keywords[0]) ==0:
                #print (str(resources_lst))
                Res = resources_lst
            else:
                for res in resources_lst:
                    for key in threadSettings.search_keywords:
                        if  key in res:
                            Res.append(res)
            #print (str(Res))    
            self.deal_resources(Res)
            
    def setflag(self,flag):
        
        self.flag    = flag
        self.counter = 0
    
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
                        print("worker" + self.flag + "[*]Put nexturl in queue.")
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
                        print("worker" + self.flag + "[*]Put url in result.")
                    #time.sleep(0.03)
                except Exception as e:
                    print (e) 
    
    def launchsqlitest(self, urls):
        
        for url in urls:
            Sqlitester(url)
    
    def runtime_counter(self):
        
        self.counter += 1
    
    def sqlifilter(self,url):
        
        #means no desired params in target_url
        if len(urllib.parse.urlparse(url).query) == 0:
            return False
        else:
            #if url not tested:
            mutex_test.acquire()
            if Requester.check_if_tested(url) == 0:
                Requester.mark_if_tested(url)
                mutex_test.release()
                return True
            else:
                mutex_test.release()
                return False
            