# !bin/python
# -*- coding: utf-8 -*-
import scrapy
from scrapy.conf import settings
from urlparse import urlparse, urljoin
import os
import sys
import tinycss
import re
import time
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


def ae_time_sub(text):
    p = r'(.*?)([0-9]{2})(.*)'
    m = re.match(p,text)
    groups = m.groups()
    if len(groups) >= 3:
        return groups[1] + groups[2]
    else:
        return None
        
def iq_time_sub(text):
    p = r'(.*?)([0-9]{2}:[0-9]{2}:[0-9]{2})(.*?)([0-9]{4}-[0-9]{2}-[0-9]{2})(.*)'
    m = re.match(p,text)
    groups = m.groups()
    if len(groups) >= 5:
        return groups[3]+" "+groups[1]
    return None

def cz_time_sub(text):
    p = r'(.*?)([0-9]{2}\.[0-9]{2}\.[0-9]{4})(.*?)'
    m = re.match(p,text)
    groups = m.groups()
    if len(groups) >= 2:
        return groups[1]
    return None




configure = {
    "output_dir": '/var/www/html',
    # 韩国
    "kr": {
        'allowed_domains': ['mohw.go.kr'],
        'site_url': 'http://www.mohw.go.kr',
        'start_urls': ['http://www.mohw.go.kr/eng/sg/ssg0111ls.jsp?PAR_MENU_ID=1001&MENU_ID=100111&page=1'],
        'rules': [r'(.*)ssg0111vw\.jsp(.*)', r'(.*)ssg0111ls\.jsp(.*)'],
        'publish':[{"rule":"//table[@class='view']/tbody/tr[2]/td[1]/text()","format":"%Y-%m-%d"}],
    },
    # 阿联酋
    'ae':{
        'allowed_domains':['mohap.gov.ae'],
        'site_url':'http://www.mohap.gov.ae',
        'start_urls':['http://www.mohap.gov.ae/en/AwarenessCenter/Pages/posts.aspx','http://www.mohap.gov.ae/ar/Aboutus/Pages/PublicHealthPolicies.aspx','http://www.mohap.gov.ae/en/MediaCenter/Pages/news.aspx','http://www.mohap.gov.ae/en/MediaCenter/Pages/events.aspx','http://www.mohap.gov.ae/en/OpenData/Pages/default.aspx','http://www.mohap.gov.ae/en/OpenData/Pages/health-statistics.aspx'],
        'rules':[r'(.*)/en/AwarenessCenter/Pages/post\.aspx(.*)',r'(.*)/FlipBooks/PublicHealthPolicies/(.*)/mobile/index\.html(.*)',r'(.*)/en/MediaCenter/Pages/news\.aspx(.*)',r'(.*)/en/OpenData/Pages/default\.aspx(.*)',r'(.*)/en/OpenData/Pages/health-statistics\.aspx(.*)',r'(.*)/en/MediaCenter/Pages/EventDetail.aspx(.*)'],
        'publish':[{"rule":"//div[@class='newsdetailstitle']/p[@class='metadate']/span[2]/text()","format":"%d %b %Y"},{"rule":"//div[@class='contentblock']/p[@class='metadata']/span[1]/text()","format":"%d %A, %B, %Y","extra":ae_time_sub},{"rule":"//div[@class='newsdetailstitle']/p[@class='metadate']/span[2]/text()","format":"%d %B %Y"}]
    },
    # 埃及
    'eg':{
        'allowed_domains':['mohp.gov.eg'],
        'site_url':'http://www.mohp.gov.eg',
        'start_urls':['http://www.mohp.gov.eg/News.aspx','http://www.mohp.gov.eg/Events.aspx','http://www.mohp.gov.eg/Courses.aspx','http://www.mohp.gov.eg/cancer/'],
        'rules':[r'(.*)/NewsDetails\.aspx(.*)',r'(.*)/EventDetails\.aspx(.*)',r'(.*)/coursedetailes\.aspx(.*)'],
        'language':'ar_EG',
        'publish':[{"rule":"//div[@class='redate']/text()","format":"%d %B %Y"}]

    },
    # 伊拉克
    'iq':{
        'allowed_domains':['moh.gov.iq'],
        'site_url':'https://www.moh.gov.iq',
        'start_urls':['https://moh.gov.iq'],
        'rules':[r'(.*)/index\.php\?name=News(.*)'],
        'language':'ar_IQ',
        'publish':[{'rule':"//table[@class='shadow_table']/tbody/center/table[@dir='rtl']/span[@dir='rtl']/p[2]/text()","format":'%Y-%m-%d %H:%M:%S',"extra":iq_time_sub}]

    },

    # 以色列
    "il": {
        'allowed_domains': ['health.gov.il'],
        'site_url': 'http://www.health.gov.il',
        'start_urls': ['https://www.health.gov.il/English/News_and_Events/Spokespersons_Messages/Pages/default.aspx'],
        'rules': [r'(.*)English/News_and_Events/Spokespersons_Messages/Pages/default\.aspx(.*)', r'(.*)English/News_and_Events/Spokespersons_Messages/Pages/(.*)'],
        'publish':[{"rule":"//table[@class='ContentLayoutNoLeftSideMainTable']/td[@class='ContentLayoutNoLeftLeftSid']/div[@class='HealthMMdDivLayout']/div[@class='HealthPRDate']/text()","format":"%d/%m/%Y %H:%M"}]
    },

    
   
    # 卡塔尔
    'qa':{
        'allowed_domains':['moph.gov.qa'],
        'site_url':'https://www.moph.gov.qa',
        'start_urls':['https://www.moph.gov.qa/news/news','https://www.moph.gov.qa/events/events','https://www.moph.gov.qa/health-strategies/national-health-strategy'],
        'rules':[r'(.*)/news(.*)',r'(.*)/events(.*)',r'(.*)/health-strategies(.*)'],
        'publish':[{"rule":"//article[@class='newsDetails']/dd[@class='pubDate']/abbr/text()","format":"%d %B %Y"}]


    },
    # 斯洛伐克
    'sk':{
        'allowed_domains':['uvzsr.sk'],
        'site_url':'http://www.uvzsr.sk',
        'start_urls':['http://www.uvzsr.sk/en/index.php/documents','http://www.uvzsr.sk/en/index.php/expert-departments'],
        'rules':[r'(.*)/en/index\.php/documents'],
        'publish':[]
    },
    # 波兰
    'pl':{
        'allowed_domains':['mz.gov.pl'],
        'site_url':'http://www.mz.gov.pl',
        'start_urls':['http://www.mz.gov.pl/aktualnosci','http://www.mz.gov.pl/leki/aktualnosci-leki/','http://www.mz.gov.pl/zdrowie-i-profilaktyka/'],
        'rules':[r'(.*)/aktualnosci/page(.*)',r'(.*)/aktualnosci(.*)',r'(.*)/zdrowie-i-profilaktyka(.*)',r'(.*)/leki/aktualnosci-leki(.*)'],
        'publish':[{"rule":"//*[@id='content-wrapper']/p[@class='news-date']/strong/text()","format":"%d.%m.%Y"}]
    },
     # 保加利亚
    'bg':{
        'allowed_domains':['mh.government.bg'],
        'site_url':'http://www.mh.government.bg',
        'start_urls':['http://www.mh.government.bg/bg/novini/aktualno/','http://www.mh.government.bg/bg/politiki/','http://www.mh.government.bg/bg/evropeyski-programi/tekushti-programi-i-proekti/'],
        'rules':[r'(.*)/bg/novini/aktualno(.*)',r'(.*)/bg/evropeyski-programi/tekushti-programi-i-proekti(.*)',r'(.*)/bg/politiki(.*)'],
        'publish':[{"rule":"//div[@id='top']/ul[@class='newsdate']/time[@datetime]/@datetime","format":"%Y-%m-%dT%H:%M:%S+03:00"}]
    },
    # 斯洛文尼亚
    'si':{
        'allowed_domains':['mz.gov.si',],
        'site_url':'http://www.mz.gov.si',
        'start_urls':['http://www.mz.gov.si/si/medijsko_sredisce/intervjuji','http://www.mz.gov.si/si/medijsko_sredisce/sporocila_za_medije','http://www.mz.gov.si/si/medijsko_sredisce/koledar_dogodkov','http://www.mz.gov.si/si/medijsko_sredisce/poslanska_vprasanja','http://www.mz.gov.si/si/pogoste_vsebine_za_javnost/izdaja_zdravil_prek_medmrezja'],
        'rules':[r'(.*)/si/medijsko_sredisce(.*)',r'(.*)/si/pogoste_vsebine_za_javnost(.*)'],
        'publish':[{"rule":"//div[@id='mainContainer']/div[@class='newsdate']/text()","format":"%d. %m. %Y"}]
    },

    # 克罗地亚
    'hr':{
        'allowed_domains':['zdravstvo.gov.hr'],
        'site_url':'https://zdravstvo.gov.hr/',
        'start_urls':['https://zdravstvo.gov.hr/vijesti/8','https://zdravstvo.gov.hr/dokumenti/10','https://zdravstvo.gov.hr/savjetovanje-sa-zainteresiranom-javnoscu-1475/1475','https://zdravstvo.gov.hr/najcesca-pitanja-i-odgovori/1479','https://zdravstvo.gov.hr/strategije-planovi-i-izvjesca/2396'],
        'rules':[r'(.*)/vijesti/8(.*)',r'(.*)/vijesti(.*)',r'(.*)/pristup-informacijama(.*)'],
        'publish':[{"rule":"//div[@class='article_left']/li[@class='time_info']/text()","format":"Objavljeno: %d.%m.%Y."}]

    },
    # 匈牙利
    'hu':{
        'allowed_domains':['enum.hu'],
        'site_url':'http://www.eum.hu',
        'start_urls':[''],
        'rules':[],

    },
    # 捷克
    'cz':{
        'allowed_domains':['mzcr.cz'],
        'site_url':'http://www.mzcr.cz',
        'start_urls':['http://www.mzcr.cz','http://www.mzcr.cz/Odbornik','http://www.mzcr.cz/Verejne'],
        'rules':[r'(.*)/dokumenty(.*)',r'(.*)/Odbornik(.*)',r'(.*)/Verejne(.*)'],
        'publish':[{'rule':"//*[@id='right-column-content']/div[@class='box-ostrance']/p[1]/text()","format":'%d.%m.%Y','extra':cz_time_sub}]

    },

    # 中国
    "cn": {
        'allowed_domains':['moh.gov.cn'],
        'site_url':'http://www.moh.gov.cn',
        'start_urls':[''],
        'language':'zh'



    },
     # 澳大利亚
    'au':{
        'allowed_domains':['health.gov.au'],
        'site_url':'http://www.health.gov.au',
        'start_urls':['http://www.health.gov.au/internet/main/publishing.nsf/Content/health-publicat.htm','http://www.health.gov.au/internet/main/publishing.nsf/Content/Research+&+Statistics-1','http://www.health.gov.au/internet/main/publishing.nsf/Content/CurrentIssues'],
        'rules':[r'(.*)/internet/main/publishing\.nsf/Content/(.*)'],
        'excludes':[r'(.*)internet/main/publishing\.nsf/Content/health-overview\.htm(.*)',r'(.*)internet/main/publishing.nsf/Content/health-central\.htm(.*)',r'(.*)internet/main/publishing\.nsf/Content/Budget-1(.*)',r'(.*)/internet/main/publishing\.nsf/Content/Listing\+of\+Tenders\+and\+Grants-1(.*)',r'(.*)/internet/main/publishing\.nsf/Content/health-eta2\.htm(.*)',r'(.*)internet/main/publishing\.nsf/Content/reporting-fraud-misconduct-compliance(.*)',r'(.*)/internet/main/publishing\.nsf/Content/foi-about(.*)',r'(.*)internet/main/publishing\.nsf/Content/public-interest-disclosure(.*)',r'(.*)internet/main/publishing\.nsf/Content/health-contracts-index\.htm(.*)',r'(.*)/internet/main/publishing\.nsf/Content/health-eta2\.htm(.*)',r'(.*)/internet/main/publishing\.nsf/Content/social-media-channels(.*)',r'(.*)/internet/main/publishing\.nsf/Content/Career\+Opportunities-1(.*)',r'(.*)/internet/main/publishing\.nsf/Content/health-pubs-calendar-index\.htm(.*)',r'(.*)/internet/main/publishing\.nsf/Content/health-history\.htm(.*)',r'(.*)/internet/main/publishing\.nsf/Content/Australian\+Health\+Ministers%27\+Conference-1(.*)',r'(.*)/internet/main/publishing\.nsf/Content/Council\+of\+Australian\+Governments(.*)',r'(.*)/internet/main/publishing\.nsf/Content/Agreements-1(.*)',r'(.*)/internet/main/publishing\.nsf/Content/eHealth(.*)',r'(.*)/internet/main/publishing\.nsf/Content/programs-initiatives-menu(.*)',r'(.*)/internet/main/publishing\.nsf/Content/campaign_certification_statements-lp(.*)',r'(.*)/internet/main/publishing\.nsf/Content/Australian\+Health\+Ministers%27\+Conference-1(.*)',r'(.*)/internet/main/publishing\.nsf/Content/Council\+of\+Australian\+Governments(.*)',r'(.*)/internet/main/publishing\.nsf/Content/Departmental\+media\+releases\+and\+speeches-1(.*)',r'(.*)/internet/main/publishing\.nsf/Content/health-mediarel-subscribe-index\.htm',r'(.*)/internet/main/publishing\.nsf/Content/Ministers-1(.*)',r'(.*)/internet/main/publishing\.nsf/Content/government-responses(.*)']
        
    },


    'ws':{
        'allowed_domains':[''],
        'site_url':'http://www.health.gov.ws',
        'start_urls':'',
        'rules':[],
        'publish':[]
    }
}


