#-*- coding:utf-8 -*-

import requests
import logs
import urllib.parse

class Requester:
    
    headers ={"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
                           "User-Agent"         :"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:48.0) Gecko/20100101 Firefox/48.0",
                           "connection"         :"keep-alive",
                           "Cache-Control"      :"max-age=0",
                           "Accept-Encoding"    :"gzip,deflate" #Crucial ELement
                            }
    session = requests.session()
    visited_links = {}
    visited_resources = {}
    visited_sqlipoints= {}
    
    @staticmethod
    def send(url , params, method):
        
        #print ('[*] Testing ' + url)
        #Add Log here.
        if  method is "post":
            return Requester.session.post(url, data = params, headers = Requester.headers)
        elif method is "get":
            return Requester.session.get(url, headers = Requester.headers)
        
    @staticmethod
    def check_if_visited(url):
        
        if url in Requester.visited_links:
            return 1
        else:
            return 0
    
    @staticmethod
    def mark_as_visited(url):
        
        Requester.visited_links[url] = 1
    
    @staticmethod
    def check_if_resvisited(url):
        
        if url in Requester.visited_resources:
            return 1
        else:
            return 0
    
    @staticmethod
    def mark_as_resvisited(url):
        
        Requester.visited_resources[url] = 1
    
    @staticmethod
    def mark_if_tested(url):
        
        urlpart = urllib.parse.urlparse(url)
        temp    = urlpart.scheme + urlpart.netloc +\
        urlpart.path + urlpart.params
        Requester.visited_sqlipoints[temp] = 1
    
    @staticmethod
    def check_if_tested(url):
        
        urlpart = urllib.parse.urlparse(url)
        temp    = urlpart.scheme + urlpart.netloc +\
        urlpart.path + urlpart.params
        if temp in Requester.visited_sqlipoints:
            return 1
        else:
            return 0
        
if __name__ == '__main__':
    
    Requester   = Requester()
    print (Requester.send('http://www.scut.edu.cn', None, 'get'))
    