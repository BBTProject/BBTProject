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

        self.resource_pattern=re.compile('.+?\.(\w+?)$')

        html_type=['html','htm','jsp','xhtml','asp','aspx','php','shtml','nsp','cgi','stm','shtm','perl']
        domain_postfix=['com','cn','net','org','gov','edu','cc','cx','wang','xin','top','tech','org','red',
                                'pub','ink','info','hk','xyz','win','tech','int','tv','tw','jp','eu','biz','name',
                                'pro','museum','coop','aero','us','uk']

        self.html_type=dict([(k,True) for k in html_type])
        self.domain_postfix=dict([(k,True) for k in domain_postfix])


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

    def get_link_type(self,link):
        match=self.resource_pattern.match(link)
        l_type=None
        try:
            l_type=match.group(1)
        except:
            pass
        if l_type and len(l_type) < 5 and l_type not in self.html_type and l_type not in self.domain_postfix:
            return l_type
        else:
            return None

    def place_on_file(self,kind,uri):
        if kind in ['jpg','jpeg','jpe','bpm','png','gif']:
            self.imgs.append(uri)
            return

        if kind in ['doc','docx']:
            self.docs.append(uri)
            return

        if kind in ['ppt','pptx']:
            self.ppts.append(uri)
            return

        if kind in ['xls','xlsx']:
            self.xlss.append(uri)
            return

        if kind in ['mp3','wmv']:
            self.mp3s.append(uri)
            return

        if kind in ['mp4','rmvb','rm','avi']:
            self.mp4s.append(uri)
            return

        self.others.append(uri)


    def classify(self,content_type,value):
        # print(content_type)
        if not value:
            return

        if not content_type:
            l_type=self.get_link_type(value)
            if not l_type:
                self.links.append(self.format_uri(value))
            else:
                self.place_on_file(l_type,self.format_uri(value))
            return

        if content_type == 'text/html':
            self.links.append(self.format_uri(value))
            return


        if content_type in self.ignore_type:
            return
            
        if content_type == 'application/pdf':
            self.pdfs.append(self.format_uri(value))
            return

        if content_type in ['application/x-jpg','application/x-jpe','application/x-bmp'] or 'image' in content_type:
            print(content_type)
            self.imgs.append(self.format_uri(value))
            return


        if content_type in ['application/ms-word','application/x-word']:
            self.docs.append(self.format_uri(value))
            return

        if content_type in ['application/x-ppt','application/vnd.ms-powerpoint']:
            self.ppts.append(self.format_uri(value))
            return


        if content_type in ['application/vnd.ms-excel','application/x-xls']:
            self.xlss.append(self.format_uri(value))
            return


        if 'audio' in content_type:
            self.mp3s.append(self.format_uri(value))
            return

        if content_type in ['application/vnd.rn-realmedia','application/vnd.rn-realmedia-vbr'] or 'video' in content_type:
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

if __name__ == '__main__':
    p=Myparser('http://www.scut.edu.cn')
    p.classify(None,'http://aaljw/ahowe/atjwo/aeoklshowroatid=wpir.cnx')
    print(p.img_list)
    print(p.link_list)
    print(p.other_list)
    
