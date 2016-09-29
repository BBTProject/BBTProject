from urllib import request,parse
import http.cookiejar
import re
import chardet
import zlib
from Mparser import Myparser
import os

#if the request headers add 'Accept-Encoding': 'gzip,deflate' ,then this func is need
def decodeGZip(rawPageData):
    if rawPageData.info().get(u"Content-Encoding") == "gzip":
        try:
            page_content = zlib.decompress(rawPageData.read(), 16 + zlib.MAX_WBITS)
            print('已解压')
        except zlib.error as ziperror:
            print('解压出错')
            print('出错解压页面:' + rawPageData.geturl())
            print ('错误信息：')
            print (zlib.error)
            return ''
    else:
        page_content = rawPageData.read()
    return page_content

def decode(content,encoding):
	if isinstance(content,bytes):
		try:
			content = str( content,encoding=encoding,errors='replace')
		except:
			content = str( content,errors='replace')
	return content

def apparent_encoding(content):
	if not isinstance(content,bytes):
		return 
	try:
		encoding=chardet.detect(content)['encoding']
	except:
		return 'utf-8'
	if encoding:
		return encoding
	else:
		return 'utf-8'

def retrieve(url,filename,path):
	try:
		os.mkdir
		r=request.urlopen(url)
		f=r.read()
		File = open( path+filename,"wb" )
		File.write(f)
		File.close()
	except Exception as e:
		print(e)



class search():
	"""docstring for spider"""
	def __init__(self):
		self.url = ''

		self.content=''

		self.response=None

		self.cookie=http.cookiejar.LWPCookieJar()
		self.cookie_support=request.HTTPCookieProcessor(self.cookie)
		self.opener=request.build_opener(self.cookie_support,request.HTTPHandler)
		request.install_opener(self.opener)

		self.headers={'User-Agent':"Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
		    		 'Connection': 'keep-alive','Content-Type': 'application/x-www-form-urlencoded'}



	def get(self,url,timeout=8):

		self.headers['Referer']=url               
		self.headers['Origin']=url
		self.url=url
		self.content=""
		self.response=None

		req=request.Request(url,headers=self.headers)       

		try:
			self.response=self.opener.open(req,timeout=timeout)      

			# help(response)

			self.url=self.response.geturl()

			

		except Exception as e:
			print(e)
		else:
			pass
		finally:
			pass

	@property
	def text(self):
		if self.response:
			self.content = decodeGZip(self.response)       #解压或decode，得到str形式的html
			content_type=self.response.getheader('Content-Type')
			pattern=re.compile(r'.+?charset=(.+?)$')
			# print((content_type))
			try:
				match=pattern.match(content_type)
				encoding=match.group(1)
				# print(encoding)
			except:
				encoding=apparent_encoding(self.content)
			
			return decode(self.content,encoding)
		else:
			return ""
	


if __name__ == '__main__':
	#first of all , the url form must be correct
	s=search()
	s.get('http://jcta.alljournals.ac.cn/cta_cn/ch/reader/create_pdf.aspx?file_no=CCTA160019&flag=1&journal_id=cta_cn&year_id=2016')
	p=Myparser(s.url)
	p.check_response(s.response)

	#set the rule to fliter the url, default is False
	p.set_same_domain(True)

	if p.need2feed:
		p.feed(s.text)

	print(p.link_list)
	print(p.img_list)
	print(p.pdf_list)
	print(p.doc_list)
	print(p.other_list)

	for i in p.pdf_list:
		retrieve(i,'pdf2.pdf','')
