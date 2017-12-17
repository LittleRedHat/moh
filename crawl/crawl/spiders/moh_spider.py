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


def br_time_sub(text):
    p = r'(.*?), ([0-9]{1,2}) de (.*?) de ([0-9]{4}), ([0-9]{1,2})h([0-9]{2})(.*?)'
    m = re.match(p,text)
    groups = m.groups()
    br2en = ['ene','feb','mar','abr','may','jun','jul','agos','sep','oct','nov', 'dic']
    if len(groups) >= 6:
        month = groups[2]
        for key,en in enumerate(br2en):
            if en.lower() in month.lower():
                month = str(key + 1)
                break
        
        day = groups[1]
        year = groups[3]
        hour = groups[4]
        minute = groups[5]
        return year+'-'+month+'-'+day+' '+hour+":"+minute
    return None

def uy_time_sub(text):
    p = r'(.*?)([0-9]{1,2}) (.*?), ([0-9]{4})'
    m = re.match(p,text)
    groups = m.groups()
    br2en = ['ene','feb','mar','abr','may','jun','jul','agos','sep','oct','nov', 'dic']
    if len(groups) >= 4:
        month = groups[2]
        for key,en in enumerate(br2en):
            if en.lower() in month.lower():
                month = str(key + 1)
                break
        day = groups[1]
        year = groups[3]
        return year+'-'+month+'-'+day
    
def mx_time_sub(text):
    p = r'([0-9]{1,2}) de (.*) de ([0-9]{4})(.*?)'
    m = re.match(p,text)
    groups = m.groups()
    br2en = ['ene','feb','mar','abr','may','jun','jul','agos','sep','oct','nov', 'dic']
    if len(groups) >= 3:
        month = groups[1]
        for key,en in enumerate(br2en):
            if en.lower() in month.lower():
                month = str(key + 1)
                break
        day = groups[0]
        year = groups[2]
        return year+'-'+month+'-'+day
def ni_time_sub(text):
    p = r'(.*?) ([0-9]{1,2}) de (.*?)/([0-9]{4})'
    m = re.match(p,text)
    groups = m.groups()
    br2en = ['ene','feb','mar','abr','may','jun','jul','agos','sep','oct','nov', 'dic']
    if len(groups) >= 3:
        month = groups[2]
        for key,en in enumerate(br2en):
            if en.lower() in month.lower():
                month = str(key + 1)
                break
        day = groups[1]
        year = groups[3]
        return year+'-'+month+'-'+day    
# spanish_month=['enero','febrero','marzo','abril','mayo','junio','julio','agosto','septiembre','octubre','noviembre','diciembre']
fr_month = ['jan','fév','mars','avr','mai','juin','juillet','aoû','sept','oct','nov','déc']

def ma_time_sub(text):
    p = r'([0-9]{1,2}) (.*?) ([0-9]{2})'
    m = re.match(p,text)
    groups = m.groups()
    if len(groups) >= 3:
        month = groups[1]
        for key,en in enumerate(fr_month):
            if en.lower() in month.lower() or month.lower() in en.lower():
                month = str(key + 1)
                break
        day = groups[0]
        year = groups[2]
        return '20'+year+'-'+month+'-'+day 
  
def lr_time_sub(text):
    p = r'(.*?) (\w+) ([0-9]{1,2})(.*)([0-9]{4})'
    m = re.match(p,text)
    groups = m.groups()
    if len(groups) >= 5:
        month = groups[1]
        day = groups[2]
        year = groups[4]
        return year+','+month+','+day

def sc_time_sub(text):
    p = r'([0-9]{1,2})(.*?) (\w+) ([0-9]{4})'
    m = re.match(p,text)
    groups = m.groups()
    if len(groups) >=4:
        year = groups[3]
        month = groups[2]
        day = groups[0]
        return day+' '+month+' '+year




