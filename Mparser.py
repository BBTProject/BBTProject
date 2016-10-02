#-*- coding:utf-8 -*-

from html import parser
import re

class Myparser(parser.HTMLParser):
    def __init__(self,url):
        parser.HTMLParser.__init__(self)
        self.links = []
        self.scripts=[]
        self.imgs=[]
        self.others=[]
        self.pdfs=[]
        self.docs=[]
        self.ppts=[]
        self.xlss=[]
        self.mp3s=[]
        self.mp4s=[]

        self.need2feed=True

        self.url=url
        self.node=url.split('/')
        self.node.pop(1)
        
        if len(self.node) > 2:
            self.node=self.node[:-1]

        self.same_domain=False

        self.ignore_type=["text/css"]

    def check_response(self,response):
        
        if response:
            content_type=response.getheader('Content-Type')
            if content_type and 'html' not in content_type:
                self.need2feed=False
                self.classify(content_type,response.geturl())
        else:
            self.need2feed=False

    def set_same_domain(self,flag=True):
        self.same_domain=flag

    def format_uri(self,uri):
        if uri.startswith('http'):
            if self.same_domain and self.node[1] not in uri:
                return
            else:
                return uri
        if uri.startswith('{'):
            return
        if uri.startswith('/'):
            return self.node[0]+'//'+self.node[1]+uri
        if uri.startswith('../../'):
            value=self.node[0]+'//'
            for i in self.node[1:-2]:
                value+=i+'/'
            value+=uri.replace('../../','')
            return value
        if uri.startswith('../'):
            value=self.node[0]+'//'
            for i in self.node[1:-1]:
                value+=i+'/'
            value+=uri.replace('../','')
            return value
        if uri=="":
            return self.url
        current_uri=self.node[0]+'//'
        for i in self.node[1:]:
            current_uri+=i+'/'
        return current_uri+uri


    def handle_starttag(self, tag, attrs):
        #print "Encountered the beginning of a %s tag" % tag
        # print('init')
        if tag == "img":
            if len(attrs) == 0: pass
            else:
                # print(attrs)
                for (variable,value) in attrs:
                    if variable == "src":
                        self.imgs.append(self.format_uri(value))
            return


        if tag == "script":
            if len(attrs) == 0: pass
            else:
                for (variable,value) in attrs:
                    if variable == "src":
                        self.scripts.append(self.format_uri(value))
            return

        if len(attrs) == 0: pass
        else:
            content_type=None
            link=None
            for (variable,value) in attrs:
                if variable == 'type' :
                    content_type=value
                if variable == 'src':
                    link=self.format_uri(value)
                if variable == 'href':
                    link=self.format_uri(value)
            self.classify(content_type,link)
            # print(attrs)


    def classify(self,content_type,value):
        # print(content_type)
        if not value:
            return

        if not content_type or content_type == 'text/html':
            self.links.append(self.format_uri(value))
            return

        if content_type in self.ignore_type:
            return
            
        if content_type == 'application/pdf':
            self.pdfs.append(self.format_uri(value))
            return

        if content_type == 'application/x-jpg' or content_type ==  'image/jpeg' or content_type ==  'application/x-jpe':
            #print(content_type)
            self.imgs.append(self.format_uri(value))
            return


        if content_type == 'application/ms-word' or content_type == 'application/x-word':
            self.docs.append(self.format_uri(value))
            return

        if content_type == 'application/x-ppt' or content_type ==  'application/vnd.ms-powerpoint':
            self.ppts.append(self.format_uri(value))
            return


        if content_type == 'application/vnd.ms-excel' or content_type ==  'application/x-xls':
            self.xlss.append(self.format_uri(value))
            return


        if content_type == 'audio/mp3':
            self.mp3s.append(self.format_uri(value))
            return

        if content_type == 'video/mpeg4':
            self.mp4s.append(self.format_uri(value))
            return


        if content_type == 'application/vnd.rn-realmedia-vbr':
            self.mp4s.append(self.format_uri(value))
            return


        if content_type == 'video/avi':
            self.mp4s.append(self.format_uri(value))
            return

        else:
            self.others.append(self.format_uri(value))

    @property
    def link_list(self):
        temp=set(self.links)
        if None in temp:
            temp.remove(None)
        return list(temp)

    @property
    def img_list(self):
        temp=set(self.imgs)
        if None in temp:
            temp.remove(None)
        return list(temp)

    @property
    def script_list(self):
        temp=set(self.scripts)
        if None in temp:
            temp.remove(None)
        return list(temp)


    @property
    def other_list(self):
        temp=set(self.others)
        if None in temp:
            temp.remove(None)
        return list(temp)


    @property
    def pdf_list(self):
        try:
            temp=set(self.pdfs)
            if None in temp:
                temp.remove(None)
            return list(temp)
        except:
            return []


    @property
    def doc_list(self):
        try:
            temp=set(self.docs)
            if None in temp:
                temp.remove(None)
            return list(temp)
        except:
            return []

    @property
    def ppt_list(self):
        try:
            temp=set(self.ppts)
            if None in temp:
                temp.remove(None)
            return list(temp)
        except:
            return []


    @property
    def xls_list(self):
        try:
            temp=set(self.xlss)
            if None in temp:
                temp.remove(None)
            return list(temp)
        except:
            return []

    @property
    def mp3_list(self):
        try:
            temp=set(self.mp3s)
            if None in temp:
                temp.remove(None)
            return list(temp)
        except:
            return []

    @property
    def mp4_list(self):
        try:
            temp=set(self.mp4s)
            if None in temp:
                temp.remove(None)
            return list(temp)
        except:
            return []

    #to be add func like above


    
