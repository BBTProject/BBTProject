#-*- coding:utf-8 -*-

import Requester
import logs
#import filter
import time
import urllib.parse

#requests Module Test Pass
#print requests.get('http://www.scut.edu.cn')
#logger Module Test Pass
#Testing Shared-Queue Now.

if __name__ == '__main__':
    
    try:
        a = 1/0
    except Exception as e:
        print ("[*] " + str(e))
    print (3/2)
    url = "http://www.scut.edu.cn/index.php?a=1&c=2&x=3a"
    res = ('www.scut.edu.cn', 'http',  '/index.php', '', 'a=1&c=2&x=3a', '')
    #res.query = "barbecue"
    print (urllib.parse.urlparse(url))
    
    for i in range(100):
        t= Requester.Requester()
        
    
    