configure = {
   
    ##############################################
    # 亚洲
    ###############################################

    ## 中国 无规则也爬不下来，谜
    "cn": {
        'allowed_domains':['moh.gov.cn'],
        'site_url':'http://www.moh.gov.cn',
        'start_urls':[
                        'http://www.moh.gov.cn/zhuz/mtbd/list.shtml',
                        'http://www.moh.gov.cn/zhuz/xwfb/list.shtml'
                    ],
        'rules':[
                    r'(.*)/zhuz/mtbd/[0-9]{6}/(.*)',
                    r'(.*)/zhuz/xwfb/[0-9]{6}/(.*)',
                    r'(.*)/zhuz/mtbd/list(.*)',
                    r'(.*)/zhuz/xwfb/list(.*)'
                ],
        'language':'zh',
        'publish':[{'rule':"//div[@class='list']/div[@class='source']/span/text()",'format':'''发布时间：
            	%Y-%m-%d
            '''}]
    },

    # 蒙古 网址打开后不是蒙古卫生部
    'mn':{
        'allowed_domains':['moh.mn'],
        'site_url':'http://www.moh.mn'
    },

    # 韩国
    "kr": {
        'allowed_domains': ['mohw.go.kr'],
        'site_url': 'http://www.mohw.go.kr',
        'start_urls': ['http://www.mohw.go.kr/eng/sg/ssg0111ls.jsp?PAR_MENU_ID=1001&MENU_ID=100111&page=1'],
        'rules': [r'(.*)ssg0111vw\.jsp(.*)', r'(.*)ssg0111ls\.jsp(.*)'],
        'publish':[{"rule":"//table[@class='view']/tbody/tr[2]/td[1]/text()","format":"%Y-%m-%d"}],
    },

    # 日本 日期解析问题，未使用公历，格式，x-path不统一
    'jp':{
        'allowed_domains':['mhlw.go.jp'],
        'site_url':'http://www.mhlw.go.jp',
        'start_urls':['http://www.mhlw.go.jp/stf/new-info/index.html'],
        'rules':[r'(.*)stf/shingi2/(.*)', r'(.*)toukei/(.*)'],
        'publish':[
                    {'rule':"//div[@id='content']/div[@class='float-right']/table[@class='border t-margin']/tbody/tr/td/p[1]",
                    'format':'平成%y年%m月%d日（木）'},
                    {'rule':"//div[@id='content']/div[@class='float-right']/table[@class='border t-margin']/tbody/tr/td/p[1]",
                    'format':'平成%y年%m月%d日（水）'},
                    {'rule':"//div[@id='content']/div[@class='float-right']/table[@class='border t-margin']/tbody/tr/td/p[1]",
                    'format':'平成%y年%m月%d日（月）'},
                    {'rule':"//div[@id='content']/div[@class='float-right']/table[@class='border t-margin']/tbody/tr/td/p[1]",
                    'format':'平成%y年%m月%d日（金）'},
                    {'rule':"//div[@id='content']/div[@class='float-right']/table[@class='border t-margin']/tbody/tr/td/p[1]",
                    'format':'平成%y年%m月%d日（火）'}
                    ]
    },

    # 朝鲜 没有网址

    # 越南
    'vn':{
        'allowed_domains':['moh.gov.vn'],
        'site_url':'http://moh.gov.vn',
        'start_urls':['http://moh.gov.vn/News/Pages/TinHoatDongV2.aspx', 'http://emoh.moh.gov.vn/publish/home'],
        'rules':[r'(.*)/news/Pages/TinHoatDongV2\.aspx\?ItemID=(.*)', r'(.*)/publish/home\?documentId=(.*)'],
        'publish':[{'rule':"//p[@class='n-data']/text()",'format':'%d/%m/%Y'}]
    },

    # 老挝
    'la':{
        'allowed_domains':['moh.gov.la'],
        'site_url':'https://www.moh.gov.la',
        'start_urls':[
            'https://www.moh.gov.la/index.php/lo-la/2017-10-27-02-54-12/2017-10-27-03-08-18',
            'https://www.moh.gov.la/index.php/lo-la/2017-11-02-08-34-25/2017-11-25-10-36-28'    
        ],
        'rules':[r'(.*)/images//pdf/Reporting/(.*)', r'(.*)/index.php/lo-la/(.*)'],
        'publish':[]
    },

    # 柬埔寨 网站建设中
    'kh':{
        'allowed_domains':['moh.gov.kh'],
        'site_url':'http://moh.gov.kh'
    },

    # 缅甸
    'mm':{
        'allowed_domains':['mohs.gov.mm'],
        'site_url':'http://mohs.gov.mm/',
        'start_urls':[
            'http://mohs.gov.mm/Main/content/new/list?pagenumber=1&pagesize=9',
            'http://mohs.gov.mm/Main/content/annouancement/list?pagenumber=1&pagesize=9'
        ],
        'rules':[r'(.*)/Main/content/new/(.*)',r'(.*)/Main/content/annouancement/(.*)'],
        'publish':[
                    {'rule':"//div[@class='single-post-info']/span[@class='last-modified pull-right']/text()",
                        'format':'Last modified on %A, %d %b %y'}
                ]
    },
    

    # 泰国
    'th':{
        'allowed_domains':['moph.go.th'],
        'site_url':'https://www.moph.go.th',
        'start_urls':['https://ops.moph.go.th/public/index.php/news/public_relations'],
        'rules':[r'(.*)/public/index.php/news/read/(.*)'],
        'publish':[{'rule':"//div[@class='row category'][3]/div[@class='f-item']/text()",'format':'%d %m %Y'}]
    },

    # 菲律宾
    'ph':{
        'allowed_domains':['doh.gov.ph'],
        'site_url':'http://www.doh.gov.ph',
        'start_urls':['http://www.doh.gov.ph/news-clips'],
        'rules':[r'(.*)/sites/default/files/news_clips/(.*)']
    },

    # 马来西亚
    'my':{
        'allowed_domains':['moh.gov.my'],
        'site_url':'http://www.moh.gov.my',
        'start_urls':['http://www.moh.gov.my/'],
        'rules':[r'(.*)/index\.php/database_stores/store_view_page/(.*)'],
        'publish':[{'rule':"//table[@class='dataTableDetail']/tbody/tr[2]/td/text()",'format':'%d-%m-%Y'}]
    },

    # 印度尼西亚 日期中信息变化，无法解析
    'id':{
        'allowed_domains':['depkes.go.id'],
        'site_url':'http://www.depkes.go.id',
        'start_urls':['http://www.depkes.go.id/folder/view/01/structure-info-terkini.html'],
        'rules':[r'(.*)/article/view/[0-9]{11}/(.*)']
    },


    # 新加坡 日期解析问题
    'sg':{
        'allowed_domains':['moh.gov.sg'],
        'site_url':'https://www.moh.gov.sg',
        'start_urls':[
                        'https://www.moh.gov.sg/content/moh_web/home.html',
                        'https://www.moh.gov.sg/content/moh_web/home/diseases_and_conditions.html',
                        'https://www.moh.gov.sg/content/moh_web/home/pressRoom.html'
                    ],
        'rules': [r'(.*)/content/moh_web/home/pressRoom/(.*)', r'(.*)/content/moh_web/home/diseases_and_conditions/(.*)'],
        'publish':[
                    {'rule':"//div[@class='lastModify entryMeta parbase']/div[@class='entry-meta']/p[@class='dates-edit']/text()",'format':'''
            Last updated on %d %b %Y
          '''}
                ]
    },

    # 文莱 日期解析问题，格式复杂
    'bn':{
        'allowed_domains':['moh.gov.bn'],
        'site_url':'http://www.moh.gov.bn',
        'start_urls':['http://www.moh.gov.bn/SitePages/Latest%20News.aspx'],
        'rules':[r'(.*)/Lists/Latest%20news/NewDispForm\.aspx\?ID=(.*)'],
        'publish':[
                    {'rule':"//td[@class='ms-formbody']/div[@class]/p[last()]/text()",'format':'%d %B %Y'},
                    {'rule':"//td[@class='ms-formbody']/div[@class]/p[last()-1]/text()",'format':'%d %B %Y'}
                ]
    },

    # 东帝汶
    'tl':{
        'allowed_domains':['moh.gov.tl'],
        'site_url':'http://www.moh.gov.tl',
        'start_urls':['http://www.moh.gov.tl/?q=blog/1'],
        'rules':[r'(.*)/\?q=node/(.*)',r'(.*)/\?q=blog/1&page(.*)'],
        'publish':[{'rule':"//header/p[@class='submitted']/span/text()",'format':'%a, %d/%m/%Y - %H:%M'}]
    },

    # 尼泊尔 网页打不开
    'np':{
        'allowed_domains':['moh.gov.np'],
        'site_url':'http://moh.gov.np'
    },
    
    # 不丹
    'bt':{
        'allowed_domains':['health.gov.bt'],
        'site_url':'http://www.health.gov.bt',
        'start_urls':['http://www.health.gov.bt/category/news/'],
        'rules':[r'(.*)'],
        'publish':[{'rule':"//time[@class='entry-date published updated']/text()",'format':'%B %d, %Y'}],
        'excludes':[
                    r'(.*)/health-calendar/(.*)',
                    r'(.*)/scheduled-training/(.*)',
                    r'(.*)/category/procurement/(.*)',
                    r'(.*)/category/promotions/(.*)',
                    r'(.*)/category/studies/(.*)',
                    r'(.*)/category/trainings/(.*)',
                    r'(.*)/category/vacancy/(.*)',
                    r'(.*)/about/(.*)',
                    r'(.*)/downloads/(.*)',
                    r'(.*)/contact/(.*)',
                    r'(.*)/healths/gallery/(.*)',
                    r'(.*)/site-map/(.*)',
                    r'(.*)/search/(.*)',
                    r'(.*)/departments/(.*)'
                ]
    },

    # 印度
    'in':{
        'allowed_domains':['mofpi.nic.in'],
        'site_url':'http://www.mofpi.nic.in',
        'start_urls':['http://www.mofpi.nic.in/press-release'],
        'rules':[r'(.*)/sites/default/files/(.*)']
    },

    # 巴基斯坦
    'pk':{
        'allowed_domains':['nhsrc.gov.pk'],
        'site_url':'http://www.nhsrc.gov.pk',
        'start_urls':['http://www.nhsrc.gov.pk'],
        'rules':[r'(.*)/news_details(.*)'],
        'publish':[{'rule':"//div[@id='right-header-datetime']/text()",'format':"%Y-%m-%d"}]
    },

    # 孟加拉国
    'bd':{
        'allowed_domains':['mohfw.gov.bd'],
        'site_url':'http://www.mohfw.gov.bd',
        'start_urls':['http://www.mohfw.gov.bd/index.php?option=com_content&view=frontpage&Itemid=1&lang=en'],
        'rules':[r'(.*)/index.php\?option=com_content&view=article&id=(.*)']
    },

    # 斯里兰卡
    'lk':{
        'allowed_domains':['health.gov.lk'],
        'site_url':'http://www.health.gov.lk',
        'start_urls':['http://www.health.gov.lk/moh_final/english/others.php?pid=110'],
        'rules':[r'(.*)/moh_final/english/public/elfinder/files/publications/AHB/(.*)']
    },

    # 马尔代夫
    'mv':{
        'allowed_domains':['health.gov.mv'],
        'site_url':'http://www.health.gov.mv',
        'start_urls':['http://www.health.gov.mv/News'],
        'rules':[r'(.*)/News/(.*)'],
        'publish':[{'rule':"//div[@class='box news-box news-article']/div/time/sup/text()",'format':'%A, %B %d, %Y'}]
    },

    # 伊朗
    'ir':{
        'allowed_domains':['behdasht.gov.ir'],
        'site_url':'http://www.behdasht.gov.ir',
        'start_urls':['http://www.behdasht.gov.ir/index.jsp?siteid=1&fkeyid=&siteid=1&pageid=1508'],
        'rules':[r'(.*)/news/(.*)']
    },

    

    # 阿富汗
    'af':{
        'allowed_domains':['moph.gov.af'],
        'site_url':'http://www.moph.gov.af/fa',
        'start_urls':['http://moph.gov.af/fa/news'],
        'rules':[r'(.*)/fa/news/(.*)'],
        'publish':[{'rule':"//div[@class='postDate']/text()",'format':'%b %d, %Y'}]
    },

    # 沙特阿拉伯
    'sa':{
        'allowed_domains':['moh.gov.sa'],
        'site_url':'http://www.moh.gov.sa',
        'start_urls':['https://www.moh.gov.sa/Ministry/MediaCenter/News/Pages/default.aspx'],
        'rules':[r'(.*)/Ministry/MediaCenter/News/Pages/(.*)'],
        'publish':[{'rule':"//span[@id='ctl00_PlaceHolderMain_ctl04_lblDate']/text()",'format':'%y'}]
    },

    # 也门
    'ye':{
        'allowed_domains':['mophp-ye.org'],
        'site_url':'http://www.mophp-ye.org',
        'start_urls':['http://www.mophp-ye.org/english/news.html'],
        'rules':[r'(.*)/english/news\.html(.*)'],
        'publish':[{'rule':"//div[@id='content']/h4/text()",'format':'%B, %Y'}]
    },

    # 阿曼
    'om':{
        'allowed_domains':['moh.gov.om'],
        'site_url':'http://www.moh.gov.om',
        'start_urls':['https://www.moh.gov.om/en_US/ebola'],
        'rules':[r'(.*)/documents/(.*)']
    },

    # 阿联酋  时间解析问题
    'ae':{
        'allowed_domains':['mohap.gov.ae'],
        'site_url':'http://www.mohap.gov.ae',
        'start_urls':[
                        'http://www.mohap.gov.ae/en/AwarenessCenter/Pages/posts.aspx',
                        'http://www.mohap.gov.ae/ar/Aboutus/Pages/PublicHealthPolicies.aspx',
                        'http://www.mohap.gov.ae/en/MediaCenter/Pages/news.aspx',
                        'http://www.mohap.gov.ae/en/MediaCenter/Pages/events.aspx',
                        'http://www.mohap.gov.ae/en/OpenData/Pages/default.aspx',
                        'http://www.mohap.gov.ae/en/OpenData/Pages/health-statistics.aspx'
                    ],
        'rules':[
                    r'(.*)/en/AwarenessCenter/Pages/post\.aspx(.*)',
                    r'(.*)/FlipBooks/PublicHealthPolicies/(.*)/mobile/index\.html(.*)',
                    r'(.*)/en/MediaCenter/Pages/news\.aspx(.*)',
                    r'(.*)/en/OpenData/Pages/default\.aspx(.*)',
                    r'(.*)/en/OpenData/Pages/health-statistics\.aspx(.*)',
                    r'(.*)/en/MediaCenter/Pages/EventDetail.aspx(.*)'
                ],
        'publish':[
                    {"rule":"//div[@class='newsdetailstitle']/p[@class='metadate']/span[2]/text()","format":"%d %b %Y"},
                    {"rule":"//div[@class='contentblock']/p[@class='metadata']/span[1]/text()","format":"%d %A, %B, %Y","extra":ae_time_sub},
                    {"rule":"//div[@class='newsdetailstitle']/p[@class='metadate']/span[2]/text()","format":"%d %B %Y"},
                    {"rule":"//p[@class='metadate']/span/text()","format":"Health and Care / Published in %d %A, %B, %Y "}
                ]
    },


    # 卡塔尔
    'qa':{
        'allowed_domains':['moph.gov.qa'],
        'site_url':'https://www.moph.gov.qa',
        'start_urls':[
                        'https://www.moph.gov.qa/news/news',
                        'https://www.moph.gov.qa/events/events',
                        'https://www.moph.gov.qa/health-strategies/national-health-strategy'
                    ],
        'rules':[r'(.*)/news(.*)',r'(.*)/events(.*)',r'(.*)/health-strategies(.*)'],
        'publish':[
            {"rule":"//header/div[@class='newsDetailsListContainer']/dl[@class='newsDetailsList']/dd[@class='pubDate']/abbr/text()","format":"%d %B %Y"}
            ]


    },

    # 巴林
    'bh':{
        'allowed_domains':['moh.gov.bh'],
        'site_url':'https://www.moh.gov.bh',
        'start_urls':['https://www.moh.gov.bh/News'],
        'rules':[r'(.*)/News/Details/(.*)'],
        'publish':[{'rule':"//div[@id='renderbody']/div[@class='pull-right']/text()",'format':'%d/%m/%Y %H:%M:%S'}]
    },

    # 科威特 网页打不开
    'kw':{
        'allowed_domains':['moh.gov.kw'],
        'site_url':'http://www.moh.gov.kw'
    },

    # 土耳其
    'tr':{
        'allowed_domains':['saglik.gov.tr'],
        'site_url':'http://www.saglik.gov.tr',
        'start_urls':['http://www.saglik.gov.tr/EN,15463/news.html'],
        'rules':[r'(.*)/EN,15(.*)'],
        'publish':[{'rule':"//section[@class='date']/text()",'format':'UPDATED : %d/%m/%Y'}],
        'excludes':[
                    r'(.*)/minister\.html',
                    r'(.*)/deputy-minister\.html',
                    r'(.*)/undersecretariat\.html',
                    r'(.*)/history-of-the-ministry-of-health\.html',
                    r'(.*)/undersecretary-deputies\.html',
                    r'(.*)/ministerial-organization\.html',
                    r'(.*)/duties-and-powers\.html',
                    r'(.*)/institutional-policies\.html',
                    r'(.*)/units\.html',
                    r'(.*)/our-minister\.html',
                    r'(.*)/our-minister\.html',
                    r'(.*)/organization-chart\.html',
                    r'(.*)/management\.html',
                    r'(.*)/tasks\.html',
                    r'(.*)/mission-and-vision\.html',
                    r'(.*)/activities\.html',
                    r'(.*)/contact\.html'
                ]
    },

    # 叙利亚
    'sy':{
        'allowed_domains':['moh.gov.sy'],
        'site_url':'http://www.moh.gov.sy',
        'start_urls':['http://www.moh.gov.sy/Default.aspx?tabid=259&language=en-US'],
        'rules':[
                    r'(.*)/Default\.aspx\?tabid=259&language=en-US',
                    r'(.*)/Default\.aspx\?tabid=260&language=en-US',
                    r'(.*)/Default\.aspx\?tabid=261&language=en-US',
                    r'(.*)/Default\.aspx\?tabid=257&language=en-US',
                    r'(.*)/Default\.aspx\?tabid=288&language=en-US'
                ]
    },


    # 伊拉克
    'iq':{
        'allowed_domains':['moh.gov.iq'],
        'site_url':'https://www.moh.gov.iq',
        'start_urls':['https://moh.gov.iq'],
        'rules':[r'(.*)/index\.php\?name=News(.*)'],
        'language':'ar_IQ',
        'publish':[{'rule':"//table[@class='shadow_table']/tbody/center/table[@dir='rtl']/span[@dir='rtl']/p[2]/text()",
                    "format":'%Y-%m-%d %H:%M:%S',"extra":iq_time_sub}]

    },

    # 约旦 网站打不开
    'jo':{
        'allowed_domains':['moh.gov.jo'],
        'site_url':'http://www.moh.gov.jo',
        'start_urls':['http://www.moh.gov.jo/Pages/viewpage.aspx?pageID=262'],
        'rules':[r'(.*)']
    },

    # 巴勒斯坦 404
    'ps':{
        'allowed_domains':['pna.org'],
        'site_url':'http://www.pna.org/moh',
        'start_urls':['http://www.mohiraq.org/news.htm'],
        'rules':[r'(.*)/news/news(.*)']
    },


    # 以色列
    "il": {
        'allowed_domains': ['health.gov.il'],
        'site_url': 'http://www.health.gov.il',
        'start_urls': ['https://www.health.gov.il/English/News_and_Events/Spokespersons_Messages/Pages/default.aspx'],
        'rules': [
                    r'(.*)English/News_and_Events/Spokespersons_Messages/Pages/default\.aspx(.*)', 
                    r'(.*)English/News_and_Events/Spokespersons_Messages/Pages/(.*)'
                ],
        'publish':[{"rule":"//table[@class='ContentLayoutNoLeftSideMainTable']/td[@class='ContentLayoutNoLeftLeftSid']/div[@class='HealthMMdDivLayout']/div[@class='HealthPRDate']/text()","format":"%d/%m/%Y %H:%M"}]
    },

    # 黎巴嫩
    'lb':{
        'allowed_domains':['cas.gov.lb'],
        'site_url':'http://www.cas.gov.lb',
        'start_urls':['http://www.cas.gov.lb/'],
        'rules':[
                    r'(.*)/demographic-and-social-en(.*)',
                    r'(.*)/national-accounts-en',
                    r'(.*)/housing-characteristics-en',
                    r'(.*)/economic-statistics-en',
                    r'(.*)/census-of-building-cbde-en',
                    r'(.*)/index.php/mdg-en',
                    r'(.*)/gender-statistics-en'
                ],
        'excludes':[r'(.*)/images/(.*)']
    },

    # 塞浦路斯 时间解析有问题
    'cy':{
        'allowed_domains':['moh.gov.cy'],
        'site_url':'http://www.moh.gov.cy',
        'start_urls':['https://www.moh.gov.cy/moh/moh.nsf/dmlannouncements_en/dmlannouncements_en?OpenDocument&Start=1&Count=1000&Collapse=1'],
        'rules':[r'(.*)/Moh/MOH\.nsf/All/(.*)',r'(.*)/moh/moh\.nsf/All/(.*)'],
        'publish':[
                    {'rule':"//form/div[@id='footer']/div[@class='lastupdate']/text()",'format':'Last Modified at: %d/%m/%Y %I:%M:%S PM'},
                    {'rule':"//form/div[@id='footer']/div[@class='lastupdate']/text()",'format':'Last Modified at: %d/%m/%Y %I:%M:%S AM'}
                ]
    },

    # 格鲁吉亚
    'ge':{
        'allowed_domains':['moh.gov.ge'],
        'site_url':'http://www.moh.gov.ge',
        'start_urls':['http://www.moh.gov.ge/en/news/'],
        'rules':[r'(.*)/en/news/[0-9]{4}/(.*)',r'(.*)/en/news/page/(.*)'],
        'publish':[{'rule':"//section[@class='newsInner']/article/section[1]/span/text()",'format':'%d %B, %Y'}]
    },

    # 亚美尼亚
    'am':{
        'allowed_domains':['pharm.am'],
        'site_url':'http://www.pharm.am',
        'start_urls':['http://www.pharm.am/index.php/en/na/'],
        'rules':[r'(.*)/index\.php/en/na/(.*)']
    },

    # 阿塞拜疆 网站打不开
    'az':{
        'allowed_domains':['mednet.az'],
        'site_url':'http://www.mednet.az',
        'start_urls':[],
        'rules':[],
        'publish':[]
    },

    # 哈萨克斯坦 网站打不开
    'kz':{
        'allowed_domains':['mzsr.gov.kz'],
        'site_url':'http://www.mzsr.gov.kz',
        'start_urls':[],
        'rules':[],
        'publish':[]
    },

    # 乌兹别克斯坦 日期中月份不是英语，无法解析
    'uz':{
        'allowed_domains':['minzdrav.uz'],
        'site_url':'http://www.minzdrav.uz',
        'start_urls':['http://www.minzdrav.uz/en/news/','http://www.minzdrav.uz/en/measure/'],
        'rules':[r'(.*)/en/news/(.*)',r'(.*)/en/measure/(.*)'],
        'publish':[{'rule':"//div[@class='NewsIn']/div[@class='ScrollPane']/span/text()",'format':'%d %B %Y'}]
    },

    # 土库曼斯坦
    'tm':{
        'allowed_domains':['saglykhm.gov.tm'],
        'site_url':'http://www.saglykhm.gov.tm',
        'start_urls':['http://www.saglykhm.gov.tm/ru/news/','http://www.saglykhm.gov.tm/ru/informasionny/'],
        'rules':[r'(.*)/netcat_files/(.*)',r'(.*)/ru/Informasionny/(.*)'],
        'publish':[],
        'excludes':[r'(.*)\.jpg']
    },

    # 吉尔吉斯斯坦 日期中月份为特殊字符，无法解析
    'kg':{
        'allowed_domains':['med.kg'],
        'site_url':'http://www.med.kg',
        'start_urls':['http://www.med.kg/ru/novosti.html'],
        'rules':[r'(.*)/ru/[0-9]{3}(.*)',r'(.*)/ru/novosti\.html(.*)'],
        'publish':[{'rule':"//dd[@class='published hasTooltip']/time/text()",'format':'''
					%d %B %Y				'''}]
    },

    # 塔吉克斯坦 网站域名不对，网站打不开
    'tj':{
        'allowed_domains':['ministeres.tn'],
        'site_url':'http://www.ministeres.tn/html/ministere',
        'start_urls':[]
    },



    ###############################################
    # 欧洲
    ###############################################

    # 挪威
    'no':{
        'allowed_domains':['regjeringen.no'],
        'site_url':'https://www.regjeringen.no/en/dep/hod/id421',
        'start_urls':[
                        'https://www.regjeringen.no/en/whatsnew/finn-aktuelt/id2000005/?documentType=aktuelt/nyheter',
                        'https://www.regjeringen.no/en/find-document/id2000006/'
                    ],
        'rules':[
                    r'(.*)/en/aktuelt/(.*)',
                    r'(.*)/en/whatsnew/finn-aktuelt/(.*)',
                    r'(.*)/en/find-document/id2000006/(.*)',
                    r'(.*)/en/dokumenter/(.*)'
                ],
        'publish':[{'rule':"//span[@class='date']/text()",'format':'Date: %Y-%m-%d'}]
    },

    # 瑞典
    'se':{
        'allowed_domains':['government.se'],
        'site_url':'http://www.government.se/government-of-sweden/ministry-of-health-and-social-affairs',
        'start_urls':['http://www.government.se/government-of-sweden/ministry-of-health-and-social-affairs'],
        'rules':[r'(.*)/articles(.*)'],
        'publish':[{'rule':"//span[@class='published']/time/text()",'format':'%d %B %Y'}]
    },

    # 芬兰
    'fi':{
        'allowed_domains':['stm.fi'],
        'site_url':'http://stm.fi/en/frontpage',
        'start_urls':['http://stm.fi/en/frontpage'],
        'rules':[
                    r'(.*)/en/article/-/asset_publisher/(.*)',
                    r'(.*)/en/artikkeli/-/asset_publisher/(.*)'
                ],
        'publish':[
            {'rule':"//div[@class='meta clearfix']/div[@class='published row-fluid']/span[@class='date'][1]/text()",'format':'%d.%m.%Y'},
            {'rule':"//div[@class='meta clearfix']/div[@class='published row-fluid']/span[@class='date']/text()",'format':'%d.%m.%Y'}
            ]
    },

    # 丹麦
    'dk':{
        'allowed_domains':['stm.dk'],
        'site_url':'http://www.stm.dk/_a_1644.html',
        'start_urls':['http://www.stm.dk/_a_1644.html'],
        'rules':[
                    r'(.*)'
                ]
    },

    # 俄罗斯
    'ru':{
        'allowed_domains':['rosminzdrav.ru'],
        'site_url':'http://www.rosminzdrav.ru',
        'start_urls':['https://www.rosminzdrav.ru/news','https://www.rosminzdrav.ru/regional_news'],
        'rules':[r'(.*)/news(.*)',r'(.*)/regional_news(.*)'],
        'publish':[
                {'rule':"//p[@class='timestamps']/time[1]/text()",
                'format':'Материал опубликован %d %B %Y в %H:%M. '}
                ],
        'excludes':[
                    r'(.*)\.jpg(.*)',
                    r'(.*)comments.atom',
                    r'(.*)system/attachments/attaches/(.*)'
                    ]
    },

    # 爱沙尼亚
    'ee':{
        'allowed_domains':['valitsus.ee'],
        'site_url':'https://www.valitsus.ee/en',
        'start_urls':['https://www.valitsus.ee/en/news'],
        'rules':[r'(.*)/en/news(.*)'],
        'publish':[{'rule':"//footer[@class='submitted']/span[1]/text()",'format':'%d. %B %Y - %H:%M'}],
        'excludes':[r'\.jpg(.*)']
    },

    # 拉脱维亚 网页打不开
    'lv':{
        'allowed_domains':['vza.gov.lv'],
        'site_url':'http://www.vza.gov.lv',
        'start_urls':[]
    },

    # 立陶宛
    'lt':{
        'allowed_domains':['sam.lrv.lt'],
        'site_url':'http://sam.lrv.lt/en',
        'start_urls':['http://sam.lrv.lt/en/news'],
        'rules':[r'(.*)/news(.*)'],
        'publish':[{'rule':"//div[@class='row startDate_wrap']/div/div[2]/p/text()",'format':'%Y %m %d'}]
    },

    # 白俄罗斯
    'by':{
        'allowed_domains':['minzdrav.gov.by'],
        'site_url':'http://www.minzdrav.gov.by/en',
        'start_urls':['http://www.minzdrav.gov.by/en/static/programmes-of-ministry-of-heal/'],
        'rules':[
                    r'(.*)/en/static/programmes-of-ministry-of-heal/scientic_progr/(.*)',
                    r'(.*)/en/static/programmes-of-ministry-of-heal/state_progr(.*)'
                ]
    },

    # 乌克兰
    'ua':{
        'allowed_domains':['health.gov.ua'],
        'site_url':'http://www.health.gov.ua/www.nsf/all/index_e?opendocument',
        'start_urls':['http://www.health.gov.ua/www.nsf/all/e05-01?opendocument'],
        'rules':[
                    r'(.*)/www\.nsf/all/e05-01-01\?opendocument',
                    r'(.*)/www\.nsf/all/e05-01-02\?opendocument',
                    r'(.*)/www\.nsf/all/u05-01-01\?opendocument'
                ]
    },

    # 波兰
    'pl':{
        'allowed_domains':['mz.gov.pl'],
        'site_url':'http://www.mz.gov.pl/en',
        'start_urls':['http://www.mz.gov.pl/en/healthcare-system/','http://www.mz.gov.pl/en/treatment/'],
        'rules':[
                    r'(.*)/en/healthcare-system/healthcare-organization/(.*)',
                    r'(.*)/en/healthcare-system/emergency-medical-services/(.*)',
                    r'(.*)/en/healthcare-system/health-personnel-and-training/(.*)',
                    r'(.*)/en/treatment/poz/(.*)',
                    r'(.*)/en/treatment/outpatient-specialist-care/(.*)',
                    r'(.*)/en/treatment/hospital-treatment/(.*)',
                    r'(.*)/en/treatment/services-guaranteed-within-health-programmes/(.*)',
                    r'(.*)/en/treatment/dental-treatment/(.*)',
                    r'(.*)/en/treatment/therapeutic-rehabilitation/(.*)',
                    r'(.*)/en/treatment/psychiatric-care-and-addiction-treatment/(.*)',
                    r'(.*)/en/treatment/nursing-and-welfare-services/(.*)',
                    r'(.*)/en/treatment/palliative-and-hospice-care/(.*)',
                    r'(.*)/en/treatment/medical-rescue-services/(.*)',
                    r'(.*)/en/treatment/spa-treatment/(.*)',
        ]
    },
    
    # 德国
    'de':{
        'allowed_domains':['bundesgesundheitsministerium.de'],
        'site_url':'http://www.bundesgesundheitsministerium.de/en/en.html',
        'start_urls':['http://www.bundesgesundheitsministerium.de/en/ministry/news.html'],
        'rules':[r'(.*)/en/ministry/(.*)'],
        'publish':[{'rule':"//p/span[@class='article-date']/text()",'format':'%d %B %Y'}],
        'excludes':[
                        r'(.*)/en/en/ministry/leadership(.*)',
                        r'(.*)/en/en/ministry/international-co-operation(.*)',
                        r'(.*)/en/en/ministry/the-federal-ministry-of-health(.*)',
                        r'(.*)/en/en/ministry/authorities-within-the-remit(.*)',
                        r'(.*)/en/en/ministry/laws(.*)',
                        r'(.*)/en/en/ministry/press-office(.*)'
                    ]
    },

    # 捷克
    'cz':{
        'allowed_domains':['mzcr.cz'],
        'site_url':'http://www.mzcr.cz/En',
        'start_urls':[
                        'http://www.mzcr.cz/En/obsah/advisory-boards-of-the-minister_1913_2.html',
                        'http://www.mzcr.cz/En/obsah/informatics-at-the-ministry-of-health_1914_2.html',
                        'http://www.mzcr.cz/En/obsah/other-information_2640_2.html',
                        'http://www.mzcr.cz/En/obsah/introduction_1926_2.html',
                        'http://www.mzcr.cz/En/obsah/general-principles_1928_2.html',
                        'http://www.mzcr.cz/En/obsah/participation-of-foreign-nationals_1929_2.html',
                        'http://www.mzcr.cz/En/obsah/health-care-in-the-czech-republic_2005_2.html',
                        'http://www.mzcr.cz/En/obsah/scope-of-care-reimbursed-from-public-health-insurance_2006_2.html',
                        'http://www.mzcr.cz/En/obsah/rights-and-obligations-of-participants_1932_2.html',
                        'http://www.mzcr.cz/En/obsah/health-insurers_1933_2.html',
                        'http://www.mzcr.cz/En/obsah/foreigners-who-do-not-participate-in-the-public-health-insurance_1934_2.html',
                        'http://www.mzcr.cz/En/obsah/foreign-nationals-and-health-insurance_1935_2.html',
                        'http://www.mzcr.cz/En/obsah/main-types-of-regulation-fees-_1937_2.html',
                        'http://www.mzcr.cz/En/obsah/time-limits-for-payment-of-regulation-fees_1938_2.html',
                        'http://www.mzcr.cz/En/obsah/categories-of-the-insured-exempt_1939_2.html',
                        'http://www.mzcr.cz/En/obsah/narcotic-drugs-and-psychotropic-substances_2061_2.html',
                        'http://www.mzcr.cz/En/obsah/pandemic-plan-of-the-czech-republic_2600_2.html'

                    ],
        'rules':[r'(.*)/En/dokumenty/(.*)'],
        'publish':[{'rule':"//div[@id='right-column-content']/div[@class='box-ostrance']/p[1]/text()",'format':'Published: %d.%m.%Y'}]
    },

    # 斯洛伐克
    'sk':{
        'allowed_domains':['uvzsr.sk'],
        'site_url':'http://www.uvzsr.sk',
        'start_urls':['http://www.uvzsr.sk/en/index.php/documents','http://www.uvzsr.sk/en/index.php/expert-departments'],
        'rules':[r'(.*)/en/index\.php/documents'],
        'publish':[]
    },
    
    # 奥地利
    'at':{
        'allowed_domains':['bmgf.gv.at'],
        'site_url':'http://www.bmgf.gv.at/cms/home/thema.html?channel=CH1013',
        'start_urls':['https://www.bmgf.gv.at/home/EN/Health/'],
        'rules':[
                    r'(.*)/home/EN/Health/Addiction/(.*)',
                    r'(.*)/home/EN/Health/Diseases_and_medicine/(.*)',
                    r'(.*)/home/EN/Health/Health_care_system/(.*)',
                    r'(.*)/home/EN/Health/Information_for_Travellers/(.*)',
                    r'(.*)/home/EN/Health/Nutrition/(.*)',
                    r'(.*)/home/EN/Health/Quality_of_Care_and_Patient_Safety/(.*)',
                    r'(.*)/home/EN/Health/Suicide_prevention_/(.*)',
                    r'(.*)/home/EN/Health/Tobacco/(.*)',
                    r'(.*)/home/EN/Health/Healthcare_Professions/(.*)'
        ]
    },

    # 瑞士 时间解析有问题
    'ch':{
        'allowed_domains':['bag.admin.ch'],
        'site_url':'https://www.bag.admin.ch/bag/de/home.html',
        'start_urls':[
                        'https://www.bag.admin.ch/bag/de/home/aktuell/news.html',
                        'https://www.bag.admin.ch/bag/de/home/aktuell/medienmitteilungen.html',
                        'https://www.bag.admin.ch/bag/de/home/aktuell/veranstaltungen.html'
                    ],
        'rules':[
                    r'(.*)/bag/de/home/aktuell/news(.*)',
                    r'(.*)/bag/de/home/aktuell/medienmitteilungen\.msg-id(.*)',
                    r'(.*)/bag/de/home/aktuell/veranstaltungen/(.*)'
                ],
        'publish':[{'rule':"//div[@class='clearfix']/p[@class='pull-left']/small/span[@class='text-dimmed']/text()",'format':'Letzte Änderung %d.%m.%Y'}]
    },

    # 列支敦士登 感觉规则没问题，加上规则爬不下来东西
    'li':{
        'allowed_domains':['llv.li'],
        'site_url':'https://www.llv.li/#/1908/amt-fur-gesundheit',
        'start_urls':['https://www.llv.li/#/40/'],
        'rules':[r'(.*)/[0-9]{2,5}/(.*)',r'(.*)/files/dss/(.*)']
    },

    # 英国
    'uk':{
        'allowed_domains':['gov.uk'],
        'site_url':'https://www.gov.uk/government/organisations/department-of-health',
        'start_urls':['https://www.gov.uk/government/latest?departments%5B%5D=department-of-health'],
        'rules':[
                    r'(.*)/government/publications/(.*)',
                    r'(.*)/government/news/(.*)',
                    r'(.*)/government/consultations/(.*)',
                    r'(.*)/government/latest(.*)'
                ],
        'publish':[{'rule':"//div[@id='history']/p[1]/span[@class='published definition']/text()",'format':'%d %B %Y'}]
    },

    # 爱尔兰 网页打不开
    'ie':{
        'allowed_domains':['doh.ie'],
        'site_url':'http://www.doh.ie',
        'start_urls':[]
    },

    # 荷兰 时间解析有问题
    'nl':{
        'allowed_domains':['government.nl'],
        'site_url':'https://www.government.nl/ministries/ministry-of-health-welfare-and-sport',
        'start_urls':['https://www.government.nl/ministries/ministry-of-health-welfare-and-sport/news'],
        'rules':[r'(.*)/ministries/ministry-of-health-welfare-and-sport/news(.*)'],
        'publish':[{'rule':"//div[@id='main']/div[@class='wrapper']/div[@id='content']/p[@class='article-meta']/text()",'format':'News item | %d-%m-%Y | %H:%M'}]
    },

    # 比利时 时间解析有问题
    'be':{
        'allowed_domains':['belgium.be'],
        'site_url':'https://www.belgium.be/en/health',
        'start_urls':['https://www.belgium.be/en/news'],
        'rules':[r'(.*)/en/news(.*)'],
        'publish':[{'rule':"//section[@id='content']/div[@id='block-system-main']/div/div[@class='submitted']/text()",'format':'''
      date: %d %B %Y    '''}]
    },

    # 卢森堡
    'lu':{
        'allowed_domains':['sante.public.lu'],
        'site_url':'http://www.sante.public.lu/fr/politique-sante/ministere-sante/index.html',
        'start_urls':['http://www.sante.public.lu/fr/actualites/index.html'],
        'rules':[r'(.*)/fr/actualites/(.*)'],
        'publish':[{'rule':"//time[@class='article-published']/text()",'format':'%d-%m-%Y'}]
    },

    # 法国 空吃内存，没输出，注释掉规则和日期也是一样
    'fr':{
        'allowed_domains':['solidarites-sante.gouv.fr'],
        'site_url':'http://solidarites-sante.gouv.fr',
        'start_urls':['http://solidarites-sante.gouv.fr/actualites/'],
        'rules':[
                    r'(.*)'
                ],
        'publish':[{'rule':"//div[@class='main-article__horodatage']/span[@class='main-article__date date--publication']",'format':'%d.%m.%y'}]
    },

    # 摩纳哥
    'mc':{
        'allowed_domains':['en.gouv.mc'],
        'site_url':'http://en.gouv.mc/Government-Institutions/The-Government/Ministry-of-Health-and-Social-Affairs',
        'start_urls':['http://en.gouv.mc/News'],
        'rules':[r'(.*)/News/(.*)'],
        'publish':[{'rule':"//div[@class='info']/span[@class='date']/text()",'format':'%d %B %Y'}]
    },

    # 西班牙 时间解析有问题,月份不是英语
    'es':{
        'allowed_domains':['msc.es'],
        'site_url':'http://www.msc.es/en/home.htm',
        'start_urls':['http://www.msc.es/en/gabinete/notasPrensa.do'],
        'rules':[r'(.*)/en/gabinete/notasPrensa\.do(.*)'],
        'publish':[
                    {'rule':"//section[@class='col-sm-8 col-md-9 informacion']/div[2]/p[1]/strong/text()",'format':'%d de %B de %Y.'},
                    {'rule':"//section[@class='col-sm-8 col-md-9 informacion']/div[2]/p[1]/strong/text()",'format':'%d de %B de %Y'}
                    ]
    },

    # 葡萄牙
    'pt':{
        'allowed_domains':['sns.gov.pt'],
        'site_url':'https://www.sns.gov.pt/',
        'start_urls':['https://www.sns.gov.pt/noticias/'],
        'rules':[
                    r'(.*)/noticias/[0-9]{4}/[0-9]{2}/[0-9]{2}/(.*)',
                    r'(.*)/noticias/page/(.*)'
                ],
        'publish':[{'rule':"//div[@class='post-info-bar']/div[@class='post-info cf col-md-2 col-xs-12']/span/text()",'format':'%d/%m/%Y'}]
    },

    # 安道尔
    'ad':{
        'allowed_domains':['salutibenestar.ad'],
        'site_url':'http://www.salutibenestar.ad/index2.htm',
        'start_urls':['https://www.salutibenestar.ad/temes-de-salut'],
        'rules':[r'(.*)/temes-de-salut/(.*)']
    },

    # 意大利 403 forbidden
    'it':{
        'allowed_domains':['ministerosalute.it'],
        'site_url':' http://www.ministerosalute.it'
    },

    # 圣马力诺 没有权限，需要登录
    'sm':{
        'allowed_domains':['sanita.segreteria.sm'],
        'site_url':'http://www.sanita.segreteria.sm'
    },

    # 马耳他
    'mt':{
        'allowed_domains':['gov.mt'],
        'site_url':'https://deputyprimeminister.gov.mt/en/Pages/health.aspx',
        'start_urls':['https://deputyprimeminister.gov.mt/en/news/Pages/News.aspx'],
        'rules':[r'(.*)/en/Government/Press%20Releases/Pages/[0-9]{4}/(.*)',r'(.*)/en/news/Pages/News(.*)'],
        'publish':[{'rule':"//div[@class='content']/div[@class='header']/div[@class='info']/text()",'format':'%b %d, %Y'}]
    },

    # 匈牙利 网页打不开
    'hu':{
        'allowed_domains':['enum.hu'],
        'site_url':'http://www.eum.hu',
        'start_urls':[''],
        'rules':[],

    },

    # 塞尔维亚 时间解析不对
    'rs':{
        'allowed_domains':['zdravlje.gov.rs'],
        'site_url':'http://www.zdravlje.gov.rs/index.php',
        'start_urls':[
                        'http://www.zdravlje.gov.rs/showpage.php?id=9',
                        'http://www.zdravlje.gov.rs/showpage.php?id=63',
                        'http://www.zdravlje.gov.rs/showpage.php?id=64',
                        'http://www.zdravlje.gov.rs/showpage.php?id=65',
                        'http://www.zdravlje.gov.rs/showpage.php?id=256',
                        'http://www.zdravlje.gov.rs/showpage.php?id=326',
                        'http://www.zdravlje.gov.rs/showpage.php?id=332',
                        'http://www.zdravlje.gov.rs/showpage.php?id=363',
                        'http://www.zdravlje.gov.rs/showpage.php?id=338',
                    ],
        'rules':[
                    r'(.*)/showelement\.php\?id=(.*)',
                    r'(.*)/showpage\.php\?id=9',
                    r'(.*)/showpage\.php\?id=63',
                    r'(.*)/showpage\.php\?id=64',
                    r'(.*)/showpage\.php\?id=65',
                    r'(.*)/showpage\.php\?id=256',
                    r'(.*)/showpage\.php\?id=326',
                    r'(.*)/showpage\.php\?id=332',
                    r'(.*)/showpage\.php\?id=363',
                    r'(.*)/showpage\.php\?id=338',
                ],
        'publish':[{'rule':"//div[@id='content']/div[@id='content_head']/text()",'format':'Са подацима од: %d.%m.%Y. '}]
    },

     # 保加利亚
    'bg':{
        'allowed_domains':['mh.government.bg'],
        'site_url':'http://www.mh.government.bg',
        'start_urls':[
                        'http://www.mh.government.bg/bg/novini/aktualno/',
                        'http://www.mh.government.bg/bg/politiki/',
                        'http://www.mh.government.bg/bg/evropeyski-programi/tekushti-programi-i-proekti/'
                    ],
        'rules':[
                    r'(.*)/bg/novini/aktualno(.*)',
                    r'(.*)/bg/evropeyski-programi/tekushti-programi-i-proekti(.*)',
                    r'(.*)/bg/politiki(.*)'
                ],
        'publish':[{"rule":"//div[@id='top']/ul[@class='newsdate']/time[@datetime]/@datetime","format":"%Y-%m-%dT%H:%M:%S+03:00"}]
    },

    # 斯洛文尼亚
    'si':{
        'allowed_domains':['mz.gov.si',],
        'site_url':'http://www.mz.gov.si',
        'start_urls':[
                        'http://www.mz.gov.si/si/medijsko_sredisce/intervjuji',
                        'http://www.mz.gov.si/si/medijsko_sredisce/sporocila_za_medije',
                        'http://www.mz.gov.si/si/medijsko_sredisce/koledar_dogodkov',
                        'http://www.mz.gov.si/si/medijsko_sredisce/poslanska_vprasanja',
                        'http://www.mz.gov.si/si/pogoste_vsebine_za_javnost/izdaja_zdravil_prek_medmrezja'
                    ],
        'rules':[r'(.*)/si/medijsko_sredisce(.*)',r'(.*)/si/pogoste_vsebine_za_javnost(.*)'],
        'publish':[{"rule":"//div[@id='mainContainer']/div[@class='newsdate']/text()","format":"%d. %m. %Y"}]
    },

    # 梵蒂冈 没有网址

    # 克罗地亚
    'hr':{
        'allowed_domains':['zdravstvo.gov.hr'],
        'site_url':'https://zdravstvo.gov.hr/',
        'start_urls':[
                        'https://zdravstvo.gov.hr/vijesti/8',
                        'https://zdravstvo.gov.hr/dokumenti/10',
                        'https://zdravstvo.gov.hr/savjetovanje-sa-zainteresiranom-javnoscu-1475/1475',
                        'https://zdravstvo.gov.hr/najcesca-pitanja-i-odgovori/1479',
                        'https://zdravstvo.gov.hr/strategije-planovi-i-izvjesca/2396'
                    ],
        'rules':[r'(.*)/vijesti/8(.*)',r'(.*)/vijesti(.*)',r'(.*)/pristup-informacijama(.*)'],
        'publish':[{"rule":"//div[@class='article_left']/li[@class='time_info']/text()","format":"Objavljeno: %d.%m.%Y."}]

    },

    # 波斯尼亚和黑塞哥维那 月份非英语，有的解析无法解析
    'ba':{
        'allowed_domains':['fmoh.gov.ba'],
        'site_url':'http://www.fmoh.gov.ba',
        'start_urls':['http://www.fmoh.gov.ba/index.php/novosti-iz-ministarstva'],
        'rules':[r'(.*)/index\.php/novosti-iz-ministarstva(.*)'],
        'publish':[{'rule':"//header/p[@class='meta']/time/text()",'format':'%d %B %Y'}]
    },

    # 黑山
    'me':{
        'allowed_domains':['mzd.gov.me'],
        'site_url':'http://www.mzd.gov.me/en/ministry',
        'start_urls':['http://www.mzd.gov.me/en/news'],
        'rules':[r'(.*)/en/news(.*)'],
        'publish':[{'rule':"//div[@class='detalji-hold']/div[@class='detalji']/text()",'format':'%d.%m.%Y %H:%M |'}]
    },

    # 罗马尼亚 日期中月份非英语，无法解析
    'ro':{
        'allowed_domains':['ms.ro'],
        'site_url':'http://www.ms.ro',
        'start_urls':['http://www.ms.ro/comunicate/'],
        'rules':[r'(.*)/[0-9]{4}/[0-9]{2}/[0-9]{2}/(.*)',r'(.*)/comunicate/(.*)'],
        'publish':[{'rule':"//span[@class='post-meta-infos']/time[@class='date-container minor-meta updated']/text()",'format':'%d %B %Y'}]
    },

    # 希腊
    'gr':{
        'allowed_domains':['efpolis.gr'],
        'site_url':'"http://www.efpolis.gr',
        'start_urls':['http://www.efpolis.gr/el/ggk-deltia-typou.html'],
        'rules':[r'(.*)/el/ggk-deltia-typou/(.*)',r'(.*)/filesbase/[0-9]{4}(.*)']
    },

    # 阿尔巴尼亚 网站打不开
    'al':{
        'allowed_domains':['moh.gov.al'],
        'site_url':'http://www.moh.gov.al',
        'start_urls':[]
    },

    # 马其顿
    'mk':{
        'allowed_domains':['vlada.mk'],
        'site_url':'http://vlada.mk/?q=node/353&language=en-gb',
        'start_urls':['http://vlada.mk/media-centar'],
        'rules':[r'(.*)/node/[0-9]{5}',r'(.*)/media-centar(.*)'],
        'publish':[{'rule':"//div[@class='meta post-info']/div[@class='meta submitted']/text()",'format':'''
            	              	%d.%m.%Y        	'''}]
    },

    ###############################################
    # 非洲
    ###############################################

    ## 埃及
    'eg':{
        'allowed_domains':['mohp.gov.eg'],
        'site_url':'http://www.mohp.gov.eg',
        'start_urls':[
            'http://www.mohp.gov.eg/News.aspx',
            'http://www.mohp.gov.eg/Events.aspx',
            'http://www.mohp.gov.eg/Courses.aspx',
            'http://www.mohp.gov.eg/cancer/'
        ],
        'rules':[
            r'(.*)/NewsDetails\.aspx(.*)',
            r'(.*)/EventDetails\.aspx(.*)',
            r'(.*)/coursedetailes\.aspx(.*)'
        ],
        'language':'ar_EG',
        'publish':[{"rule":"//div[contains(@class,'redate')]/text()","format":"%d %B %Y"}]
    },
    ## 利比亚 网站失效
    'ly':{

    },
    ## 阿尔及利亚 打不开
    'dz':{
    },
    ## 摩洛哥
    'ma':{
        'allowed_domains':['gov.ma'],
        'site_url':'http://www.sante.gov.ma',
        'start_urls':[
            'http://www.sante.gov.ma/Pages/Accueil.aspx',

        ],
        'language':'fr-fr',
        'rules':[
            r'(.*)/Pages/activites\.aspx(.*)',
            r'(.*)/Pages/toutes_actualites\.aspx(.*)',
            r'(.*)/Publications(.*)',
            r'(.*)/Medicaments(.*)',
            r'(.*)/Pages/annonces\.aspx(.*)',
            r'(.*)/Pages/communiqués\.aspx(.*)'
        ],
        'publish':[
            {
                'rule':'//*[contains(@class,"article")]//*[contains(@class,"date")]/text()',
                'format':'%Y-%m-%d',
                'extra':ma_time_sub

            }
        ]
    },
    ## 突尼斯
    'tn':{
        'allowed_domains':['santetunisie.rns.tn'],
        'site_url':'http://www.santetunisie.rns.tn',
        'start_urls':[
            'http://www.santetunisie.rns.tn/fr',

        ],
        'language':'fr-fr',
        'rules':{
            r'(.*)fr/toutes-les-actualites(.*)',
            r'(.*)fr/education-santé(.*)',
            r'(.*)fr/sante-en-tunisie(.*)',
            r'(.*)fr/indicateurs(.*)'
        }
    },
    ## 毛里塔尼亚 打不开
    'mr':{

    },
    ## 马里 没有网站
    'ml':{

    },
    ## 塞内加尔
    'sn':{
        'allowed_domains':['sante.gouv.sn'],
        'language':'fr-fr',
        'site_url':'http://www.sante.gouv.sn',
        'start_urls':[
            'http://www.sante.gouv.sn/index.php',
            'http://www.sante.gouv.sn/index.php',
        ],
        'rules':[
            r'(.*)page-reader-les-actualites-get\.php(.*)',
            r'(.*)/page-reader-content-details\.php(.*)',
            r'(.*)page-reader-categories-article-presse(.*)'
        ],
    },
    ## 冈比亚
    'gm':{
        'allowed_domains':['moh.gov.gm'],
        'site_url':'http://moh.gov.gm',
        'start_urls':[
            'http://moh.gov.gm'
        ],
        'rules':[
            r'(.*)'
        ]

    },
    ## 利比里亚
    'lr':{
        'allowed_domains':['moh.gov.lr'],
        'site_url':'http://moh.gov.lr',
        'start_urls':[
            'http://moh.gov.lr',
        ],
        'rules':[
            r'(.*)',
        ],
        'publish':[
            {
                'rule':'//*[@id="page"]//article//p[contains(@class,"post-byline")]/text()[2]',
                'format':'%Y,%B,%d',
                'extra':lr_time_sub,
            }
        ],
        'excludes':[
            r'(.*)/photos(.*)',
            r'(.*)/videos(.*)',
            r'(.*)/audios(.*)'
        ]
    },
    ## 加纳
    'gh':{
        'allowed_domains':['moh.gov.gh'],
        'site_url':'http://www.moh.gov.gh',
        'start_urls':[
            'http://www.moh.gov.gh',
        ],
        'rules':[
            r'(.*)'
        ],
        'excludes':[
            r'(.*)/gallery-of-projects(.*)',
        ]
        
    },
    ## 贝宁 打不开
    'bj':{

    },
    ## 尼日利亚 打不开
    'ng':{

    },
    ## 喀麦隆
    'cm':{
        'allowed_domains':['minsante.cm'],
        'site_url':'http://www.minsante.cm',
        'start_urls':[
            'http://www.minsante.cm/site/?q=fr',
        ],
        'language':'fr-fr',
        'rules':[
            r'(.*)/site/\?q=fr(.*)'
        ],
        'publish':[
            {
                'rule':'//*[@id="block-system-main"]//*[contains(@class,"creation")]/span[1]/text()',
                'format':'Publi\xe9 le %d %b %Y'
            }
        ]
    },
    ## 苏丹 打不开
    'sd':{

    },
    ## 安哥拉 打不开
    'ao':{

    },
    ## 埃塞俄比亚 打不开
    'et':{

    },
    ## 索马里
    'so':{
        'allowed_domains':['moh.gov.so'],
        'site_url':'http://moh.gov.so',
        'start_urls':[
            'http://moh.gov.so'
        ],
        'rules':[
            r'(.*)/en/media-center/news-updates(.*)',
            r'(.*)/en/media-center/reports(.*)',
            r'(.*)/en/media-center/events(.*)',
            r'(.*)/en/media-center/press-release(.*)',
            r'(.*)/en/awareness(.*)',
            r'(.*)/en/health-programs(.*)',
            r'(.*)/en/tb-program(.*)',
            r'(.*)/en/component/content/article(.*)',
            r'(.*)/en/publications(.*)',
            r'(.*)/en/health-facilities(.*)',
        ],

    },
    ## 厄立特里亚 网站在维护
    'er':{


    },
    ## 坦桑尼亚
    'tz':{
        'allowed_domains':['moh.go.tz'],
        'site_url':'http://www.moh.go.tz',
        'start_urls':[
            'http://www.moh.go.tz/en/'

        ],
        'rules':[
            r'(.*)/en/hmis-data(.*)',
            r'(.*)/en/announcements(.*)',
            r'(.*)/en/upcoming-events(.*)',
            r'(.*)/en/press-releases(.*)',
            r'(.*)/en/86-news-and-events(.*)',
            r'(.*)en/strategic-plans(.*)',
            r'(.*)/en/reports(.*)',
            r'(.*)/en/research-and-findings(.*)',
            r'(.*)/en/circulars(.*)',
            r'(.*)/en/guidelines(.*)',
            r'(.*)/en/yellow-fever-entry(.*)',
            r'(.*)/en/epidemiological-disease-report(.*)'


        ],
        'publish':[
            {
                'rule':'//*[@id="jsn-mainbody"]//time[@datetime]/@datetime',
                'format':'%Y-%m-%dT%H:%M:%S+00:00'
            }
        ]
        

    },
    ## 肯尼亚
    'ke':{
        'allowed_domains':['health.go.ke'],
        'site_url':'http://www.health.go.ke',
        'start_urls':[
            'http://www.health.go.ke'
        ],
        'rules':[
            r'(.*)/event(.*)',
            r'(.*)/[0-9]{4}/[0-9]{1,2}(.*)',
            r'(.*)/news(.*)',
            r'(.*)/resources(.*)',


        ],
        'publish':[
            {
                'rule':'//*[@id="main-content"]//*[contains(@class,"postmetadata")]/span[1]/text()',
                'format':'On %B %d, %Y',

            }
        ]
    },
    ## 乌干达
    'ug':{
        'allowed_domains':['health.go.ug'],
        'site_url':'http://health.go.ug',
        'start_urls':[
            'http://health.go.ug'
        ],
        'rules':[
            r'(.*)/news-and-updates(.*)',
            r'(.*)/contene(.*)',
            r'(.*)/projects(.*)',
            r'(.*)/programs(.*)',
            r'(.*)/publications(.*)'
        ],
    },
    ## 卢旺达 带cookie才可以访问
    'rw':{
        'allowed_domains':['moh.gov.rw'],
        'site_url':'http://moh.gov.rw',
        'start_urls':[
            'http://moh.gov.rw/index.php?id=2'
        ],

        'rules':[
            r'(.*)/index\.php\?id=(5|2|183|90|95|109|99|177|124|136|29|242|227)(.*?)',
            r'(.*)/index\.php\?id=34(.*)'
        ],
    },

    ## 布隆迪 打不开
    'bi':{

    },
    ## 赞比亚 打不开
    'zm':{

    },
    ## 马拉维
    'mw':{
        'allowed_domains':['health.gov.mw'],
        'site_url':'http://www.hiv.health.gov.mw',
        'start_urls':[
            'http://www.hiv.health.gov.mw'
        ],
        'rules':[
            r'(.*)/index\.php/our-documents(.*)',
            r'(.*)/index\.php/(.*)/latest-news(.*)',
            r'(.*)/index\.php/(.*)/events-calender(.*)',
            r'(.*)/index\.php/information(.*)',
            r'(.*)/index\.php(.*)'
        ],


    },
    ## 莫桑比克 打不开
    'mz':{

    },
    ## 马达加斯加 前端渲染 爬不了
    'mg':{
        'allowed_domains':['sante.gov.mg'],
        'site_url':'http://www.sante.gov.mg',
        'start_urls':[
            'http://www.sante.gov.mg'
        ],
        'rules':[
            r'(.*)'
        ],
    },
    ## 毛里求斯
    'mu':{
        'allowed_domains':['health.govmu.org'],
        'site_url':'http://health.govmu.org',
        'start_urls':[
            'http://health.govmu.org/English/Pages/default.aspx'
        ],
        'rules':[
            r'(.*)/(e|E)nglish/ServicesHealth(.*)',
            r'(.*)/(e|E)nglish/Statistics(.*)',
            r'(.*)/(e|E)nglish/News(.*)',
            r'(.*)/(e|E)nglish/Events(.*)'


        ],
        'publish':[
            {
                'rule':'normalize-space(//*[@id="ctl00_PlaceHolderMain__editModePanelPublishingDateFormatted"]/span[2]/text())',
                'format':'%B %d, %Y'
            }
        ]
    },
    ## 塞舌尔
    'sc':{
        'allowed_domains':['health.gov.sc'],
        'site_url':'http://www.health.gov.sc',
        'start_urls':[
            'http://www.health.gov.sc'
        ],
        'rules':[
            r'(.*)index\.php/media/news(.*)',
            r'(.*)/index\.php/news-posts(.*)',
            r'(.*)index\.php/press-release-blog(.*)',
            r'(.*)index\.php/[0-9]{4}/[0-9]{1,2}/[0-9]{1,2}/(.*)',
            r'(.*)/index\.php/newsletters(.*)',
            r'(.*)/index\.php/media/speeches(.*)',
            r'(.*)/index\.php/national-assembly-questions(.*)',
            r'(.*)/index\.php/policies(.*)',
            r'(.*)/index\.php/plans(.*)',
            r'(.*)/index\.php/reports(.*)',
            r'(.*)/index\.php/statistics(.*)',
            r'(.*)/index\.php/money-matters(.*)',
            r'(.*)/index\.php/faqs(.*)'
        ],
        'publish':[
            {
                'rule':'//*[@id="theme-page"]//time[@datetime and contains(@class,"news-single-date")]/@datetime',
                'format':'%B %d, %Y'
            },
            {
                'rule':'//*[@id="theme-page"]//*[contains(@class,"mk-single-content")]/p[1]/span/em/text()',
                'format':'%d %B %Y',
                'extra':sc_time_sub,
            }
        ]

    },
    ## 纳米比亚
    'na':{
        'allowed_domains':['mhss.gov.na'],
        'site_url':'http://www.mhss.gov.na',
        'start_urls':[
            'http://www.mhss.gov.na'
        ],
        'rules':[
            r'(.*)/(news|events)(.*)',
            r'(.*)/downloads(.*)',
            r'(.*)/namphia(.*)'
        ],
        'excludes':[
            r'(.*)/(videos|picture-galleries)(.*)'
        ],
        'publish':[
            {
                'rule':'//*[@id="id_passed"]/div[1]/b/span/text()',
                'format':'%d %b %Y'
            }
        ]

    },
    ## 伯兹瓦纳 
    'bw':{
        'allowed_domains':['gov.bw'],
        'site_url':'http://www.gov.bw',
        'start_urls':['http://www.gov.bw/en/Ministries--Authorities/Ministries/MinistryofHealth-MOH/'],
        'rules':[
            r'(.*)/en/Ministries--Authorities/Ministries/MinistryofHealth-MOH(.*)'
        ],
    },
    ## 津巴布韦 503
    'zw':{

    },
    ## 斯威士兰 404
    'sz':{

    },
    ## 莱索托
    'ls':{
        'allowed_domains':['health.gov.ls'],
        'site_url':'http://www.health.gov.ls',
        'start_urls':[
            'http://www.health.gov.ls/gov_webportal/home/index.html'
        ],
        'rules':[
            r'(.*)/gov_webportal/(articles|health|ministries|news archives|home)(.*)',
        ],
    },
    ## 南非
    'za':{
        'allowed_domains':['health.gov.za'],
        'site_url':'http://www.health.gov.za',
        'start_urls':['http://www.health.gov.za'],
        'rules':[
            r'(.*)/index\.php/(diseases|gf-tb-program)(.*)',
            r'(.*)/index\.php/component/phocadownload(.*)',
            r'(.*)/index\.php/[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}'
        ],
    },
    ###############################################
    # 北美洲
    ###############################################

    ## 美国
    'us':{
        'allowed_domains':['hhs.gov'],
        'site_url':'https://www.hhs.gov',
        'start_urls':[
            'https://www.hhs.gov',
            'https://www.hhs.gov/blog',

        ],
        'rules':[
            r'(.*)/blog(.*)',
            r'(.*)/about/news(.*)',
            r'(.*)/about/strategic-plan(.*)',
            r'(.*)/programs/prevention-and-wellness(.*)',
            r'(.*)/programs/research(.*)',
            r'(.*)/programs/topic-sites(.*)'
        ],
        'publish':[
            {
                'rule':'//*[@id="block-system-main"]//*[contains(@class,"date-display-single") and @content]/@content',
                'format':'%Y-%m-%dT%H:%M:%S-05:00'
            },
            {
                'rule':'//*[@id="site-content"]//*[contains(@class,"content")]//*[contains(@class,"left")]/b/text()[2]',
                'format':'%B %d, %Y'
            }
        ]
    },
    ## 加拿大
    'ca':{
        'allowed_domains':['canada.ca','healthycanadians.gc.ca'],
        'site_url':'',
        'start_urls':[
            'https://www.canada.ca/en/services/health.html',

        ],
        'rules':[
            r'(.*)/en/services/health(.*)',
            r'(.*)/en/health-canada/services(.*)',
            r'(.*)/en/public-health/services(.*)',
            r'(.*)/en/public-health(.*)',
            r'(.*)/en/health-canada(.*)',
            r'(.*)/eating-nutrition(.*)',
        ],
        'publish':[
            {
                'rule':'//*[@id="wb-dtmd"]//*[contains(@property,"dateModified")]/text()',
                'format':'%Y-%m-%d'
            }

        ]
    },
    ## 墨西哥
    'mx':{
        'allowed_domains':['gob.mx'],
        'site_url':'https://www.gob.mx',
        'start_urls':[
            'https://www.gob.mx/salud/en',
            'https://www.gob.mx/salud/en/archivo/articulos',
            'https://www.gob.mx/salud/en/archivo/prensa',
            'https://www.gob.mx/salud/en/archivo/documentos',
            'https://www.gob.mx/temas/archivo/galerias/influenza',


        ],
        'rules':[
            r'(.*)/salud/archivo/articulos(.*)',
            r'(.*)/salud/en/archivo/prensa(.*)',
            r'(.*)/salud/en/prensa(.*)',
            r'(.*)salud/en/articulos(.*)',
            r'(.*)/salud/en/archivo/documentos(.*)',
            r'(.*)/salud/acciones-y-programas/personal-de-la-salud(.*)',
            r'(.*)/senasica(.*)',
            r'(.*)/salud/acciones-y-programas(.*)',
            r'(.*)/temas/archivo/galerias/influenza(.*)',
            r'(.*)/salud/censia/galerias(.*)'

        ],
        'publish':[
            {
                'rule':'//section[contains(@class,"border-box")]/dl/dd[2]/text()',
                'format':'%B %d, %Y'
            },
            {
                'rule':'//section[contains(@class,"border-box")]/dl/dd[1]/text()',
                'format':'%Y-%m-%d',
                'extra':mx_time_sub,

            }

        ]

    },
    ## 洪都拉斯 打不开
    'hn':{
        'allowed_domains':['go.hn'],
        'site_url':'http://health.go.hn',
        'start_urls':[''],
        'rules':[],

    },
    ## 危地马拉
    'gt':{
        'allowed_domains':['gob.gt'],
        'site_url':'http://www.mspas.gob.gt',
        'start_urls':[
            'http://www.mspas.gob.gt/index.php/noticias/comunicados',
            'http://www.mspas.gob.gt/index.php/servicios'
        ],
        'rules':[
            r'(.*)/index\.php/noticias(.*)',
            r'(.*)/index\.php/servicios(.*)',
            r'(.*)index\.php/institucional(.*)',

            


        ],
        'publish':[
            {
                'rule':'normalize-space(string(//*[@id="content"]/article//*[contains(@class,"blog-article-date")]))',
                'format':'%b %d %Y'
            }

        ]

    },
    ## 萨尔瓦多 打不开
    'sv':{
        'allowed_domains':['gob.sv'],
        'site_url':'http://www.mspas.gob.sv',
        'start_urls':[''],
        'rules':[],
    },
    ## 牙买加 通过
    'jm':{
        'allowed_domains':['moh.gov.jm'],
        'site_url':'http://moh.gov.jm',
        'start_urls':[
            'http://moh.gov.jm/updates/press-releases',
        ],
        'rules':[
            r'(.*)/updates/press-releases(.*)',
            r'(.*)/(.*)'

        ],
        'excludes':[

        ],
        'publish':[
            {
                'rule':'//*[contains(@class,"entry-meta")]//time[contains(@class,"entry-date published")]/@datetime',
                'format':'%Y-%m-%dT%H:%M:%S-05:00'
            }

        ]
    },
    ## 特立尼达和多巴哥 时间解析过于不鲁棒
    'tt':{
        'allowed_domains':['health.gov.tt'],
        'site_url':'http://www.health.gov.tt',
        'start_urls':[
            'http://www.health.gov.tt',
            'http://www.health.gov.tt/news',

        ],
        'rules':[
            r'(.*)/news(.*)',
            r'(.*)/sitepages/default\.aspx(.*)',


        ],
        'publish':[
            {
                'rule':'//*[@id="ctl00_cphCore_GridView1_ctl02_Table2"]//td[@valign="top"]/text()[2]',
                'format':'%A, %B %d, %Y'
            }
        ]


    },
    ## 巴哈马 TODO
    'bs':{
        'allowed_domains':['gov.bs'],
        'site_url':'http://www.bahamas.gov.bs',
        'start_urls':[
            'http://www.bahamas.gov.bs/health'
        ],
        'rules':[

        ],

    },

    ## 伯利兹
    'bz':{
        'allowed_domains':['enum.hu'],
        'site_url':'http://www.eum.hu',
        'start_urls':[
            'http://www.belize.gov.bz/index.php/ministry-of-health'
        ],
        'rules':[
            
        ],
        'publish':[

        ]


    },
    ## 尼加瓜拉 通过
    'ni':{
        'allowed_domains':['minsa.gob.ni'],
        'site_url':'http://www.minsa.gob.ni',
        'start_urls':[
            'http://www.minsa.gob.ni',

        ],
        'rules':[
            r'(.*)index\.php/(.*)noticias(.*)',
            r'(.*)index\.php/enlaces(.*)',
            r'(.*)index\.php/repository(.*)',
            r'(.*)index\.php/directorio(.*)',

        ],
        'publish':[
            {
                'rule':'//*[@id="contenido"]/div[3]/p[position()= (last()-1)]/strong/text()',
                'format':'%Y-%m-%d',
                'extra':ni_time_sub,
            }
        ]

    },
    ## 哥斯达黎加 没有网站

    ## 巴拿马 通过
    'pa':{
        'allowed_domains':['minsa.gob.pa'],
        'site_url':'http://www.minsa.gob.pa',
        'start_urls':[
            'http://www.minsa.gob.pa/noticias-breves',
            'http://www.minsa.gob.pa/destacados',
            'http://www.minsa.gob.pa/informacion-salud',
            'http://www.minsa.gob.pa/direccion',
            'http://www.minsa.gob.pa/regiones-de-salud',
            'http://www.minsa.gob.pa/proyectos',
            'http://www.minsa.gob.pa/programas',
            'http://www.minsa.gob.pa/centro-de-prensa',
        ],
        'rules':[
            r'(.*)/noticias-breves(.*)',
            r'(.*)/destacados(.*)',
            r'(.*)/informacion-salud(.*)',
            r'(.*)/direccion(.*)',
            r'(.*)/regiones-de-salud(.*)',
            r'(.*)/proyectos(.*)',
            r'(.*)/programas(.*)',
            r'(.*)/noticia(.*)',
            r'(.*)/campana(.*)',
            r'(.*)/promocion-salud(.*)'
        ],
        'publish':[
            {
            'rule':'//*[@id="block-system-main"]//article//footer/span/@content',
            'format':'%Y-%m-%dT%H:%M:%S-05:00'
            },
        ]
    },

    ## 古巴 打不开
    'cu':{
        'allowed_domains':['minsa.gob.cu'],
        'site_url':'http://www.minsa.gob.cu',
        'start_urls':[''],
        'rules':[],

    },
    ## 海地 没有网站

    ## 安提瓜和巴布达 通过
    'ag':{
        'allowed_domains':['mbs.gov.ag'],
        'site_url':'http://mbs.gov.ag',
        'start_urls':[
            'http://mbs.gov.ag'
        ],
        'rules':[
            r'(.*)/press_releases(.*)',
            r'(.*)/information(.*)',  
        ],
    },
    ## 多米尼克 网站开发中
    'dm':{
    },
    ## 多米尼加 打不开
    'do':{

    },
    ## 圣卢西亚 打不开
    'lc':{

    },
    ## 圣基茨和尼维斯 打不开
    'kn':{

    },
    ## 巴巴多斯 通过
    'bb':{
        'allowed_domains':['health.gov.bb'],
        'site_url':'http://health.gov.bb',
        'start_urls':[
            'http://health.gov.bb'
        ],
        'rules':[
            r'(.*)/ministry_health(.*)',
        ],
    },
    ## 格林纳达 通过
    'gd':{
        'allowed_domains':['health.gov.gd'],
        'site_url':'http://health.gov.gd',
        'start_urls':[
            'http://health.gov.gd/index.php?lang=en',
        ],
        'rules':[
            r'(.*)/index\.php(.*)'
        ]
    },
    ## 圣文森特和格林纳丁斯 未通过
    'vc':{
        'allowed_domains':['moh.gov.vc'],
        'site_url':'http://moh.gov.vc',
        'start_urls':[
            'http://moh.gov.vc/health',
        ],
        'rules':[
            r'(.*)/health/index\.php(.*)',

        ]
    },
    ###############################################
    # 南美洲
    ###############################################

    ## 哥伦比亚 通过
    'co':{
        'allowed_domains':['minsalud.gov.co'],
        'site_url':'https://www.minsalud.gov.co',
        'start_urls':['https://www.minsalud.gov.co/English/Paginas/ABC-victims.aspx','https://www.minsalud.gov.co/English/Paginas/Social-Health-Promotion.aspx','https://www.minsalud.gov.co/English/Paginas/inicio.aspx','https://www.minsalud.gov.co/English/Paginas/historico-noticias.aspx'],
        'rules':[r'(.*)/English/Paginas(.*)'],
        'publish':[
            {
                'rule':'//*[@id="DeltaPlaceHolderMain"]//*[contains(@class,"fecha")]/text()',
                'format':'%d/%m/%Y'
            }
        ]

    },
    ## 厄瓜多尔 打不开
    'ec':{
        'allowed_domains':['msp.gov.ec'],
        'site_url':'http://www.msp.gov.ec',
        'start_urls':[],
        'rules':[]

    },
    # 委瑞内拉 无效
    've':{
        'allowed_domains':['platino.gov.ve'],
        'site_url':'http://www.platino.gov.ve',
        'start_urls':[],
        'rules':[]
    },

    # 圭亚那 打不开
    'gy':{
        'allowed_domains':['sdnp.org.gy'],
        'site_url':'http://www.sdnp.org.gy',
        'start_urls':[],
        'rules':[]
    },

    # 苏里南 通过
    'sr':{
        'allowed_domains':['www.gov.sr'],
        'site_url':'http://www.gov.sr',
        'start_urls':['http://www.gov.sr/ministerie-van-volksgezondheid/publicaties.aspx'],
        'rules':[r'(.*)/ministerie-van-volksgezondheid/publicaties(.*)'],
        'publish':[]
    },

     # 秘鲁 网站暂时下线
    'pe':{
        'allowed_domains':['minsa.gob.pe'],
        'site_url':'http://www.minsa.gob.pe',
        'start_urls':['http://www.minsa.gob.pe/portalweb/02estadistica/estadistica_1.asp?sub5=2','http://www.minsa.gob.pe/portalweb/index_est03.asp?box=4','http://www.minsa.gob.pe/portalweb/index_pro03.asp?box=1'],
        'rules':[r'(.*)/portalweb/02estadistica/(.*)',r'(.*)/estadisticas/estadisticas(.*)',r'(.*)/portalweb/07profesionales(.*)'],
        'publish':[
            {
                'rule':'',
                'format':''
            }
        ]
    },
    
    # 玻利维亚 打不开
    'bo':{
        'allowed_domains':['sns.gov.bo'],
        'site_url':'http://www.sns.gov.bo',
        'start_urls':[],
        'rules':[]
          
        
    },
    ## 巴拉圭 (样式有问题)
    'py':{
        'allowed_domains':['mspbs.gov.py'],
        'site_url':'https://www.mspbs.gov.py',
        'start_urls':[
            'https://www.mspbs.gov.py',
            'https://www.mspbs.gov.py/portal','https://www.mspbs.gov.py/dgtic','https://www.mspbs.gov.py/dnerhs',
            'http://www.mspbs.gov.py/rrhh','https://www.mspbs.gov.py/dnvs','https://www.mspbs.gov.py/planificacion',
            'http://www.mspbs.gov.py/dggies','https://www.mspbs.gov.py/dgrrii','https://www.mspbs.gov.py/drcps',
        ],
        'rules':[
            r'(.*)/portal/(.*)',r'(.*)/digies(.*)',r'(.*)/dgtic(.*)',r'(.*)/dnerhs(.*)',r'(.*)/rrhh(.*)',
            r'(.*)/dnvs(.*)',r'(.*)/planificacion(.*)',r'(.*)/dggies(.*)',r'(.*)/dgrrii(.*)',r'(.*)/drcps(.*)',  
        ],
        'publish':[
            # {
            #     'rule':'normalize-space(//*[contains(@class,"news-bar")]//*[contains(@class,"time-clock")])',
            #     'format':'%d %b, %Y'
            # }

        ]
    },

    # 巴西 通过(样式会乱)
    'br':{
        'allowed_domains':['saude.gov.br'],
        'site_url':'http://portalms.saude.gov.br',
        'start_urls':[
            'http://portalms.saude.gov.br',
            'http://portalms.saude.gov.br/noticias',
            'http://www.blog.saude.gov.br',
            'http://www.blog.saude.gov.br/promocao-da-saude'
        ],
        'rules':[
            r'(.*)/noticias(.*)',
            r'(.*)index\.php/servicos(.*)',
            r'(.*)/promocao-da-saude(.*)',
            r'(.*)index\.php/promocao-da-saude(.*)',
            r'(.*)index\.php/entenda-o-sus-home(.*)',
            r'(.*)index\.php/perguntas-e-respostas-home(.*)',
            r'(.*)index\.php/cursos-e-eventos-home(.*)',
            r'(.*)index\.php/combate-ao-aedes-home(.*)',
            r'(.*)index\.php/materias-especiais(.*)',
            r'(.*)/acoes-e-programas(.*)',

        ],
        'publish':[
            {
                'rule':'//*[@id="content-section"]//*[contains(@class,"documentPublished")]/text()',
                'extra':br_time_sub,
                'format':'%Y-%m-%d %H:%M',
            },
            {
                'rule':'//*[@id="content-section"]//*[contains(@class,"documentByLine")]/ul[2]/li[1]/text()[2]',
                'extra':br_time_sub,
                'format':'%Y-%m-%d %H:%M',

            }
        ]
          
        
    },

    # 智利 scrapy all thing 通过
    'cl':{
        'allowed_domains':['deis.cl'],
        'site_url':'http://www.deis.cl',
        'start_urls':[
            'http://www.deis.cl',
            'http://www.deis.cl/indicadores-basicos-de-salud',
            'http://www.deis.cl/estadisticas-de-natalidad-y-mortalidad',
            'http://www.deis.cl/estadisticas-de-atenciones-y-recursos-para-la-salud',
            'http://www.deis.cl/estadisticas-de-enfermedades-de-notificacion-obligatoria',
            'http://www.deis.cl/prensa-y-otras-publicaciones-2',
            'http://www.deis.cl/archivo-historico',
            'http://www.deis.cl/category/agenda',
            'http://www.deis.cl/category/noticias',
            'http://www.deis.cl/estandares-y-normativas'
        ],
        'rules':[
            r'(.*)'
        ],
        'exludes':[]   
    },

    # 阿根廷 再说
    'ar':{
        'allowed_domains':['msal.gob.ar'],
        'site_url':'http://www.msal.gov.ar',
        'start_urls':[],
        'rules':[
          
        ]
    },

    # 乌拉圭 通过
    'uy':{
        'allowed_domains':['msp.gub.uy'],
        'site_url':'http://www.msp.gub.uy',
        'start_urls':[
            'http://www.msp.gub.uy',
            'http://www.msp.gub.uy/listado-de-noticias',
            'http://www.msp.gub.uy/comunicados'

        ],
        'rules':[
            r'(.*)/comunicado(.*)',
            r'(.*)/noticia(.*)',
            r'(.*)/programa(.*)',
            r'(.*)/publicación(.*)',
            r'(.*)/publicaciones(.*)',
            r'(.*)/publica(.*)'
        ],
        'publish':[
            {
                'rule':'//*[@id="content"]//*[contains(@class,"field-fecha-noticia")]/text()',
                'format':'%d/%m/%Y'
            },
            {
                'rule':'//*[@id="content"]//*[contains(@class,"date-display-single")]/text()',
                'format':'%Y-%m-%d',
                'extra':uy_time_sub
            }
        ]
    },
    ###############################################
    # 大洋洲
    ###############################################

    # 新西兰 通过
    'nz':{
        'allowed_domains':['health.govt.nz'],
        'site_url':'http://www.health.govt.nz',
        'start_urls':['http://www.health.govt.nz','http://www.health.govt.nz/nz-health-statistics','http://www.health.govt.nz/publications'],
        'rules':[
            r'(.*?)/nz-health-statistics(.*)',
            r'(.*?)/publication(.*)',
        ],
        'publish':[
            {
                'rule':'//article//*[@class="date-display-single"]/@content',
                'format':'%Y-%m-%dT%H:%M:%S+13:00'
            },
            # {
            #     'rule':'//*[@id="content-footer"]//*[@class="date"]/text()',
            #     'format':'%d %B %Y'
            # },
        ]
    },
    # 斐济群岛 通过
    'fj':{
        'allowed_domains':['health.gov.fj'],
        'site_url':['http://www.health.gov.fj'],
        'start_urls':['http://www.health.gov.fj','http://www.health.gov.fj/?page_id=198'],
        'rules':[]
    },

    # 澳大利亚 需要过滤的文件过多
    'au':{
        'allowed_domains':['health.gov.au'],
        'site_url':'http://www.health.gov.au',
        'start_urls':[
            'http://www.health.gov.au'
        ],
        'rules':[
            r'(.*)/internet/main/publishing\.nsf/Content/(.*)',
        ],
        'excludes':[
            ## Ministers
            r'(.*)/internet/main/publishing\.nsf/Content/CurrentIssues(.*)',
            ## For Consumers
            r'(.*)/internet/main/publishing\.nsf/Content/Aboriginal\+and\+Torres\+Strait\+Islander\+Health-1lp(.*),
            r'(.*)/internet/main/publishing\.nsf/Content/health-ethics-index\.htm(.*),
            r'(.*)/internet/main/publishing\.nsf/Content/health-care-homes(.*),
            r'(.*)/internet/main/publishing\.nsf/Content/Healthcare\+systems-1(.*),
            r'(.*)/internet/main/publishing\.nsf/Content/health-medicarebenefits-index\.htm(.*),
            r'(.*)/internet/main/publishing\.nsf/Content/Mental\+Health\+and\+Wellbeing-1(.*),
            r'(.*)/internet/main/publishing\.nsf/Content/national-mens-and-womens-health-1(.*),
            r'(.*)/internet/main/publishing\.nsf/Content/National-Rural-Health-Commissioner(.*),
            r'(.*)/internet/main/publishing\.nsf/Content/norfolk-is(.*),
            r'(.*)/internet/main/publishing\.nsf/Content/palliative-care-and-end-of-life-care(.*),
            r'(.*)/internet/main/publishing\.nsf/Content/consumer-pharmacy(.*),
            r'(.*)/internet/main/publishing\.nsf/Content/primarycare(.*),
            r'(.*)/internet/main/publishing\.nsf/Content/,
            r'(.*)/internet/main/publishing\.nsf/Content/,
            r'(.*)/internet/main/publishing\.nsf/Content/,
            r'(.*)/internet/main/publishing\.nsf/Content/,
            r'(.*)/internet/main/publishing\.nsf/Content/,
            r'(.*)/internet/main/publishing\.nsf/Content/,
            r'(.*)/internet/main/publishing\.nsf/Content/,
            r'(.*)/internet/main/publishing\.nsf/Content/,
            r'(.*)/internet/main/publishing\.nsf/Content/,




                   
        ]
        
    },

    # 巴布亚新几内亚 通过
    'pg':{
        'allowed_domains':['health.gov.pg'],
        'site_url':'http://www.health.gov.pg',
        'start_urls':['http://www.health.gov.pg','http://www.health.gov.pg/pages/healthpolicyA.htm','http://www.health.gov.pg/pages/healthpolicyD.htm','http://www.health.gov.pg/pages/healthpolicyH.htm','http://www.health.gov.pg/pages/healthpolicyM.htm','http://www.health.gov.pg/pages/healthpolicyP.htm'],
        'rules':[]
    },

    # 所罗门群岛 打不开
    'sb':{
        'allowed_domains':['health.gov.sb'],
        'site_url':'http://www.health.gov.sb',
        'start_urls':[],
        'rules':[]
    },

    # 瓦努阿图 打不开
    'vu':{
        'allowed_domains':['moh.gov.vu'],
        'site_url':'https://moh.gov.vu',
        'start_urls':[],
        'rules':[]
    },
    # 帕罗 已废弃
    'pw':{
        'allowed_domains':['health.gov.pw'],
        'site_url':'http://health.gov.pw',
        'start_urls':[],
        'rules':[]
    },

    # 密克罗尼西亚联邦 打不开
    'fm':{
        'allowed_domains':['health.gov.fm'],
        'site_url':'http://health.gov.fm',
        'start_urls':[],
        'rules':[]
    },

    # 马绍尔群岛 打不开
    'mh':{
        'allowed_domains':['health.gov.mh'],
        'site_url':'http://health.gov.mh',
        'start_urls':[],
        'rules':[]

    },

    # 基里巴斯 通过
    'ki':{
        'allowed_domains':['health.gov.ki'],
        'site_url':'http://health.gov.ki',
        'start_urls':['http://www.health.gov.ki/download.html','http://www.health.gov.ki/health-news.html','http://www.health.gov.ki/documents.html','http://www.health.gov.ki/iec-materials.html','http://www.health.gov.ki/forms.html'],
        'rules':[r'(.*)/download/category/(.*)',r'(.*)/health-news/(.*)']
    },
    # 瑙鲁 打不开
    'nr':{
        'allowed_domains':['health.gov.nr'],
        'site_url':'http://health.gov.nr',
        'start_urls':[''],
        'rules':[]
    },

    # 图瓦卢 打不开
    'tv':{
        'allowed_domains':['health.gov.tv'],
        'site_url':'http://health.gov.tv',
        'start_urls':[''],
        'rules':[]

    },

    # 汤加 通过
    'to':{
        'allowed_domains':['health.gov.to'],
        'site_url':'http://health.gov.to',
        'start_urls':['http://www.health.gov.to/drupal/?q=node/26','http://www.health.gov.to/drupal/?q=Annual','http://www.health.gov.to/drupal/sites/default/files/MOH%20Corporate%20Plan%202008-2012.pdf','http://www.health.gov.to/drupal/sites/default/files/Tongan%20Registered%20List%20of%20Medicinal%20%20Drugs%20Final%20-%20MARCH%202016.xlsx'],
        'rules':[r'(.*)/drupal/sites/default/file(.*)'],
    },

    # 萨摩亚 通过
    'ws':{
        'allowed_domains':['health.gov.ws'],
        'site_url':'http://www.health.gov.ws',
        'start_urls':['http://www.health.gov.ws','http://www.health.gov.ws/publications0/legislations','http://www.health.gov.ws/publications0/findings-and-reports'],
        'rules':[
            r'(.*)/component/content/article(.*)',
            r'(.*)/health-warning-alerts/(.*)'
        ],
        'publish':[
            {
                'rule':'//*[@id="sp-component"]//*[@class="article-info"]//time[@datetime]/@datetime',
                'format':'%Y-%m-%dT%H:%M:%S+14:00'
            }
        ]

    }
}

