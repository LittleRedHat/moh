# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
# import pymongo
from scrapy.exceptions import DropItem
from scrapy.conf import settings
from urlparse import urlparse,urljoin
import urllib
import hashlib
from bs4 import BeautifulSoup
import os
import traceback
import sys
reload(sys)
sys.setdefaultencoding('utf8')
from elasticsearch import Elasticsearch
import base64
import html2text

from crawl.items import ResourceItem
from crawl.spiders.moh_spider import configure

class ElasticsearchPipeline(object):
    def __init__(self):
        self.es = Elasticsearch(hosts=settings['ES_HOSTS'])
    def process_item(self,item,spider):
        if not item or isinstance(item,DropItem):
            return

        if item.get('rtype') == 'html':
            doc = dict(item)
            doc['content'] = h2t(doc['content'])
            doc['type'] = doc['rtype']
            del doc['rtype']
            # doc['content']=base64.b64encode(doc['content'])
            # doc['content']="this is a test"
            self.es.index(index='crawler',doc_type='articles',id=hashlib.md5(doc['url']).hexdigest(),body=doc,timeout='60s')
        elif item.get('rtype') == 'attachment':
            doc = dict(item)
            doc['data']=base64.b64encode(doc['content'])
            doc['type'] = doc['rtype']
            del doc['rtype']
            del doc['content']
            # doc['data']=doc['content']
            # doc['content']="this is a test"
            self.es.index(index='crawler',doc_type='articles',id=hashlib.md5(doc['url']).hexdigest(),body=doc,pipeline='attachment',timeout='60s')
        return item

def h2t(html):
    try:
        h = html2text.HTML2Text()
        return h.handle(html)
    except:
        return html





# class MongoPipeline(object):
    
#     def __init__(self):
#         connection = pymongo.MongoClient(
#             settings["MONGO_HOST"],
#             settings["MONGO_PORT"]
#         )
#         self.db =connection[settings['MONGO_DB']]

#     def update_or_insert(self,collections,article):
#         origin = collections.find_one({'url':article['url']})
#         if not origin:
#             article['last_md5'] = article['md5'] 
#             collections.insert_one(article)

#         elif origin['md5'] != article['md5']:
#             article['last_md5'] = origin['md5']
#             collections.update({'_id':origin.get('_id')},article)
        
                
        
    
#     def process_item(self,item,spider):
#         if not item:
#             return DropItem()

#         if item.get('type') == 'html':
            
#             article = dict(item)
#             # article['content'] = bson.binary.Binary(article['content']) 
#             article = {k: v.decode('unicode_escape') for k,v in article.iteritems()}

#             collections = self.db['articles']
#             self.update_or_insert(collections,article)
            
#         elif item['type'] == 'attachment':
#             attachment = dict(item)
#             attachment['content'] = bson.binary.Binary(attachment['content']) 
#             # print type(attachment['content'])
#             # attachment = {k: v.decode('unicode_escape') for k,v in attachment.iteritems()}
#             collections = self.db['attachments']
#             self.update_or_insert(collections,attachment)
            
#         return item
    
