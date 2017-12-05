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
        'start_urls':['http://www.moh.gov.cn/zwgk/jdjd/ejlist.shtml'],
        'rules':[r'(.*)/zwgk/jdjd/(.*)'],
        'language':'zh',
        'publish':[{'rule':"//span[@class='time']/text()",'format':'%Y-%m-%d'}]

    },
     # 澳大利亚
    'au':{
        'allowed_domains':['health.gov.au'],
        'site_url':'http://www.health.gov.au',
        'start_urls':['http://www.health.gov.au/internet/main/publishing.nsf/Content/health-publicat.htm','http://www.health.gov.au/internet/main/publishing.nsf/Content/Research+&+Statistics-1','http://www.health.gov.au/internet/main/publishing.nsf/Content/CurrentIssues'],
        'rules':[r'(.*)/internet/main/publishing\.nsf/Content/(.*)'],
        'excludes':[r'(.*)internet/main/publishing\.nsf/Content/health-overview\.htm(.*)',r'(.*)internet/main/publishing.nsf/Content/health-central\.htm(.*)',r'(.*)internet/main/publishing\.nsf/Content/Budget-1(.*)',r'(.*)/internet/main/publishing\.nsf/Content/Listing\+of\+Tenders\+and\+Grants-1(.*)',r'(.*)/internet/main/publishing\.nsf/Content/health-eta2\.htm(.*)',r'(.*)internet/main/publishing\.nsf/Content/reporting-fraud-misconduct-compliance(.*)',r'(.*)/internet/main/publishing\.nsf/Content/foi-about(.*)',r'(.*)internet/main/publishing\.nsf/Content/public-interest-disclosure(.*)',r'(.*)internet/main/publishing\.nsf/Content/health-contracts-index\.htm(.*)',r'(.*)/internet/main/publishing\.nsf/Content/health-eta2\.htm(.*)',r'(.*)/internet/main/publishing\.nsf/Content/social-media-channels(.*)',r'(.*)/internet/main/publishing\.nsf/Content/Career\+Opportunities-1(.*)',r'(.*)/internet/main/publishing\.nsf/Content/health-pubs-calendar-index\.htm(.*)',r'(.*)/internet/main/publishing\.nsf/Content/health-history\.htm(.*)',r'(.*)/internet/main/publishing\.nsf/Content/Australian\+Health\+Ministers%27\+Conference-1(.*)',r'(.*)/internet/main/publishing\.nsf/Content/Council\+of\+Australian\+Governments(.*)',r'(.*)/internet/main/publishing\.nsf/Content/Agreements-1(.*)',r'(.*)/internet/main/publishing\.nsf/Content/eHealth(.*)',r'(.*)/internet/main/publishing\.nsf/Content/programs-initiatives-menu(.*)',r'(.*)/internet/main/publishing\.nsf/Content/campaign_certification_statements-lp(.*)',r'(.*)/internet/main/publishing\.nsf/Content/Australian\+Health\+Ministers%27\+Conference-1(.*)',r'(.*)/internet/main/publishing\.nsf/Content/Council\+of\+Australian\+Governments(.*)',r'(.*)/internet/main/publishing\.nsf/Content/Departmental\+media\+releases\+and\+speeches-1(.*)',r'(.*)/internet/main/publishing\.nsf/Content/health-mediarel-subscribe-index\.htm',r'(.*)/internet/main/publishing\.nsf/Content/Ministers-1(.*)',r'(.*)/internet/main/publishing\.nsf/Content/government-responses(.*)']
        
    },

    # 萨摩亚
    'ws':{
        'allowed_domains':['health.gov.ws'],
        'site_url':'http://www.health.gov.ws',
        'start_urls':'',
        'rules':[],
        'publish':[]
    },
    ###############################################
    # 亚洲
    ###############################################


    ###############################################
    # 欧洲
    ###############################################



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
    ## 牙买加
    'jm':{
        'allowed_domains':['gov.jm'],
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
        'allowed_domains':['gov.tt'],
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
    ## 尼加瓜拉
    'ni':{
        'allowed_domains':['gob.ni'],
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

    ## 巴拿马
    'pa':{
        'allowed_domains':['gob.pa'],
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
        'allowed_domains':['gob.cu'],
        'site_url':'http://www.minsa.gob.cu',
        'start_urls':[''],
        'rules':[],

    },
    ## 海地 没有网站

    ## 安提瓜和巴布达
    'ag':{
        'allowed_domains':['gov.ag'],
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
    ## 巴巴多斯
    'bb':{
        'allowed_domains':['gov.bb'],
        'site_url':'http://health.gov.bb',
        'start_urls':[
            'http://health.gov.bb'
        ],
        'rules':[
            r'(.*)/ministry_health(.*)',
        ],
    },
    ## 格林纳达
    'gd':{
        'allowed_domains':['gov.gd'],
        'site_url':'http://health.gov.gd',
        'start_urls':[
            'http://health.gov.gd/index.php?lang=en',
        ],
        'rules':[
            r'(.*)/index\.php(.*)'
        ]
    },
    ## 圣文森特和格林纳丁斯
    'vc':{
        'allowed_domains':['gov.vc'],
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

    ## 哥伦比亚
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

    # 苏里南
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
    ## 巴拉圭
    'py':{
        'allowed_domains':['mspbs.gov.py'],
        'site_url':'https://www.mspbs.gov.py',
        'start_urls':[
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

    # 巴西
    'br':{
        'allowed_domains':['saude.gov.br'],
        'site_url':'http://portalms.saude.gov.br',
        'start_urls':[
            'http://portalms.saude.gov.br/noticias','http://blog.saude.gov.br','http://www.blog.saude.gov.br/promocao-da-saude'
        ],
        'rules':[
            r'(.*)/noticias(.*)',r'(.*)index\.php/servicos(.*)',r'(.*)/promocao-da-saude(.*)',r'(.*)index\.php/promocao-da-saude(.*)',
            r'(.*)index\.php/entenda-o-sus-home(.*)',r'(.*)index\.php/perguntas-e-respostas-home(.*)',r'(.*)index\.php/cursos-e-eventos-home(.*)',
            r'(.*)index\.php/combate-ao-aedes-home(.*)',r'(.*)index\.php/materias-especiais(.*)',r'(.*)/acoes-e-programas(.*)',

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

    # 智利 scrapy all thing
    'cl':{
        'allowed_domains':['deis.cl'],
        'site_url':'http://www.deis.cl',
        'start_urls':[
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

    # 乌拉圭
    'uy':{
        'allowed_domains':['msp.gub.uy'],
        'site_url':'http://www.msp.gub.uy',
        'start_urls':[
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

    # 新西兰
    'nz':{
        'allowed_domains':['health.govt.nz'],
        'site_url':'http://www.health.govt.nz',
        'start_urls':['http://www.health.govt.nz/nz-health-statistics','http://www.health.govt.nz/publications'],
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
    # 斐济群岛
    'fj':{
        'allowed_domains':['health.gov.fj'],
        'site_url':['http://www.health.gov.fj'],
        'start_urls':['http://www.health.gov.fj/?page_id=198'],
        'rules':[]
    },

    # 澳大利亚 TODO
    'au':{
        'allowed_domains':['health.gov.au'],
        'site_url':'http://www.health.gov.au',
        'start_urls':['http://www.health.gov.au/internet/main/publishing.nsf/Content/health-publicat.htm','http://www.health.gov.au/internet/main/publishing.nsf/Content/Research+&+Statistics-1','http://www.health.gov.au/internet/main/publishing.nsf/Content/CurrentIssues'],
        'rules':[r'(.*)/internet/main/publishing\.nsf/Content/(.*)'],
        'excludes':[r'(.*)/internet/main/publishing\.nsf/Content/health-overview\.htm(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/health-central\.htm(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/Annual\+Reports-3(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/Budget-1(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/Listing\+of\+Tenders\+and\+Grants-1(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/health-eta2\.htm(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/reporting-fraud-misconduct-compliance(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/foi-about(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/public-interest-disclosure(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/health-contracts-index\.htm(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/stakeholder-engagement(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/social-media-channels(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/Career\+Opportunities-1(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/health-pubs-calendar-index\.htm(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/health-history\.htm(.*)',

                    r'(.*)/internet/main/publishing\.nsf/Content/Australian\+Health\+Ministers%27\+Conference-1(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/Council\+of\+Australian\+Governments(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/Departmental\+media\+releases\+and\+speeches-1(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/Health\+Warnings-1(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/health-mediarel-subscribe-index\.htm(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/Ministers-1(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/government-responses(.*)',

                    r'(.*)/internet/main/publishing\.nsf/Content/Agreements-1(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/eHealth(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/programs-initiatives-menu(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/campaign_certification_statements-lp(.*)',

                    r'(.*)/internet/main/publishing\.nsf/Content/Aboriginal\+and\+Torres\+Strait\+Islander\+Health-1lp(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/Conditions\+and\+Diseases-[1-2](.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/Education\+and\+Prevention-[1-2](.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/Gene\+Technology-[1-2](.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/health-compliance(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/health-ethics-index.htm(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/health-care-homes(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/Health\+products\+and\+medicines-[1-2](.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/health-thesaurus.htm(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/Healthcare\+systems-[1-2](.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/health-medicarebenefits-index\.htm(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/Mental\+Health\+and\+Wellbeing-[1-2](.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/national-mens-and-womens-health-[1-2](.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/norfolk-is(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/Palliative\+Care-[1-2](.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/consumer-pharmacy(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/primarycare(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/regulation-and-red-tape-reduction(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/Rural\+Health-[1-2](.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/Services-[1-2](.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/healthiermedicare(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/Health\+Warnings-[1-2](.*)',

                    r'(.*)/internet/main/publishing\.nsf/Content/Health\+Workforce-2(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/health-care-homes-professional(.*)',
                    r'(.*)/internet/main/publishing\.nsf/Content/strongmedicare(.*)'



                   ]
        
    },

    # 巴布亚新几内亚
    'pg':{
        'allowed_domains':['health.gov.pg'],
        'site_url':'http://www.health.gov.pg',
        'start_urls':['http://www.health.gov.pg/pages/healthpolicyA.htm','http://www.health.gov.pg/pages/healthpolicyD.htm','http://www.health.gov.pg/pages/healthpolicyH.htm','http://www.health.gov.pg/pages/healthpolicyM.htm','http://www.health.gov.pg/pages/healthpolicyP.htm'],
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

    # 基里巴斯 
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

    # 汤加
    'to':{
        'allowed_domains':['health.gov.to'],
        'site_url':'http://health.gov.to',
        'start_urls':['http://www.health.gov.to/drupal/?q=node/26','http://www.health.gov.to/drupal/?q=Annual','http://www.health.gov.to/drupal/sites/default/files/MOH%20Corporate%20Plan%202008-2012.pdf','http://www.health.gov.to/drupal/sites/default/files/Tongan%20Registered%20List%20of%20Medicinal%20%20Drugs%20Final%20-%20MARCH%202016.xlsx'],
        'rules':[r'(.*)/drupal/sites/default/file(.*)'],
    },

    # 萨摩亚
    'ws':{
        'allowed_domains':['health.gov.ws'],
        'site_url':'http://www.health.gov.ws',
        'start_urls':['http://www.health.gov.ws','http://www.health.gov.ws/publications0/legislations','http://www.health.gov.ws/publications0/findings-and-reports'],
        'rules':[r'(.*)/component/content/article(.*)',r'(.*)/health-warning-alerts/(.*)'],
        'publish':[
            {
                'rule':'//*[@id="sp-component"]//*[@class="article-info"]//time[@datetime]/@datetime',
                'format':'%Y-%m-%dT%H:%M:%S+14:00'
            }
        ]

    }
}


class MohSpider(scrapy.Spider):

    name = 'moh'

    def __init__(self, domain=None, debug=None, debug_url=None,*args, **kwargs):

       super(MohSpider, self).__init__()
       params = configure[domain]
       self.allowed_domains = params['allowed_domains']
       self.site_url = params['site_url']
       self.output_dir = configure['output_dir']
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
    

    def start_requests(self):
        for url in self.start_urls:
            if self.nation in ['rw']:
                yield scrapy.Request(url,cookies={'_accessKey2':'CD2we/sGT5LdZuwhvlgz3y4zkhvdvTTh'})
            else:
                yield scrapy.Request(url)


    def parse(self, response):
        '''
        parse html to extract useful link and assets
        '''
        if response.headers and response.headers.get('Content-Type') and ('text/html' in response.headers['Content-Type']):
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
            
            resource['type'] = 'html'
            resource['location'] = self.site_url
            resource['language'] = self.language_inference(response)
            resource['publish'] = self.publish_time_inference(response)
            # print resource['publish']
            resource['nation'] = self.nation
            text = self.h2t(response)
            resource['content'] = response.body
            resource['keywords'] = json.dumps(self.text2keywords(text,resource['language'],keywords_num=5))

            if response.meta.get('title'):
                title = response.meta.get('title')
            else:
                title = response.xpath('//title/text()').extract()
                if len(title):
                    title = title[0]
                else:
                    title = ''

            resource['title'] = title
            

            if not self.debug:
                yield resource
            # return

            print '*'*40
            print '(url,language,publish,title)',resource['url'],resource['language'],resource['publish'],resource['title']

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
                    # if self.debug:
                    #     print 'yield http url %s from %s'%(http_url,response.url)
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
                if http_url and not self.debug:
                    yield scrapy.Request(http_url, callback=self.style_parse)

                    

            javascripts = response.xpath('//script[@src]/@src').extract()
            for javascript in javascripts:
                http_url = self.gen_http_url(response.url, javascript)
                if http_url and not self.debug:
                    yield scrapy.Request(http_url, callback=self.assets_parse)

            images = response.xpath('//img[@src]/@src').extract() or []
            input_images = response.xpath(
                '//input[@type="image"]/@src').extract() or []
            images.extend(input_images)
            for img in images:
                img_http_url = self.gen_http_url(response.url, img)
                if img_http_url and not self.debug:
                    yield scrapy.Request(img_http_url, callback=self.assets_parse)
        else:
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
            if not self.debug:
                yield resource
            print '*'*40
            print '(url,title)',resource['url'],resource['title']

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
        print '*'*40
        print ('css','url'),response.url
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
                return tr4w.get_keywords(keywords_num=keywords_num, word_min_len=1)
            # 其他网页关键词提取，用summa textrank
            else:
                k = keywords.keywords(text,scores=True)
                return k[0:keywords_num]
        except Exception,e:
            pass

        

if __name__ == '__main__':
    iq_time_sub("أرسلت بواسطة: أدارة الموقع | التاريخ: 2017-10-05 | الوقـت: 10:56:19 صباحا  | قراءة : 13")
    
        
            