ALLOWED_FILE_DOWNLOAD = [
    'text/xml','text/plain','text/html',
    # 'image/jpeg','application/x-bmp','image/fax','image/x-icon','image/jpeg','application/x-jpg','application/x-png','image/tiff',
    'application/vnd.ms-powerpoint','application/vnd.ms-powerpoint','application/x-ppt',
    'application/msword','application/octet-stream',
    'application/x-xls','application/vnd.ms-excel',
    'application/pdf',
]

    
class MohSpider(scrapy.Spider):

    name = 'moh'

    def __init__(self, domain=None, debug=None, debug_url=None,html_update = 0,attachment_update = 30,asset_update = 10,*args, **kwargs):

       super(MohSpider, self).__init__()
       params = configure[domain]
       self.allowed_domains = params['allowed_domains']
       self.site_url = params['site_url']
       self.output_dir = settings['DATA_OUTPUT']
       if debug_url:
           self.start_urls = [debug_url]
       else:
           self.start_urls = params['start_urls']
       self.rules = params['rules'] or []
       self.excludes = params.get('excludes') or []
       self.publish = params.get('publish') or []
       self.language = params.get('language') or ''
       self.nation = domain
       self.debug = debug
    #    self.history = self.load_history()
       self.html_update = int(html_update)
       self.attachment_update = int(attachment_update)
       self.asset_update = int(asset_update)
       self.now = datetime.datetime.now()

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
        return spider

    def spider_closed(self,spider):
        # self.save_history()
        pass
       

    def save_history(self):
        if self.debug:
            history_file = os.path.join(settings['HISTORY_DIR'],self.nation + '-debug.json')
        else:
            history_file = os.path.join(settings['HISTORY_DIR'],self.nation + '.json')
        if self.history:
            json.dump(self.history,codecs.open(history_file,'w','utf-8'))



    def content_allowed(self,content_type):
        for item in ALLOWED_FILE_DOWNLOAD:
            if item in content_type:
                return True
        return False

    def start_requests(self):
        for url in self.start_urls:
            if self.nation in ['rw']:
                yield scrapy.Request(url,cookies={'_accessKey2':'CD2we/sGT5LdZuwhvlgz3y4zkhvdvTTh'})
            else:
                yield scrapy.Request(url)


    def should_update(self,record):
        if not record:
            return True

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
            if not self.url_in_rule(record.get('url')):
                return False
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

        if last_update_date + delta > now:
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
            if not self.url_in_rule(response.url):
                last_update = datetime.date.today()
                saved_record = {'url':response.url,'type':'html','content_type':content_type,'last_update':last_update.strftime('%Y-%m-%d'),'valid':False}
                self.save_record(response.url,saved_record)
                return

            resource = ResourceItem()
            resource['url'] = response.url
            resource['rtype'] = 'html'
            resource['location'] = self.site_url
            resource['language'] = self.language_inference(response)
            resource['publish'] = self.publish_time_inference(response)
            resource['nation'] = self.nation
            resource['content_type'] = content_type

            text = self.h2t(response)
            resource['content'] = response.text
            resource['keywords'] = json.dumps(self.text2keywords(text,resource['language'],keywords_num=5))

            title_from_meta = response.meta.get('title') or ''
            title_from_html = response.xpath('//title/text()').extract()

            
            if len(title_from_html):
                title_from_html = title_from_html[0]
            else:
                title_from_html = ''
            
            # if len(title_from_meta) < len(title_from_html):
            #     title = title_from_html 
            # else:
            #     title = title_from_meta
            if title_from_meta:
                title = title_from_meta
            else:
                title = title_from_html

            resource['title'] = title

            # saved_record = {'content_type':content_type,'url':resource['url'],'type':resource['rtype']}
            # self.save_record(response.url,saved_record)

            should_update = self.should_update(record)
            if not self.debug and should_update:
                yield resource

            # last_update = datetime.date.today()
           
            print '*'*40
            print '(url,language,publish,title)',resource['url'],resource['language'],resource['publish'],resource['title']
            
            ## get html base
            base = response.xpath('//base[@href]/@href').extract()
            if len(base):
                base = base[0]
            else:
                base = None
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
                    request = scrapy.Request(http_url,callback=self.parse,meta={'title':link_title})
                    _record = self.get_record(http_url)
                    should_update = self.should_update(_record)
                    # print '*'*40
                    # print http_url,should_update
                    # print '*'*40
                    if should_update:
                        # print http_url
                        yield request
                    
                    # if self.debug:
                    #     print 'yield http url %s from %s'%(http_url,response.url)
                    # if http_url == 'http://www.mz.gov.pl/wp-content/uploads/2015/07/Wczesne-wykrywanie-dane-krajowe.ppt':
                    #     print 'yield http url %s from %s'%(http_url,response.url)
                    #     print 'link title is ',link_title
                    #     return
            stylesheets = response.xpath(
                '//link[@type="text/css"]/@href').extract()
            
            for stylesheet in stylesheets:
                http_url = self.gen_http_url(response.url, stylesheet,base)
                if http_url:
                    request = scrapy.Request(http_url, callback=self.style_parse)
                    _record = self.get_record(http_url)
                    should_update = self.should_update(_record)
                    if should_update:
                        yield request

            javascripts = response.xpath('//script[@src]/@src').extract()
            for javascript in javascripts:
                http_url = self.gen_http_url(response.url,javascript,base)
                if http_url:
                    request = scrapy.Request(http_url, callback=self.assets_parse)
                    
                    _record = self.get_record(http_url)

                    should_update = self.should_update(_record)
                    if should_update and self.url_in_rule(http_url):
                        
                        yield request

            images = response.xpath('//img[@src]/@src').extract() or []
            input_images = response.xpath(
                '//input[@type="image"]/@src').extract() or []
            images.extend(input_images)
            for img in images:
                img_http_url = self.gen_http_url(response.url,img,base)
                if img_http_url:
                    request = scrapy.Request(img_http_url, callback=self.assets_parse)

                    _record = self.get_record(img_http_url)
                    should_update = self.should_update(_record)
                    if should_update:
                        yield request

        elif content_type and self.content_allowed(content_type):  
            resource = ResourceItem()
            resource['url'] = response.url
            resource['content'] = response.body
            resource['rtype'] = 'attachment'
            resource['location'] = self.site_url
            resource['nation'] =  self.nation
            resource['content_type'] = content_type
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

        if not self.debug:
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
                    t = time.strftime("%Y-%m-%dT%H:%M:%SZ",t)
                    break
            return t
        except:
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

        if not self.debug:
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
                    should_update = self.should_update(record)
                    request = scrapy.Request(http_url,self.style_parse)
                    if should_update:
                        yield request
                    
            elif hasattr(item,'declarations'):
                for decl in getattr(item,'declarations'):
                    for decl_val in getattr(decl,'value'):
                        if getattr(decl_val,'type') == u'URI':
                            uri = getattr(decl_val,'value')
                            image_url = self.gen_http_url(url,uri,None)
                            if image_url:
                                record = self.get_record(image_url)
                                should_update = self.should_update(record)
                                request = scrapy.Request(image_url,self.assets_parse)
                                if should_update:
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
                return tr4w.get_keywords(keywords_num=keywords_num, word_min_len=1)
            # 其他网页关键词提取，用summa textrank
            else:
                k = keywords.keywords(text,scores=True)
                return k[0:keywords_num]
        except Exception,e:
            pass

        

if __name__ == '__main__':
    spider = MohSpider(domain='us',debug=True)
    # record = spider.get_record('http://download.mohw.go.kr/react/modules/download.jsp?BOARD_ID=1365&CONT_SEQ=289977&FILE_SEQ=138058&FILE_NAME=[ENG][8.19]Preparation%20for%20a%20healthy%202nd%20semester!%20Get%20vaccination%20shots,%20and%20follow%20sanitation%20recommendations.docx')
    # print spider.should_update(record)
    
    spider.save_record('http://download.mohw.go.kr/react/modules/download.jsp',{'aa':1})

    spider.save_record('http://download.mohw.go.kr/react/modules/download.jsp',{'bb':1})
        
            