class MohSpider(scrapy.Spider):

    name = 'moh'

    def __init__(self, domain=None, *args, **kwargs):

       super(MohSpider, self).__init__()
       params = configure[domain]
       self.allowed_domains = params['allowed_domains']
       self.site_url = params['site_url']
       self.output_dir = configure['output_dir']
       self.start_urls = params['start_urls']
       self.rules = params['rules'] or []
       self.excludes = params.get('excludes') or []
       self.publish = params.get('publish') or []
       self.language = params.get('language') or ''
       self.nation = domain
       

    def parse(self, response):
        '''
        parse html to extract useful link and assets
        '''
        if response.headers and response.headers['Content-Type'] and ('text/html' in response.headers['Content-Type']):
            # print response.url

            # 过滤掉不相关的页面
            flag = False
            for rule in self.rules:
                if re.match(rule, response.url):
                    flag = True
                    break
            for rule in self.excludes:
                if re.match(rule, response.url):
                    flag = False
                    break
            
            if response.url in self.start_urls:
                flag = True
            if not flag:
                return
            
            resource = ResourceItem()
            resource['url'] = response.url
            resource['content'] = response.body
            resource['type'] = 'html'
            resource['location'] = self.site_url
            resource['language'] = self.language_inference(response)
            resource['publish'] = self.publish_time_inference(response)
            resource['nation'] = self.nation
            text = self.h2t(response)
            resource['keywords'] = self.text2keywords(text,resource['language'],keywords_num=5)

            print response.url
            if response.meta.get('title'):
                title = response.meta.get('title')
            else:
                title = response.xpath('//title/text()').extract()
                if len(title):
                    title = title[0]
                else:
                    title = ''

            resource['title'] = title
            yield resource
            # return

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
                    link_title = '没有标题'
                http_url = self.gen_http_url(response.url,link_text)
                if http_url:
                    # print 'yield http url %s from %s'%(http_url,response.url)
                    # if http_url == 'http://www.mz.gov.pl/wp-content/uploads/2015/07/Wczesne-wykrywanie-dane-krajowe.ppt':
                    #     print 'yield http url %s from %s'%(http_url,response.url)
                    #     print 'link title is ',link_title
                    #     return
                    request = scrapy.Request(http_url,callback=self.parse,meta={'title':link_title})
                    yield request

            stylesheets = response.xpath(
                '//link[@type="text/css"]/@href').extract()
            for stylesheet in stylesheets:
                http_url = self.gen_http_url(response.url, stylesheet)
                if http_url:
                    yield scrapy.Request(http_url, callback=self.style_parse)
                    

            javascripts = response.xpath('//script[@src]/@src').extract()
            for javascript in javascripts:
                http_url = self.gen_http_url(response.url, javascript)
                if http_url:
                    yield scrapy.Request(http_url, callback=self.assets_parse)

            images = response.xpath('//img[@src]/@src').extract() or []
            input_images = response.xpath(
                '//input[@type="image"]/@src').extract() or []
            images.extend(input_images)
            for img in images:
                img_http_url = self.gen_http_url(response.url, img)
                if img_http_url:
                    yield scrapy.Request(img_http_url, callback=self.assets_parse)
        else:
            print response.url
            resource = ResourceItem()
            resource['url'] = response.url
            resource['content'] = response.body
            resource['type'] = 'attachment'
            resource['location'] = self.site_url
            resource['nation'] =  self.nation
            if response.meta.get('title'):
                resource['title'] = response.meta.get('title')
            else:
                resource['title'] = ''
            yield resource

    def assets_parse(self, response):
        '''
            parse images/js/...
        '''
        resource = ResourceItem()
        resource['url'] = response.url
        resource['content'] = response.body
        resource['type'] = 'asset'
        resource['location'] = self.site_url
        yield resource

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
        '''
            article publish time inference from defined rules, it is tightly with html structure  
        '''
        t = None
        for item in self.publish:
            t = response.xpath(item['rule']).extract()
            if t:
                t = t[0]
                t = t.strip(' \r\n')
                extra = item.get('extra')
                if extra:
                    t = extra(t)
            else:
                continue
            try:
                t = time.strptime(t,item["format"])
            except: 
                t = None
            if t:
                t = time.strftime("%Y-%m-%d %H:%M:%S",t)
                break
        return t

    def style_parse(self, response):
        '''
            css parser to extract import css and image
        '''
        print response.url
        url = response.url
        content = response.body
        resource = ResourceItem()
        resource['url'] = url
        resource['content'] = content
        resource['type'] = 'asset'
        resource['location'] = self.site_url
        yield resource
        
        try:
            decode_content = content.decode('utf-8')
        except:
            try:
                decode_content = content.decode('str_escape')
            except:
                try:
                    decode_content = content.decode('unicode_escape')
                except:
                    decode_content = content
        stylesheet = tinycss.make_parser().parse_stylesheet(decode_content)

        for item in stylesheet.rules: 
            if isinstance(item,tinycss.css21.ImportRule):
                uri = item.uri
                http_url = self.gen_http_url(url,uri)
                if http_url:  
                    yield scrapy.Request(http_url,self.style_parse)	
            elif hasattr(item,'declarations'):
                for decl in getattr(item,'declarations'):
                    for decl_val in getattr(decl,'value'):
                        if getattr(decl_val,'type') == u'URI':
                            uri = getattr(decl_val,'value')
                            image_url = self.gen_http_url(url,uri)
                            if image_url:
                                yield scrapy.Request(image_url,self.assets_parse)

   
    def gen_http_url(self,source_url,dest_url):
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
        else:
            return urljoin(source_url,dest_url)



    def h2t(self,response):
        try:
            html = response.text
            h = html2text.HTML2Text()
            return h.handle(html)
        except:
            pass
    def text2keywords(self,text,language,keywords_num=5):
        try:
            # 中文网页关键词提取,用textrank4zh
            if 'zh' in language:
                tr4w = TextRank4Keyword()
                tr4w.analyze(text=text, lower=True, window=2)
                return tr4w.get_keywords(keywords_num=keywords_num, word_min_len=1):
            # 其他网页关键词提取，用summa textrank
            else:
                k = keywords.keywords(text,scores=True)
                return k[0:keywords_num]
        except Exception,e:
            pass

        

if __name__ == '__main__':
    iq_time_sub("أرسلت بواسطة: أدارة الموقع | التاريخ: 2017-10-05 | الوقـت: 10:56:19 صباحا  | قراءة : 13")
    
        
            