class FilePipeline(object):
    def __init__(self):
        self.output_dir = settings['DATA_OUTPUT']

    # def map_name_from_url(self,url):


    def process_item(self,item,spider):
        if not item or isinstance(item,DropItem):
            return
        ## asset handler
        if item.get('rtype') == 'asset':
            url = item['url']
            url = urllib.unquote(url)
            content = item.get('content')

            parse_result = urlparse(url)

            # url =  parse_result.netloc + parse_result.path
            # not update already exist resource 
            mine_dir,output_name= self.map_url_to_dirs(url)
            mine_output_path = os.path.join(mine_dir,output_name)
            self.output_content(url,content)
            return

        next_item = ResourceItem()
        url = item['url']
        url = urllib.unquote(url)
        content = item.get('content')
        next_item['url'] = url
        next_item['content']=content
        next_item['rtype']= item.get('rtype') or ''
        next_item['title'] = item.get('title') or ''
        next_item['location']=item.get('location') or ''
        next_item['language'] = item.get('language') or ''
        next_item['publish'] = item.get('publish') or '1970-01-01T00:00:00Z'
        #print item.get('publish')
        next_item['nation'] = item.get('nation') or ''
        next_item['keywords']=item.get('keywords') or ''
        netloc = urlparse(url).netloc

        # for all html, it musts be update
        if item.get('rtype') == 'html':
            # try:
            #     decode_content = content.decode('utf-8')
            # except:
            #     try:
            #         decode_content = content.decode('str_escape')
            #     except:
            #         try:
            #             decode_content = content.decode('unicode_escape')
            #         except:
            #             decode_content = content

            decode_content = content
            md5 = hashlib.md5(decode_content).hexdigest()
            key = hashlib.md5(url).hexdigest()
            # mine_dir,_ = self.map_url_to_dirs(url)
            mine_dir,modified_name= self.map_url_to_dirs(url)
            modified_name = key+'_'+modified_name 
            mine_output_path = os.path.join(mine_dir,modified_name)
            next_item['md5']=md5
            next_item['local_url'] = mine_output_path

            domain = []
            if item.get('nation') and configure.get(item.get('nation')):
                c = configure.get(item.get('nation'))
                domain = c.get('allowed_domains')

            try:
                soup = BeautifulSoup(decode_content,'lxml')
                # modify hrefs
                hrefs = soup.find_all('a')
                base = soup.find('base')
                if base and base.get('href'):
                    base_href = base.get('href')
                    base['href'] = ''
                    base = base_href
                else:
                    base = None

                for item in hrefs:
                    href = item.get('href')
                    http_url = self.gen_http_url(url,href,base)
                    if http_url and url_in_domain(http_url,domain):
                        http_url = urllib.unquote(http_url)     
                        dir,path_name = self.map_url_to_dirs(http_url)
                        key = hashlib.md5(http_url).hexdigest()
                        path_name = key +'_'+path_name
                        your_output_path = os.path.join(dir,path_name)
                        relpath = os.path.relpath(your_output_path,mine_dir)
                        # if href.startswith('http'):
                        #     print "modify href",href,url,http_url,relpath
                        item['href']=relpath

                # modify css js image
                javascripts = soup.find_all('script')
                for item in javascripts:
                    src = item.get('src')
                    http_url = self.gen_http_url(url,src,base)
                    if http_url and url_in_domain(http_url,domain):
                        http_url = urllib.unquote(http_url)
                        dir,path_name= self.map_url_to_dirs(http_url)
                        your_output_path = os.path.join(dir,path_name)
                        relpath = os.path.relpath(your_output_path,mine_dir)
                        item['src']=relpath
                        
                
                styles = soup.find_all('link')
                for item in styles:
                    href = item.get('href')
                    http_url = self.gen_http_url(url,href,base)
                    if http_url and url_in_domain(http_url,domain):
                        http_url = urllib.unquote(http_url)
                        dir,path_name= self.map_url_to_dirs(http_url)
                        your_output_path = os.path.join(dir,path_name)
                        relpath = os.path.relpath(your_output_path,mine_dir)
                        item['href']=relpath

                images = soup.find_all('img')
                for item in images:
                    src = item.get('src')

                    http_url = self.gen_http_url(url,src,base)
                    if http_url and url_in_domain(http_url,domain):
                        http_url = urllib.unquote(http_url)
                        dir,path_name= self.map_url_to_dirs(http_url)
                        your_output_path = os.path.join(dir,path_name)
                        relpath = os.path.relpath(your_output_path,mine_dir)
                        item['src']=relpath
                self.output_content(url,str(soup),modified_name)
                next_item['content'] = str(soup)
            
            except Exception,e:
                print e
                #self.output_content(url,item['content'],modified_name)

            return next_item 
           
        elif item.get('rtype') == 'attachment':
            
            key = hashlib.md5(url).hexdigest()
            # mine_dir,_ = self.map_url_to_dirs(url)
            mine_dir,modified_name = self.map_url_to_dirs(url)
            modified_name = key+'_'+modified_name 

            mine_output_path = os.path.join(mine_dir,modified_name)

            # not update exist attachment
            if os.path.exists(mine_output_path):
                return

            md5 = hashlib.md5(content).hexdigest()

            next_item['md5']=md5
            next_item['local_url'] = mine_output_path

            self.output_content(url,content,modified_name)
            return next_item
            
        
       
    def isAbsolutePath(self,url):
        if not url:
            return False
        try:
            parse_result = urlparse(url)
            if url.startswith('/') or parse_result.scheme:
                return True
            else:
                return False
        except:
            traceback.print_exc()
        return False

    def gen_http_url(self,source_url,dest_url,base):
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
        
    def output_content(self,url,content,modified_name = None):
        if content:
            output_dir_from_url,output_name= self.mkdirs_from_url(url)
            if modified_name:
                output_name = modified_name
            try:
                with open(os.path.join(output_dir_from_url,output_name),'wb') as fp:
                    fp.write(content)
            except:
                print output_dir_from_url,output_name
    

    def map_url_to_dirs(self,url):
        
        parse_result = urlparse(url)
        base_dir = parse_result.netloc
        path = parse_result.path
        root,file = os.path.split(path)
        if root != '' and root.startswith('/'):
            root = root[1:]
        output_dir_from_url = os.path.join(base_dir,root)
        output_name = file
        if parse_result.query:
            output_name = output_name + '%3f' + parse_result.query
        return output_dir_from_url,output_name

    def mkdirs_from_url(self,url):
        output_dir_from_url,output_name = self.map_url_to_dirs(url)
        output_dir_from_url = os.path.join(self.output_dir,output_dir_from_url)
        if not os.path.exists(output_dir_from_url) or not os.path.isdir(output_dir_from_url):
            os.makedirs(output_dir_from_url)
        return output_dir_from_url,output_name


def url_in_domain(url,domain):
    try:
        netloc = urlparse(url).netloc
        for item in domain:
            if item in netloc:
                return True
        return False
    except:
        return True
if __name__ == '__main__':
    pass
    

