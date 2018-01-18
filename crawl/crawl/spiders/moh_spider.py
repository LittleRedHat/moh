# !bin/python
# -*- coding: utf-8 -*-
import scrapy
from scrapy import signals
from scrapy.conf import settings
from urlparse import urlparse, urljoin
import os
import urllib
import tinycss
import re
import time
import datetime
from datetime import timedelta
import json
from crawl.items import ResourceItem
from summa import keywords
import sys
try:
    reload(sys)
    sys.setdefaultencoding('utf-8')
except:
    pass
from textrank4zh import TextRank4Keyword
import html2text
import codecs
import hashlib
from crawl.cache import r
from c import *

class MohSpider(scrapy.Spider):

    name = 'moh'

    def __init__(self, domain=None, debug=None, debug_url=None, update=False,max_html_update=100,max_html_list=20,html_crawl=0,html_update=30,attachment_update=1000,asset_update =1000,*args, **kwargs):

       super(MohSpider, self).__init__()
       params = configure[domain]
       self.allowed_domains = params['allowed_domains']
       self.site_url = params['site_url']
       self.output_dir = settings['DATA_OUTPUT']
       if debug_url:
           self.start_urls = [debug_url]
       else:
           self.start_urls = params['start_urls']
    #    self.rules = params['rules'] or []
       self.listRules = params.get('listRules') or []
       self.excludes = params.get('excludes') or []
       self.publish = params.get('publish') or []
       self.language = params.get('language') or ''
       self.nation = domain
       self.debug = debug

       self.update = update
       self.max_html_update = int(max_html_update)
       self.html_update = int(html_update)
       self.max_html_list = int(max_html_list)
       self.attachment_update = int(attachment_update)
       self.asset_update = int(asset_update)
       self.html_crawl = int(html_crawl)
       self.now = datetime.datetime.now()
       self.detail_count = 0
       self.list_count = 0

    def get_url_rule(self,url):

        for rule in self.excludes:
            if re.match(rule, url):
                return None,0
        for listRule in self.listRules:
            rule = listRule['rule']
            if re.match(rule,url):
                return listRule,1
            detailRules = listRule['detailRules']
            for detailRule in detailRules:
                rule = detailRule['rule']
                if re.match(rule,url):
                    return detailRule,2
        

        if url in self.start_urls:
            return None,3

        return None,0

    def url_in_rule(self,url):
        flag = False
        for rule in self.rules:
            if re.match(rule, url):
                flag = True
                break
        for rule in self.excludes:
            if re.match(rule, url):
                flag = False
                break
        if url in self.start_urls:
            flag = True
        return flag

    

    def load_history(self):
        if self.debug:
            history_file = os.path.join(settings['HISTORY_DIR'],self.nation + '-debug.json')
        else:
            history_file = os.path.join(settings['HISTORY_DIR'],self.nation + '.json')
        if os.path.exists(history_file):
            return json.load(codecs.open(history_file,'r'))
        else:
            return {}
            
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(MohSpider, cls).from_crawler(crawler, *args, **kwargs)
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        # crawler.signals.connect(spider.spider_error,  signal=signals.spider_error)
        # crawler.signals.connect(spider.request_dropped,  signal=signals.request_dropped)
        
        return spider

    def spider_closed(self,spider):
        # self.save_history()
        pass
    
    # def spider_error(self,response,spider):
    #     print 'error for spider'
    #     url = response.url
    #     last_update = datetime.date.today()
    #     record = {'error':True,'last_error':last_update.strftime('%Y-%m-%d'),'url':url}
    #     spider.save_record(url,record)

    # def request_dropped(self,request,spider):
    #     print 'error for request'
    #     url = request.url
    #     last_update = datetime.date.today()
    #     record = {'error':True,'last_error':last_update.strftime('%Y-%m-%d'),'url':url}
    #     spider.save_record(url,record)

    

    def save_history(self):
        if self.debug:
            history_file = os.path.join(settings['HISTORY_DIR'],self.nation + '-debug.json')
        else:
            history_file = os.path.join(settings['HISTORY_DIR'],self.nation + '.json')
        if self.history:
            json.dump(self.history,codecs.open(history_file,'w','utf-8'))

    def errback_httpbin(self, failure):
        url = failure.request.url
        last_update = datetime.date.today()
        record = {'error':True,'last_error':last_update.strftime('%Y-%m-%d'),'url':url}
        self.save_record(url,record)

    def content_allowed(self,content_type):
        for item in ALLOWED_FILE_DOWNLOAD:
            if item in content_type:
                return True
        return False

    def start_requests(self):
        for url in self.start_urls:
            if self.nation in ['rw']:
                yield scrapy.Request(url,callback=self.parse,errback=self.errback_httpbin,cookies={'_accessKey2':'CD2we/sGT5LdZuwhvlgz3y4zkhvdvTTh'})
            ## il need post
            if self.nation in ['il']:
                yield scrapy.Request(url,callback=self.parse,errback=self.errback_httpbin,method='POST')
            else:
                yield scrapy.Request(url,callback=self.parse,errback=self.errback_httpbin)


    def should_crawl(self,record):
        ## 更新模式下只爬取一定数目详情页
        if self.update and self.detail_count > self.max_html_update:
            return False
        ## 更新模式下只爬取一定数目列表页
        if self.update and self.list_count > self.max_html_list:
            return False

        if not record:
            return True
        error = record.get('error') or 'False'
        if record.get('error') == 'True':
            return True

        if record.get('type') == 'attachment':
            delta = timedelta(days = self.attachment_update)
            content_type = record.get('content_type') or '&&&&&'
            if not self.content_allowed(content_type):
                return False

        ## 对于网页都应该爬取，但是不一定要重新索引
        elif record.get('type') == 'html':

            delta = timedelta(days = self.html_crawl)
            content_type = record.get('content_type') or '&&&&&'
            if not self.content_allowed(content_type):
                return False

            rule,url_type = self.get_url_rule(record.get('url'))
            if not url_type:
                return False
            # if not self.url_in_rule(record.get('url')):
            #     return False
            
        elif record.get('type') == 'asset':
            delta = timedelta(days = self.asset_update)

        else:
            return False
            # content_type = record.get('content_type') or '&&&&&'
            # if not self.content_allowed(content_type):
            #     return False
        
        last_update = record.get('last_update')
        if not last_update:
            return True
        last_update_date = datetime.datetime.strptime(last_update,'%Y-%m-%d').date()
        now = datetime.date.today()

        if now - last_update_date < delta:
            return False
        else:
            return True
    def should_update(self,record):

        if not record:
            return True
        # print 'record is not null'
        error = record.get('error') or 'False'
        if record.get('error') == 'True':
            return True
        # print "not error"


        if record.get('type') == 'attachment':
            delta = timedelta(days = self.attachment_update)
            content_type = record.get('content_type') or '&&&&&'
            if not self.content_allowed(content_type):
                return False
        elif record.get('type') == 'html':
            delta = timedelta(days = self.html_update)
            content_type = record.get('content_type') or '&&&&&'
            if not self.content_allowed(content_type):
                return False
            rule,url_type = self.get_url_rule(record.get('url'))
            if not url_type in [1,2,3]:
                return False
            if url_type == 2 and self.html_update != 0 and self.update:
                return False

            # if not self.url_in_rule(record.get('url')):
            #     return False
        elif record.get('type') == 'asset':
            delta = timedelta(days = self.asset_update)
            # print "type is asset"

        else:
            return False
            # content_type = record.get('content_type') or '&&&&&'
            # if not self.content_allowed(content_type):
            #     return False
        
        last_update = record.get('last_update')
        if not last_update:
            return True
        # print "last_update is not null"
        last_update_date = datetime.datetime.strptime(last_update,'%Y-%m-%d').date()
        now = datetime.date.today()
        # print last_update_date,now,delta,last_update_date + delta

        if now - last_update_date < delta:
            return False
        else:
            return True
        

        
    def get_record(self,url):
        url = urllib.unquote(url)
        md5 = hashlib.md5(url).hexdigest()
        key = 'moh:'+self.nation +':'+md5
        return r.hgetall(key)
        
    def save_record(self,url,saved_record):
        record = self.get_record(url)
        url = urllib.unquote(url)
        md5 = hashlib.md5(url).hexdigest()
        key = 'moh:'+self.nation+':'+md5
        # should_update = self.should_update(record)
        # if should_update:
            # print dict(record.items()+saved_record.items())
        r.hmset(key,saved_record)

    def parse(self, response):
        '''
        parse html to extract useful link and assets

        '''
        # now = datetime.datetime.now()
        # history_save_interval = timedelta(minutes = 5)
        # if self.now + history_save_interval < now:
        #     self.now = now
        #     self.save_history()


        record = self.get_record(response.url)
        
        content_type = None
        saved_record = None

        if record and record.get('content_type'):
            content_type = record.get('content_type').strip()
        elif response.headers and response.headers.get('Content-Type'):
            ct = response.headers.get('Content-Type').split(';')
            if len(ct):
                content_type = ct[0].strip()
        
        if content_type and ('text/html' in content_type):
            # print response.url
            # 过滤掉不相关的页面

            rule,url_type = self.get_url_rule(response.url)
            if not url_type:
                last_update = datetime.date.today()
                saved_record = {'url':response.url,'type':'html','content_type':content_type,'last_update':last_update.strftime('%Y-%m-%d'),'valid':False}
                self.save_record(response.url,saved_record)
                return

            if url_type == 1:
                self.list_count = self.list_count + 1




            resource = ResourceItem()
            resource['url'] = response.url
            resource['rtype'] = 'html'
            resource['location'] = self.site_url
            resource['language'] = self.language_inference(response)
            resource['publish'] = '1970-01-01T00:00:00Z'
            resource['nation'] = self.nation
            resource['content_type'] = content_type
            if hasattr(response, 'encoding'):
                resource['encoding'] = response.encoding

            

            title_from_meta = response.meta.get('title') or ''
            resource['title'] = title_from_meta

            resource['content'] = response.text
            
            if url_type == 2:
                
                
                resource['publish'] = self.publish_time_inference(response)
                content = response.xpath(rule.get('content'))

                if len(content):
                    content = content[0]
                    ct = content.xpath('.').extract_first()
                    # content = content.xpath('normalize-space(string(.))').extract_first()
                    
                    text = self.h2t(ct)
                    if not text:
                        text = content.xpath('normalize-space(string(.))').extract_first()

                    if self.debug:
                        print 'content is ',text
                        
                    resource['saved_content'] = text
                    resource['keywords'] = json.dumps(self.text2keywords(text,resource['language'],keywords_num=5))

                if rule.get('title'):
                    title = response.xpath(rule.get('title'))
                    if len(title):
                        title = title[0].xpath('normalize-space(string(.))').extract_first()
                        if title:
                            resource['title'] = title
            

            # saved_record = {'content_type':content_type,'url':resource['url'],'type':resource['rtype']}
            # self.save_record(response.url,saved_record)

            should_update = self.should_update(record)
            if not self.debug and should_update:
                self.detail_count =  self.detail_count + 1
                # print '(url,language,publish,title)',resource['url'],resource['language'],resource['publish'],resource['title']
                yield resource

            # last_update = datetime.date.today()
           
            print '*'*40
            print '(url,type,language,publish,title)',resource['url'],url_type,resource['language'],resource['publish'],resource['title']
            
            ## get html base
            base = response.xpath('//base[@href]/@href').extract()
            if len(base):
                base = base[0]
            else:
                base = None
           
            stylesheets = response.xpath(
                '//link[(@type="text/css") or (@rel="stylesheet")]/@href').extract()
            
            
            for stylesheet in stylesheets:
                http_url = self.gen_http_url(response.url, stylesheet,base)
                if http_url:
                    request = scrapy.Request(http_url, callback=self.style_parse,errback=self.errback_httpbin)
                    _record = self.get_record(http_url)
                    should_crawl = self.should_crawl(_record)
                    if should_crawl:
                        yield request

            javascripts = response.xpath('//script[@src]/@src').extract()
            for javascript in javascripts:
                http_url = self.gen_http_url(response.url,javascript,base)
                if http_url:
                    request = scrapy.Request(http_url, callback=self.assets_parse,errback=self.errback_httpbin)
                    
                    _record = self.get_record(http_url)

                    should_crawl = self.should_crawl(_record)
                    if should_crawl:
                        
                        yield request

            images = response.xpath('//img[@src]/@src').extract() or []
            input_images = response.xpath(
                '//input[@type="image"]/@src').extract() or []
            images.extend(input_images)
            for img in images:
                img_http_url = self.gen_http_url(response.url,img,base)
                if img_http_url:
                    request = scrapy.Request(img_http_url, callback=self.assets_parse,errback=self.errback_httpbin)
                    _record = self.get_record(img_http_url)
                    should_crawl = self.should_crawl(_record)
                    if should_crawl:
                        yield request


            links = response.xpath('//a[@href]')
            for link in links:
                link_text = link.xpath('@href').extract()
                if len(link_text):
                    link_text = link_text[0]
                else:
                    link_text = None
                link_title = link.xpath('normalize-space(string(.))').extract()
                if len(link_title):
                    link_title = link_title[0]
                else:
                    link_title = ''
                http_url = self.gen_http_url(response.url,link_text,base)

                if http_url:
                    if self.nation in ['il']:
                        request = scrapy.Request(http_url,callback=self.parse,meta={'title':link_title},errback=self.errback_httpbin,method='POST')
                    else:
                        request = scrapy.Request(http_url,callback=self.parse,meta={'title':link_title},errback=self.errback_httpbin)
                    
                    _record = self.get_record(http_url)
                    should_crawl = self.should_crawl(_record)
                    if should_crawl:
                        yield request
                    
        elif content_type and self.content_allowed(content_type):  
            resource = ResourceItem()
            resource['url'] = response.url
            resource['content'] = response.body
            resource['rtype'] = 'attachment'
            resource['location'] = self.site_url
            resource['nation'] =  self.nation
            resource['content_type'] = content_type
            if hasattr(response,'encoding'):
                resource['encoding'] = response.encoding
            if response.meta.get('title'):
                resource['title'] = response.meta.get('title')
            else:
                resource['title'] = ''

            should_update = self.should_update(record)

            if (not self.debug) and should_update:
                yield resource

            print '*'*40
            print '(url,type)',resource['url'],resource['rtype']
            
            # last_update = datetime.date.today()
            saved_record = {'content_type':content_type,'url':resource['url'],'type':resource['rtype']}
            self.save_record(response.url,saved_record)
        else:
            last_update = datetime.date.today()
            saved_record = {'url':response.url,'content_type':content_type,'last_update':last_update.strftime('%Y-%m-%d')}
            self.save_record(response.url,saved_record)
        
        

    def assets_parse(self, response):
        '''
            parse images/js/...
        '''
        resource = ResourceItem()
        resource['url'] = response.url
        resource['content'] = response.body
        resource['rtype'] = 'asset'
        resource['location'] = self.site_url
        # resource['encoding'] = response.get('encoding')

        record = self.get_record(response.url)
        should_update = self.should_update(record)

        if not self.debug and should_update:
            yield resource
        print '*'*40
        print '(url,type)',resource['url'],resource['rtype']
            
        # last_update = datetime.date.today()
        # self.save_record(response.url,{'url':resource['url'],'type':resource['rtype']})
           
    def language_inference(self,response):
        '''
            html language inference from lang attribute
        '''
        language = response.xpath("//html[@lang]/@lang[1]").extract()
        if not language:
            if self.language:
                language = self.language
            else:
                language = 'en'
        else:
            language = language[0]
        return language

    def publish_time_inference(self,response):
        try:
            rule,url_type = self.get_url_rule(response.url)
            # print rule
            if url_type == 2:
                t = None
                for item in rule['publish']:
                    t = response.xpath(item['rule']).extract()
                    if len(t):
                        for s in t:
                            if s.strip(' \r\n\t'):
                                t = s
                                break
                        t = t.strip(' \r\n\t')
                        extra = item.get('extra')
                        if extra:
                            t = extra(t)
                    else:
                        continue
                    try:
                        t = time.strptime(t,item["format"])
                    except Exception,e:
                        print e
                        t = None
                    if t:
                        t = time.strftime("%Y-%m-%dT%H:%M:%SZ",t)
                        break
                return t
            else:
                return None
        except Exception,e:
            print e
            
            return None

    def style_parse(self, response):
        '''
            css parser to extract import css and image
        '''
        url = response.url
        content = response.text
        resource = ResourceItem()
        resource['url'] = url
        resource['content'] = content
        resource['rtype'] = 'asset'
        resource['location'] = self.site_url
        # resource['encoding'] = response.get('encoding')


        record = self.get_record(url)
        should_update = self.should_update(record)
        if not self.debug and should_update:
            yield resource

        print '*'*40
        print '(url,type)',resource['url'],resource['rtype']
            

        #   last_update = datetime.date.today()
        #   self.save_record(response.url,{'url':resource['url'],'type':resource['rtype']})
        

        stylesheet = tinycss.make_parser().parse_stylesheet(content)

        for item in stylesheet.rules: 
            if isinstance(item,tinycss.css21.ImportRule):
                uri = item.uri
                http_url = self.gen_http_url(url,uri,None)

                if http_url:
                    record = self.get_record(http_url)
                    should_crawl = self.should_crawl(record)
                    request = scrapy.Request(http_url,self.style_parse,errback=self.errback_httpbin)
                    if should_crawl:
                        yield request
                    
            elif hasattr(item,'declarations'):
                for decl in getattr(item,'declarations'):
                    for decl_val in getattr(decl,'value'):
                        if getattr(decl_val,'type') == u'URI':
                            uri = getattr(decl_val,'value')
                            image_url = self.gen_http_url(url,uri,None)
                            if image_url:
                                record = self.get_record(image_url)
                                should_crawl = self.should_crawl(record)
                                request = scrapy.Request(image_url,self.assets_parse,errback=self.errback_httpbin)
                                if should_crawl:
                                    yield request 

    def gen_http_url(self,source_url,dest_url,base):
        '''
            generate absolute url 
        '''
        if not dest_url:
            return None
        elif dest_url.startswith('#'):
            return None
        elif dest_url.startswith('mailto'):
            return None
        elif dest_url.startswith('javascript:'):
            return None
        elif base:
            return urljoin(base,dest_url).encode('utf-8')
        else:
            return urljoin(source_url,dest_url).encode('utf-8')

    def h2t(self,html):
        try:
            h = html2text.HTML2Text()
            h.ignore_links = True
            h.skip_internal_links = True
            h.bypass_tables = False
            h.ignore_images = True
            return h.handle(html)
        except Exception,e:
            print e
            return None
    def text2keywords(self,text,language,keywords_num=5):
        try:
            # 中文网页关键词提取,用textrank4zh
            if 'zh' in language:
                tr4w = TextRank4Keyword()
                tr4w.analyze(text=text, lower=True, window=2)
                return tr4w.get_keywords(keywords_num=keywords_num, word_min_len=1)
            # 其他网页关键词提取，用summa textrank
            else:
                k = keywords.keywords(text,scores=True)
                return k[0:keywords_num]
        except Exception,e:
            pass










if __name__ == '__main__':
    pass
    
    
        
            
