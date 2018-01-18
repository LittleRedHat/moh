#-*- coding=utf-8 -*-
import re
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
    #br2en = ['ene','feb','mar','abr','may','jun','jul','agos','sep','oct','nov', 'dic']
    if len(groups) >= 6:
        month = groups[2]
        for key,en in enumerate(pt_month):
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
    #br2en = ['ene','feb','mar','abr','may','jun','jul','agos','sep','oct','nov', 'dic']
    if len(groups) >= 4:
        month = groups[2]
        for key,en in enumerate(pt_month):
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
    #br2en = ['ene','feb','mar','abr','may','jun','jul','agos','sep','oct','nov', 'dic']
    if len(groups) >= 3:
        month = groups[1]
        for key,en in enumerate(pt_month):
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
    #br2en = ['ene','feb','mar','abr','may','jun','jul','agos','sep','oct','nov', 'dic']
    if len(groups) >= 3:
        month = groups[2]
        for key,en in enumerate(pt_month):
            if en.lower() in month.lower():
                month = str(key + 1)
                break
        day = groups[1]
        year = groups[3]
        return year+'-'+month+'-'+day    
spanish_month=['ene','feb','mar','abr','may','jun','jul','ago','sept','oct','nov','dic']
fr_month = ['jan','fév','mars','avr','mai','juin','juillet','aoû','sept','oct','nov','déc']
en_month = ['jan','feb','mar','apr','may','jun','jul','aug','sept','oct','nov','dec']
id_month = ['jan','feb','mar','apr','mei','jun','jul','aug','sept','okt','nov','des']
pt_month = ['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','deze']

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

def au_time_sub(text):
    
    p = r'(.*?)([0-9]{1,2}) (\w+) ([0-9]{4})'
    m = re.match(p,text)
    groups = m.groups()
    if len(groups) >=3:
        year = groups[3]
        month = groups[2]
        day = groups[1]
        return year+'-'+month+'-'+day

def ar_time_sub(text):
    p = r'(.*?)([0-9]{1,2}) de (\w+) de ([0-9]{4}) ([0-9]{1,2}):([0-9]{1,2})'
    m = re.match(p,text)
    groups = m.groups()
    #br2en = ['ene','feb','mar','abr','may','jun','jul','agos','sep','oct','nov', 'dic']
    if len(groups) >=6:
        month = groups[2]
        for key,en in enumerate(pt_month):
            if en.lower() in month.lower():
                month = str(key + 1)
                break
        year = groups[3]
        day = groups[1]
        hour= groups[4]
        minute = groups[5]
        return year+'-'+month+'-'+day+' '+hour+":"+minute

def ar_time_sub2(text):
    print 'text is',text
    p = r'(.*?)([0-9]{1,2}) de (\w+) de ([0-9]{4})'
    m = re.match(p,text)
    groups = m.groups()
    # br2en = ['ene','feb','mar','abr','may','jun','jul','agos','sep','oct','nov', 'dic']
    if len(groups) >=4:
        month = groups[2]
        for key,en in enumerate(spanish_month):
            if en.lower() in month.lower():
                month = str(key + 1)
                break
        year = groups[3]
        day = groups[1]
        print year+'-'+month+'-'+day
        return year+'-'+month+'-'+day

def pe_time_sub(text):
    p = r'(.*?)([0-9]{1,2}) de (\w+) del ([0-9]{4})'
    m = re.match(p,text)
    groups = m.groups()
    # br2en = ['ene','feb','mar','abr','may','jun','jul','agos','sep','oct','nov', 'dic']
    if len(groups) >=4:
        month = groups[2]
        for key,en in enumerate(pt_month):
            if en.lower() in month.lower():
                month = str(key + 1)
                break
        year = groups[3]
        day = groups[1]
        return year+'-'+month+'-'+day


def id_time_sub(text):
    p = r'(.*?)([0-9]{1,2}) (\w+) ([0-9]{4}) (.*)'
    m = re.match(p,text)
    groups = m.groups()
    if len(groups) >=5:
        month = groups[2]
        for key,en in enumerate(id_month):
            if en.lower() in month.lower():
                month = str(key + 1)
                break
        year = groups[3]
        day = groups[1]
        return year+'-'+month+'-'+day


def bh_time_sub(text):
    p = r'(.*?)([0-9]{1,2})/([0-9]{1,2})/([0-9]{4}) ([0-9]{1,2}):([0-9]{1,2}):([0-9]{1,2})(.*?)'
    m = re.match(p,text)
    # print "bh_time_sub",text
    groups = m.groups()
    if len(groups) >=6:
        month = groups[2]
        year = groups[3]
        day = groups[1]
        hour = groups[4]
        minute = groups[5]
        second = groups[6]
        
        return year+'-'+month+'-'+day+' '+hour+':'+minute+':'+second


def ch_time_sub(text):
    p = r'(.*?)([0-9]{1,2})\.([0-9]{1,2})\.([0-9]{4})'
    m = re.match(p,text)
    groups = m.groups()
    if len(groups) >=4:
        month = groups[2]
        year = groups[3]
        day = groups[1]
        return year+'-'+month+'-'+day


def rs_time_sub(text):
    p = r'(.*?)([0-9]{1,2})\.([0-9]{1,2})\.([0-9]{4})'
    m = re.match(p,text)
    groups = m.groups()
    if len(groups) >=4:
        month = groups[2]
        year = groups[3]
        day = groups[1]
        return year+'-'+month+'-'+day

def ba_time_sub(text):
    p = r'([0-9]{1,2}) (\w+?) ([0-9]{4})'
    m = re.match(p,text)
    groups = m.groups()
    if len(groups) >=3:
        month = groups[1]
        for key,en in enumerate(en_month):
            if en.lower() in month.lower():
                month = str(key + 1)
                break
        year = groups[2]
        day = groups[0]
        
        return year+'-'+month+'-'+day

def me_time_sub(text):
    p = r'([0-9]{1,2})\.([0-9]{1,2})\.([0-9]{4}) ([0-9]{1,2}):([0-9]{1,2})(.*?)'
    m = re.match(p,text)
    groups = m.groups()
    if len(groups) >=5:
        month = groups[1]
        year = groups[2]
        day = groups[0]
        hour = groups[3]
        minute = groups[4]
        return year+'-'+month+'-'+day+' '+hour+':'+minute

ro_month = ['ianuarie', 'februarie', 'martie', 'aprilie', 'mai', 'iunie', 'iulie', 'august', 'septembrie', 'octombrie', 'noiembrie', 'decembrie']
def ro_time_sub(text):
    p = r'([0-9]{1,2}) (\w+?) ([0-9]{4})'
    m = re.match(p,text)
    groups = m.groups()
    if len(groups) >=3:
        month = groups[1]
        for key,en in enumerate(ro_month):
            if en.lower() in month.lower():
                month = str(key + 1)
                break
        year = groups[2]
        day = groups[0]
        
        return year+'-'+month+'-'+day
def es_time_sub(text):
    p = r'([0-9]{1,2}) de (\w+?) de ([0-9]{4})'
    m = re.match(p,text)
    groups = m.groups()
    if len(groups) >=3:
        month = groups[1]
        for key,en in enumerate(spanish_month):
            if en.lower() in month.lower():
                month = str(key + 1)
                break
        year = groups[2]
        day = groups[0]
        
        return year+'-'+month+'-'+day

def bn_time_sub(text):
    p = r'(.*) ([0-9]{1,2}) (\w+) ([0-9]{4}) (.*)'
    m = re.match(p,text)
    groups = m.groups()
    if len(groups) >=4:
        month = groups[2]
        for key,en in enumerate(en_month):
            if en.lower() in month.lower():
                month = str(key + 1)
                break
        year = groups[3]
        day = groups[1]
        
        return year+'-'+month+'-'+day

it_month = ['gen','feb','mar','apr','mag','giu','lug','ago','set','ott','nov','dic']

def it_time_sub(text):
    p = r'([0-9]{1,2})\xa0(\w+)\xa0([0-9]{4})'
    m = re.match(p,text)
    groups = m.groups()
    if len(groups) >=3:
        month = groups[1]
        for key,en in enumerate(it_month):
            if en.lower() in month.lower():
                month = str(key + 1)
                break
        year = groups[2]
        day = groups[0]
        #print year+'-'+month+'-'+day
        
        return year+'-'+month+'-'+day



def int_time_sub(text):
    print "text is",text
    p = r'([0-9]{1,2}) (\w+) ([0-9]{4})(.*)'
    m = re.match(p,text)
    groups = m.groups()
    if len(groups) >=3:
        day = groups[0]
        month = groups[1]
        year = groups[2]
        return year+'-'+month+'-'+day


configure = {

    ##############################################
    # 世界卫生组织
    ###############################################
    ## 世界卫生组织 en
    "int":{
        'allowed_domains': ['who.int'],
        'site_url': 'http://www.who.int',
        'start_urls': [
            'http://who.int/mediacentre/news/en/',
            'http://who.int/publications/en/',
            'http://who.int/publications/journals/en/',
            'http://who.int/topics/en/'
        ],
        'language':'en',
        'listRules':[
            {
                'rule':r'(.*)/mediacentre/news/releases/(previous/)?en(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/mediacentre/news/releases/[0-9]+/(.*)/en(.*)',
                        'content':r'//*[@id="primary"]',
                        'title':r'//*[@id="primary"]/*[contains(@class,"headline")]',
                        'publish':[
                            {
                                'rule':r'//*[@id="primary"]//*[contains(@class,"dateline")]/text()',
                                'format':'%Y-%B-%d',
                                'extra':int_time_sub,
                            },
                            {
                                'rule':r'//*[@id="primary"]//*[contains(@class,"meta")]/p/text()',
                                'format':'%d %B %Y',
                                
                            }
                        ]

                    }
                ]
            },
            {
                'rule':r'(.*)/mediacentre/news/statements/(previous/)?en(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/mediacentre/news/statements/[0-9]+/(.*)/en(.*)',
                        'content':r'//*[@id="primary"]',
                        'title':r'//*[@id="primary"]/*[contains(@class,"headline")]',
                        'publish':[
                            {
                                'rule':r'//*[@id="primary"]//*[contains(@class,"dateline")]/text()',
                                'format':'%Y-%B-%d',
                                'extra':int_time_sub,
                            },
                            {
                                'rule':r'//*[@id="primary"]//*[contains(@class,"meta")]/p/text()',
                                'format':'%d %B %Y',
                                
                            }
                        ]

                    }
                ]
            },
            {
                'rule':r'(.*)/mediacentre/news/notes/(previous/)?en(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/mediacentre/news/notes/[0-9]+/(.*)/en(.*)',
                        'content':r'//*[@id="primary"]',
                        'title':r'//*[@id="primary"]/*[contains(@class,"headline")]',
                        'publish':[
                            {
                                'rule':r'//*[@id="primary"]//*[contains(@class,"dateline")]/text()',
                                'format':'%Y-%B-%d',
                                'extra':int_time_sub,
                            },
                            {
                                'rule':r'//*[@id="primary"]//*[contains(@class,"meta")]/p/text()',
                                'format':'%d %B %Y',
                                
                            }
                        ]

                    }
                ]
            },
            {
                'rule':r'(.*)/mediacentre/commentaries/([0-9]+/)?en(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/mediacentre/commentaries/[0-9]+/(.*)/en(.*)',
                        'content':r'//*[@id="primary"]',
                        'title':r'//*[@id="primary"]/*[contains(@class,"headline")]',
                        'publish':[
                            {
                                'rule':r'//*[@id="primary"]//*[contains(@class,"dateline")]/text()',
                                'format':'%Y-%B-%d',
                                'extra':int_time_sub,
                            },
                            {
                                'rule':r'//*[@id="primary"]//*[contains(@class,"meta")]/p/text()',
                                'format':'%d %B %Y',
                                
                            }
                        ]

                    }
                ]
            },

            {
                'rule':r'(.*)/publications/en/',
                'detailRules':[
                    {
                        'rule':r'(.*)/mediacentre/news/notes/[0-9]+/(.*)/en(.*)',
                        'content':r'//*[@id="primary"]',
                        'title':r'//*[@id="primary"]/*[contains(@class,"headline")]',
                        'publish':[
                            {
                                'rule':r'//*[@id="primary"]//*[contains(@class,"dateline")]/text()',
                                'format':'%Y-%B-%d',
                                'extra':int_time_sub,
                            },
                            {
                                'rule':r'//*[@id="primary"]//*[contains(@class,"meta")]/p/text()',
                                'format':'%d %B %Y',
                                
                            }
                        ]

                    }
                ]
            },
            {
                'rule':r'(.*)/topics/en(.*)',
                'detailRules':[],
            },
            # {
            #     'rule':r'(.*)/topics/(.*)/en/(.*)',
            #     'detailRules':[
            #         {
            #             'rule':r'(.*)/mediacentre/news/notes/[0-9]+/(.*)/en(.*)',
            #             'content':r'//*[@id="primary"]',
            #             'title':r'//*[@id="primary"]/*[contains(@class,"headline")]',
            #             'publish':[
            #                 {
            #                     'rule':r'//*[@id="primary"]//*[contains(@class,"dateline")]/text()',
            #                     'format':'%Y-%B-%d',
            #                     'extra':int_time_sub,
            #                 },
            #                 {
            #                     'rule':r'//*[@id="primary"]//*[contains(@class,"meta")]/p/text()',
            #                     'format':'%d %B %Y',
                                
            #                 }
            #             ]

            #         }
            #     ]
            # },





        ]


    },




   
    ##############################################
    # 亚洲
    ###############################################

    ## 中国 需要执行js
    "cn": {
        'allowed_domains':['moh.gov.cn'],
        'site_url':'http://www.moh.gov.cn',
        'start_urls':[
                'http://www.moh.gov.cn/zhuz/index.shtml',
                'http://www.moh.gov.cn/zhuz/mtbd/list.shtml',
                'http://www.moh.gov.cn/zhuz/xwfb/list.shtml',

                'http://www.moh.gov.cn/zwgk/index.shtml',
                'http://www.moh.gov.cn/zwgk/yqbb3/ejlist.shtml',
                'http://www.moh.gov.cn/zwgk/spaq/spaq_ejlist.shtml',
                'http://www.moh.gov.cn/zwgk/ylwsfw/spaq_ejlist.shtml',
                'http://www.moh.gov.cn/zwgk/jdjd/ejlist.shtml',
                'http://www.moh.gov.cn/zwgk/tjxx1/ejflist.shtml',
        ],
        'rules':[
                r'(.*)/zhuz/mtbd/(.*)',
                r'(.*)/zhuz/xwfb/(.*)',

                r'(.*)zwgk/yqbb3/(.*)',
                r'(.*)/zwgk/spaq(.*)',
                r'(.*)/zwgk/ylwsfw(.*)',
                r'(.*)/zwgk/lcl/(.*)',
                r'(.*)/zwgk/jdjd(.*)',
                r'(.*)/zwgk/tjxx1(.*)',
                r'(.*)/zwgk/(.*)',

                r'(.*)/jkj/(.*)',
                r'(.*)/sps/(.*)',
                r'(.*)/mohwsbwstjxxzx(.*)',
                

        ],
        'language':'zh-cn',
        'publish':[
            {
                'rule':"//div[@class='list']/div[@class='source']/span/text()",
                'format':'发布时间： %Y-%m-%d'
            }
        ],
        'listRules':[
            ## 新闻发布
            {
                'rule':r'(.*)/zhuz/xwfb/list(_[0-9]+)?\.shtml(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/zhuz/xwfb/(.*)',
                        'content':r'//*[@id="xw_box"]',
                        'title':r'//div[contains(@class,"list")]/div[contains(@class,"tit")]',
                        'publish':[
                            {
                                'rule':"//div[@class='list']/div[@class='source']/span/text()",
                                'format':'发布时间： %Y-%m-%d'
                            }
                        ],
                    }
                ]
            },
            ## 媒体报道
            {
                'rule':r'(.*)/zhuz/mtbd/list(_[0-9]+)?\.shtml(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/zhuz/mtbd/(.*)',
                        'content':r'//*[@id="xw_box"]',
                        'title':r'//div[contains(@class,"list")]/div[contains(@class,"tit")]',
                        'publish':[
                            {
                                'rule':"//div[@class='list']/div[@class='source']/span/text()",
                                'format':'发布时间： %Y-%m-%d'
                            }
                        ],
                    }
                ]
            },
            ## 疫情播报
            {
                'rule':r'(.*)/zwgk/yqbb3/elist(_[0-9]+)?\.shtml(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/zwgk/yqbb3/(.*)',
                        'content':r'//*[@id="xw_box"]',
                        'title':r'//div[contains(@class,"list")]/div[contains(@class,"tit")]',
                        'publish':[
                            {
                                'rule':"//div[@class='list']/div[@class='source']/span/text()",
                                'format':'发布时间： %Y-%m-%d'
                            }
                        ],
                    }
                ]
            },
            ## 食品安全
            {
                'rule':r'(.*)/zwgk/spaq/spaq_elist(_[0-9]+)?\.shtml(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/sps/(.*)',
                        'content':r'//*[@id="xw_box"]',
                        'title':r'//div[contains(@class,"list")]/div[contains(@class,"tit")]',
                        'publish':[
                            {
                                'rule':"//div[@class='list']/div[@class='source']/span/text()",
                                'format':'发布时间： %Y-%m-%d'
                            }
                        ],
                    }
                ]
            },
            ## 医疗卫生服务
            {
                'rule':r'(.*)/zwgk/ylwsfw/spaq_elist(_[0-9]+)?\.shtml(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/jkj/(.*)',
                        'content':r'//*[@id="xw_box"]',
                        'title':r'//div[contains(@class,"list")]/div[contains(@class,"tit")]',
                        'publish':[
                            {
                                'rule':"//div[@class='list']/div[@class='source']/span/text()",
                                'format':'发布时间： %Y-%m-%d'
                            }
                        ],
                    }
                ]
            },
            ## 统计信息
            {
                'rule':r'(.*)/zwgk/tjxx1/ejflist(_[0-9]+)?\.shtml(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/mohwsbwstjxxzx/(.*)',
                        'content':r'//*[@id="xw_box"]',
                        'title':r'//div[contains(@class,"list")]/div[contains(@class,"tit")]',
                        'publish':[
                            {
                                'rule':"//div[@class='list']/div[@class='source']/span/text()",
                                'format':'发布时间： %Y-%m-%d'
                            }
                        ],
                    }
                ]
            },
            ## 解读
            {
                'rule':r'(.*)/zwgk/jdjd/ejlist(_[0-9]+)?\.shtml(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/zwgk/jdjd/(.*)',
                        'content':r'//*[@id="xw_box"]',
                        'title':r'//div[contains(@class,"list")]/div[contains(@class,"tit")]',
                        'publish':[
                            {
                                'rule':"//div[@class='list']/div[@class='source']/span/text()",
                                'format':'发布时间： %Y-%m-%d'
                            }
                        ],
                    }
                ]
            },   
        ]
    },

    # 蒙古 网址打开后不是蒙古卫生部
    'mn':{
        'allowed_domains':['moh.mn'],
        'site_url':'http://www.moh.mn'
    },

    # 韩国 通过 asia 已更新
    "kr": {
        'allowed_domains': ['mohw.go.kr'],
        'site_url': 'http://www.mohw.go.kr',
        'start_urls': [
            'http://www.mohw.go.kr',
            'http://www.mohw.go.kr/eng/sg/ssg0111ls.jsp?PAR_MENU_ID=1001&MENU_ID=100111&page=1'
        ],
        'rules': [r'(.*)ssg0111vw\.jsp(.*)', r'(.*)ssg0111ls\.jsp(.*)'],
        
        'publish':[
            {
                "rule":'//*[@id="contents"]//table[contains(@class,"view")]/tbody/tr[2]/td[1]/text()',
                "format":"%Y-%m-%d"
            }
        ],
        'listRules':[
            {
                'rule':r'(.*)ssg0111ls\.jsp(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)ssg0111vw\.jsp(.*)',
                        'content':r'//*[@id="contents"]/div[2]/form',
                        'title':r'//*[@id="contents"]/div[2]/form/table/tbody/tr[1]/td',
                        'publish':[
                            {
                                "rule":'//*[@id="contents"]//table[contains(@class,"view")]/tbody/tr[2]/td[1]/text()',
                                "format":"%Y-%m-%d"
                            }
                        ]
                    }
                ]
            }
        ],

    },

    # 日本 切换到英文版网站 asia 已更新
    'jp':{
        'allowed_domains':['mhlw.go.jp'],
        'site_url':'http://www.mhlw.go.jp',
        'start_urls':[
            'http://www.mhlw.go.jp/english/index.html',
            'http://www.mhlw.go.jp/english/database',
            'http://www.mhlw.go.jp/english/new-info/index.html',

        ],
        'rules':[
            r'(.*)english/topics(.*)',
            r'(.*)english/policy(.*)',
            r'(.*)/english/database(.*)',
            r'(.*)/english/wp(.*)',
        ],
        'publish':[
            {
                'rule':'//*[@id="main-content"]/div[1]/p[1]/text()',
                'format':'Updated on %d %B %Y',
            }          
        ],
        'excludes':[
            r'(.*)/english/topics/2011eq(.*)',
        ],

        'listRules':[
            ## database
            {
                'rule':r'(.*)/english/database/(.*)',
                'detailRules':[],
            },
            ## news
            {
                'rule':r'(.*)/english/new-info/(.*)\.html',
                'detailRules':[],
            },

            {
                'rule':r'(.*)/english/topics/(.*)/index\.html(.*)',
                'detailRules':[
                ],
            },
            {
                'rule':r'(.*)/english/policy(.*)',
                'detailRules':[
                ],
            },
            {
                'rule':r'(.*)/english/wp(.*)',
                'detailRules':[
                ],
            },

        ]
    },

    # 朝鲜 没有网址

    # 越南 需要翻墙 asia 已更新
    'vn':{
        'allowed_domains':['moh.gov.vn'],
        'site_url':'http://moh.gov.vn',
        'language':'vi',
        'start_urls':[
            'http://moh.gov.vn',
            'http://moh.gov.vn/News/Pages/TinHoatDongV2.aspx',
            'http://emoh.moh.gov.vn/publish/home',
            'http://moh.gov.vn/province/Pages/ThongKeYTe.aspx',
        ],
        'rules':[
            r'(.*)/news/Pages/(.*)',
            r'(.*)/News/Pages/(.*)',
            r'(.*)/publish/home(.*)',
            r'(.*)/province/Pages(.*)',
        ],
        'publish':[
            {
                'rule':'//*[@id="toPrint"]/p[contains(@class,"n-date")]/text()',
                'format':'%d/%m/%Y %H:%M'
            }
        ],
        'listRules':[
            {
                'rule':r'(.*)/[nN]ews/Pages/[^\?]+(\?Pageg(.*)=[0-9]+)?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/[nN]ews/Pages/(.*)\?ItemID=(.*)',
                        'content':r'//*[@id="toPrint"]',
                        'title':r'//*[@id="toPrint"]/h2/font/font',
                        'publish':[
                            {
                                'rule':'//*[@id="toPrint"]/p[contains(@class,"n-date")]/text()',
                                'format':'%d/%m/%Y %H:%M'
                            }
                        ],

                        
                    }
                ]

            },
            {
                'rule':r'(.*)/province/Pages/[^\?]+(\?Pageg(.*)=[0-9]+)?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/province/Pages/(.*)\?ItemID=(.*)',
                        'content':r'//*[@id="toPrint"]',
                        'title':r'//*[@id="toPrint"]/h2/font/font',
                        'publish':[
                            {
                                'rule':'//*[@id="toPrint"]/p[contains(@class,"n-date")]/text()',
                                'format':'%d/%m/%Y %H:%M'
                            }
                        ],

                        
                    }
                ]

            },

           
            
        ]
    },

    # 老挝 通过 asia 已更新
    'la':{
        'allowed_domains':['moh.gov.la'],
        'site_url':'https://www.moh.gov.la',
        'start_urls':[
            'https://www.moh.gov.la/index.php/lo-la',
        ],
        'rules':[
            r'(.*)/images/pdf/Reporting/(.*)',
            r'(.*)/index\.php/lo-la/(.*)'
        ],
        'language':'lo',
        'publish':[],
        'listRules':[
            {
                'rule':'(.*)/index\.php/lo-la/[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}/[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}(\?start=[0-9]+(.*))?$',
                'detailRules':[
                    {
                        'rule':'(.*)/index\.php/lo-la/[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}/[0-9]{4}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}-[0-9]{2}/(.*)',
                        'content':r'//*[@id="ju-maincol"]',
                        'title':r'//*[@id="inner_content"]//article/header/h1[2]',
                        'publish':[],
                    }
                ] 
            }

        ]
    },

    # 柬埔寨 网站建设中
    'kh':{
        'allowed_domains':['moh.gov.kh'],
        'site_url':'http://moh.gov.kh'
    },

    # 缅甸 news 和 publication 都是通过js加载 已更新 en
    'mm':{
        'allowed_domains':['mohs.gov.mm'],
        'site_url':'http://mohs.gov.mm',
        'start_urls':[
            'http://mohs.gov.mm',
            'http://mohs.gov.mm/Main/content/new/list?pagenumber=1&pagesize=9',
            'http://mohs.gov.mm/Main/content/annouancement/list?pagenumber=1&pagesize=9',
            'http://mohs.gov.mm/Main/content/publication/list?pagenumber=1&pagesize=9',

        ],
        'language':'my',
        'rules':[
            r'(.*)/Main/content/new/(.*)',
            r'(.*)/Main/content/annouancement/(.*)',
            r'(.*)/Main/content/publication(.*)',
        ],
        'publish':[
                {
                    'rule':"//div[contains(@class,'single-post-info')]/span[contains(@class,'last-modified pull-right')]/text()",
                    'format':'Last modified on %A, %d %b %y'
                }
        ],
        'listRules':[
            {
                'rule':r'(.*)/Main/content/new/list\?pagenumber=[0-9]+&pagesize=[0-9]+(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/Main/content/new/(.*)',
                        'content':r'//*[@id="wrapper"]//div[contains(@class,"single-blog-text-area")]',
                        'title':r'//*[@id="wrapper"]//div[contains(@class,"single-blog-text-area")]/h2',
                        'publish':[
                                {
                                    'rule':"//div[contains(@class,'single-post-info')]/span[contains(@class,'last-modified pull-right')]/text()",
                                    'format':'Last modified on %A, %d %b %y'
                                }
                        ],

                    }
                ]
            },
            {
                'rule':r'(.*)/Main/content/annouancement/list\?pagenumber=[0-9]+&pagesize=[0-9]+(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/Main/content/annouancement/(.*)',
                        'content':r'//*[@id="wrapper"]//div[contains(@class,"single-blog-text-area")]',
                        'title':r'//*[@id="wrapper"]//div[contains(@class,"single-blog-text-area")]/h2',
                        'publish':[
                                {
                                    'rule':"//div[contains(@class,'single-post-info')]/span[contains(@class,'last-modified pull-right')]/text()",
                                    'format':'Last modified on %A, %d %b %y'
                                }
                        ],

                    }
                ]
            },
            {
                'rule':r'(.*)/Main/content/publication(.*)',
                'detailRules':[
                ]
            }
        ]


    },
    
    # 泰国 需要翻墙 asia 已更新
    'th':{
        'allowed_domains':['moph.go.th'],
        'site_url':'https://www.moph.go.th',
        'start_urls':[
            'https://ops.moph.go.th/public/index.php/news/public_relations',
            'https://ops.moph.go.th/public/index.php/policy_plan',
            'https://ops.moph.go.th/public/index.php/downloads',

        ],
        'rules':[
            r'(.*)/public/index\.php/news/read/(.*)',
            r'(.*)/public/index\.php/news/public_relations(.*)',
            r'(.*)/public/index\.php/downloads(.*)',

        ],
        'publish':[
            {
                'rule':'//*[@id="mainview"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div[2]/text()',
                'format':'%d %b %Y'
            }
        ],
        'listRules':[
            {
                'rule':r'(.*)/public/index\.php/news/public_relations(\?&per_page=[0-9]+)?(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/public/index\.php/news/read/(.*)',
                        'content':r'//*[@id="mainview"]',
                        'title':r'//*[@id="mainview"]/div/div[2]/div[1]/h1/font/font',
                        'publish':[
                            {
                                'rule':'//*[@id="mainview"]/div/div[2]/div[2]/div/div/div[2]/div[3]/div[2]/text()',
                                'format':'%d %b %Y'
                            }
                        ],

                    }
                ]
            },
        ]
    },

    # 菲律宾 翻墙 通过 en 已更新
    'ph':{
        'allowed_domains':['doh.gov.ph'],
        'site_url':'http://www.doh.gov.ph',
        'start_urls':[
            'http://www.doh.gov.ph/news-clips',
            'http://www.doh.gov.ph/press-releases',
            'http://www.doh.gov.ph/national-objectives-health',

        ],
        'rules':[
            r'(.*)/sites/default/files/news_clips/(.*)',
            r'(.*)/node(.*)',

        ],
        'publish':[
            {
                'rule':'//*[@id="content"]//article/div[2]/div/div/p[1]/em/text()',
                'format':'Press Release/ %B %d, %Y'
            }
        ],
        'listRules':[
            {
                'rule':r'(.*)/news-clips(.*)',
                'detailRules':[
                   
                ]
            },
            {
                'rule':r'(.*)/press-releases(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/node/(.*)',
                        'content':r'//*[@id="content"]',
                        'title':r'//*[@id="page-title"]',
                        'publish':[
                            {
                                'rule':'//*[@id="content"]//article/div[2]/div/div/p[1]/em/text()',
                                'format':'Press Release/ %B %d, %Y'
                            }
                        ],

                    }

                   
                ]
            }
        ]
    },

    # 马来西亚 通过 en 已更新
    'my':{
        'allowed_domains':['moh.gov.my'],
        'site_url':'http://www.moh.gov.my',
        'start_urls':[
            'http://www.moh.gov.my/index.php'
        ],
        'rules':[
            r'(.*)/index\.php/database_stores/store_view_page/(.*)',
            r'(.*)index\.php/pages/view(.*)',
        ],
        'publish':[
            {
                'rule':'//*[@id="container_content"]//*[contains(@class,"dataTableDetail")]/tbody/tr[3]/td/text()',
                'format':'%d-%m-%Y %H:%M:%S'
            }
        ],
        'listRules':[
            {
                'rule':r'(.*)/index\.php/database_stores/store_view_page/[0-9]+$',
                'detailRules':[
                    {
                        'rule':r'(.*)/index\.php/database_stores/store_view_page/[0-9]+/[0-9]+(.*)',
                        'content':r'//*[@id="container_content"]',
                        'title':None,
                        'publish':[
                            {
                                'rule':'//*[@id="container_content"]//*[contains(@class,"dataTableDetail")]/tbody/tr[3]/td/text()',
                                'format':'%d-%m-%Y %H:%M:%S'      
                            }
                        ]
                    }
                ]
            },
            {
                'rule':r'(.*)/index\.php/pages/view(.*)',
                'detailRules':[
                ]
            }
        ]
    },
    # 印度尼西亚 通过 en 已更新
    'id':{
        'allowed_domains':['depkes.go.id'],
        'site_url':'http://www.depkes.go.id',
        'start_urls':['http://www.depkes.go.id/folder/view/01/structure-info-terkini.html'],
        'rules':[
            r'(.*)/article/view/[0-9]{11}/(.*)',
            r'(.*)/folder/view/01(.*)',
        ],
        'language':'en-id',
        'publish':[
            
            {
                'rule':'//*[@id="vbMainLayer"]/div[7]/ul/li/span/text()',
                'format':'%Y-%m-%d',
                'extra':id_time_sub
            }
        ],
        'listRules':[
            {
                'rule':r'(.*)/folder/view/01(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/article/view/[0-9]{11}/(.*)',
                        'content':r'//*[@id="vbMainLayer"]//*[contains(@class,"ants-news-content")]',
                        'title':r'//*[@id="vbMainLayer"]//*[contains(@class,"title")]',
                        'publish':[
                            {
                                'rule':'//*[@id="vbMainLayer"]//span[contains(@class,"date")]/text()',
                                'format':'%Y-%m-%d',
                                'extra':id_time_sub
                            }
                        ],
                    }
                ]
            }
        ]

    },


    # 新加坡 item通过js添加 en 已更新
    'sg':{
        'allowed_domains':['moh.gov.sg'],
        'site_url':'https://www.moh.gov.sg',
        'start_urls':[
                        'https://www.moh.gov.sg/content/moh_web/home.html',
                        'https://www.moh.gov.sg/content/moh_web/home/diseases_and_conditions.html',
                        'https://www.moh.gov.sg/content/moh_web/home/pressRoom.html',
                        'https://www.moh.gov.sg/content/moh_web/home/Publications.html',
                        'https://www.moh.gov.sg/content/moh_web/home/legislation.html',
                    ],
        'rules': [
            r'(.*)/content/moh_web/home/pressRoom/(.*)',
            r'(.*)/content/moh_web/home/diseases_and_conditions/(.*)',
            r'(.*)content/moh_web/home/Publications(.*)',
            r'(.*)/content/moh_web/home/statistics(.*)',
            r'(.*)/content/moh_web/home/legislation(.*)',

        ],
        'publish':[
            {
                'rule':'//*[@id="content"]/div[2]/div/div[4]/div/div/p',
                'format':'Last updated on %d %b %Y',
            },
        ],
        'listRules':[
            {
                'rule':r'(.*)/content/moh_web/home/pressRoom\.html(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/content/moh_web/home/pressRoom/(.*)',
                        'content':r'//*[@id="content"]//*[contains(@class,"entry-content")]',
                        'title':r'//*[@id="content"]//*[contains(@class,"article")]//*[contains(@class,"header")]/h1',
                        'publish':[
                            {
                                'rule':'//*[@id="content"]//*[contains(@class,"dates-edit")]/text()',
                                'format':'Last updated on %d %b %Y',
                            },
                        ],
                    }
                ]
            },
            {
                'rule':r'(.*)/content/moh_web/home/diseases_and_conditions\.html(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/content/moh_web/home/diseases_and_conditions/(.*)',
                        'content':r'//*[@id="content"]//*[contains(@class,"entry-content")]',
                        'title':r'//*[@id="content"]//*[contains(@class,"article")]//*[contains(@class,"header")]/h1',
                        'publish':[
                            {
                                'rule':'//*[@id="content"]//*[contains(@class,"dates-edit")]/text()',
                                'format':'Last updated on %d %b %Y',
                            },
                        ],
                    }
                ]
            },
            {
                'rule':r'(.*)/content/moh_web/home/Publications(.*)',
                'detailRules':[
                ]
            },
            {
                'rule':r'(.*)/content/moh_web/home/legislation(.*)',
                'detailRules':[
                ]
            },
        ]
    },

    # 文莱 en 已更新
    'bn':{
        'allowed_domains':['moh.gov.bn'],
        'site_url':'http://www.moh.gov.bn',
        'start_urls':[
            'http://www.moh.gov.bn/SitePages/Latest%20News.aspx',
            'http://www.moh.gov.bn/SitePages/healthlineonline.aspx',

        ],
        'rules':[
            r'(.*)/Lists/Latest%20news/NewDispForm\.aspx\?ID=(.*)',
        ],
        'listRules':[
            {
                'rule':r'(.*)SitePages/Latest%20News\.aspx(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/Lists/Latest%20news/NewDispForm\.aspx\?ID=(.*)',
                        'content':r'//*[@id="WebPartWPQ12"]',
                        'title':r'//*[@id="WebPartWPQ12"]/table/tbody/tr[3]/td/table/tbody/tr[1]/td/h2',
                        'publish':[
                            {
                                'rule':'//*[@id="WebPartWPQ12"]/table/tbody/tr[3]/td/table/tbody/tr[2]/td/div/p[14]/text()',
                                'extra':bn_time_sub,
                                'format':'%Y-%m-%d'
                            },
                            {
                                'rule':'//*[@id="WebPartWPQ12"]/table/tbody/tr[3]/td/table/tbody/tr[2]/td/div/p[35]/text()[2]',
                                'extra':bn_time_sub,
                                'format':'%Y-%m-%d'
                            },

                           
                        ]
                    }
                ]
            }
        ]
    },

    # 东帝汶 en 通过 网站维护
    'tl':{
        'allowed_domains':['moh.gov.tl'],
        'site_url':'http://www.moh.gov.tl',
        'start_urls':[
            'http://www.moh.gov.tl/?q=blog/1',
            'http://www.moh.gov.tl/?q=report'
        ],
        'rules':[
            r'(.*)/\?q=node/(.*)',
            r'(.*)/\?q=blog/1&page(.*)',
            r'(.*)/\?q=report&page(.*)'
        ],
        'publish':[
            {
                
                'rule':"//article//p[contains(@class,'submitted')]/span/text()",
                'format':'%a, %d/%m/%Y - %H:%M'
            }
        ],
        'listRules':[
            {
                'rule':'',
                'detailRules':[
                    {
                        'rule':'',
                        'content':'',
                        'title':'',
                        'publish':[
                            {
                                
                                'rule':"//article//p[contains(@class,'submitted')]/span/text()",
                                'format':'%a, %d/%m/%Y - %H:%M'
                            }
                        ],
                    }
                ]
            }
        ]
    },

    # 尼泊尔 网页打不开
    'np':{
        'allowed_domains':['moh.gov.np'],
        'site_url':'http://moh.gov.np'
    },
    
    # 不丹 en 通过 文件过多 已更新
    'bt':{
        'allowed_domains':['health.gov.bt'],
        'site_url':'http://www.health.gov.bt',
        'start_urls':['http://www.health.gov.bt/category/news/','http://www.health.gov.bt/publications/'],
        'rules':[
           r'(.*)'
        ],
        'publish':[
            {
                'rule':"//time[contains(@class,'entry-date published updated')]/text()",'format':'%B %d, %Y'
            }
        ],
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
        ],
        'listRules':[
            {
                'rule':r'(.*)/category/news(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)',
                        'content':r'//*[@id="content"]',
                        'title':r'//*[@id="content"]/article//*[contains(@class,"entry-title")]',
                         'publish':[
                            {
                                'rule':"//time[contains(@class,'entry-date published updated')]/text()",'format':'%B %d, %Y'
                            }
                        ],
                    }
                ]
            },
            {
                'rule':r'(.*)/publications(.*)',
                'detailRules':[
                ]
            }
        ]
        
    },

    # 印度 en 通过 样式有点问题 已更新
    'in':{
        'allowed_domains':['mofpi.nic.in'],
        'site_url':'http://www.mofpi.nic.in',
        'start_urls':[
            'http://www.mofpi.nic.in/press-release',
            'http://www.mofpi.nic.in/documents/reports/annual-report',
            'http://www.mofpi.nic.in/documents/reports/technical-reports',
            'http://www.mofpi.nic.in/documents/reports/nsso-reports',
        ],
        'rules':[r'(.*)/sites/default/files/(.*)'],
        'listRules':[
            {
                'rule':r'(.*)(press-release|documents)(.*)',
                'detailRules':[
                ]
            }
        ]
    },

    # 巴基斯坦 en 通过 已更新
    'pk':{
        'allowed_domains':['nhsrc.gov.pk'],
        'site_url':'http://www.nhsrc.gov.pk',
        'start_urls':[
            'http://www.nhsrc.gov.pk',
            'http://www.nhsrc.gov.pk/press_releases.html',

        ],
        'rules':[
            r'(.*)/press_release(.*)'
            r'(.*)/news_details(.*)'
        ],
        'publish':[
            {
                'rule':'//*[@id="right-header-datetime"]/text()',
                'format':'%B %d, %Y'
            }
        ],
        'listRules':[
            {
                'rule':r'(.*)/press_releases\.html(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)press_release_detailes(.*)',
                        'content':r'//*[@id="right-content-body"]',
                        'title':r'//*[@id="right-header-text"]',
                        'publish':[
                            {
                                'rule':'//*[@id="right-header-datetime"]/text()',
                                'format':'%B %d, %Y'
                            }
                        ],
                    }
                ]
            }
        ]
    },

    # 孟加拉国 en 通过 已更新
    'bd':{
        'allowed_domains':['mohfw.gov.bd'],
        'site_url':'http://www.mohfw.gov.bd',
        'start_urls':[
            'http://www.mohfw.gov.bd/index.php?option=com_content&view=frontpage&Itemid=1&lang=en'
        ],
        'rules':[
            r'(.*)/index.php\?option=com_content&view=article&id=(.*)',
        ],
        'listRules':[
            {
                'rule':r'index\.php\?option=com_content&view=frontpage(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/index.php\?option=com_content&view=article&id=(.*)',
                        'content':r'//*[@id="wrapper"]//*[contains(@class,"innercontent")]',
                        'title':r'//*[@id="wrapper"]//*[contains(@class,"contentheading")]',
                        'publish':[]
                    }
                ]
            }
        ]
    },

    # 斯里兰卡 en 通过 已更新
    'lk':{
        'allowed_domains':['health.gov.lk'],
        'site_url':'http://www.health.gov.lk',
        'start_urls':[
            'http://www.health.gov.lk/moh_final/english/others.php?pid=110',
            'http://www.health.gov.lk/moh_final/english/others.php?pid=127',
            'http://www.health.gov.lk/moh_final/english/heath_alert.php',
            'http://www.health.gov.lk/moh_final/english/gazzete_notification.php?spid=53',
            'http://www.health.gov.lk/moh_final/english/general_notice.php?spid=33'
        ],
        'rules':[
            r'(.*)/moh_final/english/public/elfinder/files/publications/AHB/(.*)',
            r'(.*)/moh_final/english/others\.php\?pid=(.*)'
        ],
        'listRules':[
            {
                'rule':r'(.*)/moh_final/english(.*)',
                'detailRules':[]
            }
        ]
    },

    # 马尔代夫 en 通过 已更新
    'mv':{
        'allowed_domains':['health.gov.mv'],
        'site_url':'http://www.health.gov.mv',
        'start_urls':['http://www.health.gov.mv/News'],
        'rules':[
            r'(.*)/News/(.*)'
        ],
        'publish':[
            {
                'rule':'//*[@id="content"]//time[contains(@itemprop,"datePublished")]/@datetime',
                'format':'%Y-%m-%d'
            }
        ],
        'listRules':[
            {
                'rule':r'(.*)/News([^0-9]*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/News/[0-9]+(.*)',
                        'content':r'//*[@id="content"]/*[contains(@class,"news-body")]',
                        'title':r'//*[@id="content"]//*[contains(@itemprop,"headline")]',
                        'publish':[
                            {
                                'rule':'//*[@id="content"]//time[contains(@itemprop,"datePublished")]/@datetime',
                                'format':'%Y-%m-%d'
                            }
                        ],
                    }
                ]

            }
        ]
    },


    # 伊朗 ar 新闻太多 编码问题 通过 已更新
    'ir':{
        'allowed_domains':['behdasht.gov.ir'],
        'site_url':'http://www.behdasht.gov.ir',
        'start_urls':[
            'http://www.behdasht.gov.ir/index.jsp?siteid=1&fkeyid=&siteid=1&pageid=1508'],
        'language':'ar',
        'rules':[
            r'(.*)/news/(.*)',
            r'(.*)/page/%DA%A9%D9%84\+%D8%A7%D8%AE%D8%A8%D8%A7%D8%B1\?page=(.*)',

        ],
        'listRules':[
            {
                'rule':r'(.*)/page/(.*)(\?page=(.*))?',
                'detailRules':[
                    {
                        'rule':r'(.*)/news/(.*)',
                        'content':r'//*[@id="PrintArea"]',
                        'title':r'//*[@id="PrintArea"]/div/div/div[1]/div/p[3]/span/span/span/span/span/span/span/strong',
                        #'title':None,
                        'publish':[],
                    }
                ]
            }
        ]
    },


    # 阿富汗 ar 已更新
    'af':{
        'allowed_domains':['moph.gov.af'],
        'site_url':'http://www.moph.gov.af/fa',
        'start_urls':[
            'http://moph.gov.af/fa/news',
            'http://moph.gov.af/fa/page/access-to-information/104408',
            'http://moph.gov.af/fa/page/access-to-information/monthly-report',
            'http://moph.gov.af/fa/page/585',
        ],
        'rules':[
            r'(.*)/fa/news/(.*)',
            r'(.*)/fa/Documents\?DID=(.*)'
        ],
        'language':'ar',
        'publish':[{'rule':"//div[contains(@class,'postDate')]/text()",'format':'%b %d, %Y'}],
        'listRules':[
            {
                'rule':r'(.*)/fa/news(\?page=[0-9]+)?',
                'detailRules':[
                    {
                        'rule':r'(.*)/fa/news/(.*)',
                        'content':r'//*[@id="dataBody"]//*[contains(@class,"content")]',
                        'title':r'//*[@id="dataBody"]//*[contains(@class,"heading")]',
                        'publish':[{'rule':"//div[contains(@class,'postDate')]/text()",'format':'%b %d, %Y'}],
                    }
                ]
            },
            {
                'rule':r'(.*)/fa/Documents\?DID=(.*)',
                'detailRules':[
                ]
            },
            {
                'rule':r'(.*)/fa/Documents\?page=[0-9]+&did=[0-9]+(.*)',
                'detailRules':[
                ]
            },
        ]

    },

    # 沙特阿拉伯 js加载 en/ar 已更新
    'sa':{
        'allowed_domains':['moh.gov.sa'],
        'site_url':'http://www.moh.gov.sa',
        'start_urls':[
            'https://www.moh.gov.sa/en/Ministry/MediaCenter/News/Pages/default.aspx',
            'https://www.moh.gov.sa/en/Ministry/MediaCenter/Ads/Pages/default.aspx',
            'https://www.moh.gov.sa/en/Ministry/MediaCenter/Publications/Pages/default.aspx',


        ],
        'rules':[
            r'(.*)/en/Ministry/MediaCenter/News/Pages/(.*)',
            r'(.*)/en/Ministry/MediaCenter/Publications/Pages/(.*)',
            r'(.*)/en/Ministry/MediaCenter/Ads/Pages(.*)',
        ],
        'excludes':[
            r'(.*)en/_layouts/MOH/SSOLogin\.aspx(.*)'
        ],
        'language':'ar',
        'publish':[
            {
                'rule':'//*[@id="ctl00_PlaceHolderMain_ctl04_lblDate"]/text()',
                'format':'%d %B %Y'
            }
        ],
        'listRules':[
            {
                'rule':r'(.*)/en/Ministry/MediaCenter/News/Pages/default\.aspx(\?PageIndex=[0-9]+)?(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/en/Ministry/MediaCenter/News/Pages/news-(.*)',
                        'content':r'//*[@id="PageContent"]/div[contains(@class,"news_details")]',
                        'title':r'//*[@id="PageContent"]/div[contains(@class,"news_title2")]',
                        'publish':[
                            {
                                'rule':'//*[@id="ctl00_PlaceHolderMain_ctl04_lblDate"]/text()',
                                'format':'%d %B %Y'
                            }
                        ],
                    }
                ]
            },
            {
                'rule':r'(.*)/en/Ministry/MediaCenter/Ads/Pages/default\.aspx(\?PageIndex=[0-9]+)?(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/en/Ministry/MediaCenter/Ads/Pages/ads-(.*)',
                        'content':r'//*[@id="PageContent"]/div[contains(@class,"news_details")]',
                        'title':r'//*[@id="PageContent"]/div[contains(@class,"news_title2")]',
                        'publish':[
                            {
                                'rule':'//*[@id="ctl00_PlaceHolderMain_ctl05_lblDate"]/text()',
                                'format':'%d %B %Y'
                            }
                        ],
                    }
                ]
            },
            {
                'rule':r'(.*)en/Ministry/MediaCenter/Publications/Pages(.*)',
                'detailRules':[]
            }

        ]
    },
    # 也门 en 通过 已更新
    'ye':{
        'allowed_domains':['mophp-ye.org'],
        'site_url':'http://www.mophp-ye.org',
        'start_urls':[
            'http://www.mophp-ye.org/english/news.html',
            'http://www.mophp-ye.org/arabic/reports_statistical.html',
            'http://www.mophp-ye.org/english/magazine.html',
            'http://www.mophp-ye.org/english/data.html',
        ],
        'rules':[
            r'(.*)/english/news\.html(.*)'
        ],
        'publish':[
            {
                'rule':"//div[@id='content']/h4/text()",
                'format':'%B, %Y'
            }
        ],
        'listRules':[
            {
                'rule':r'(.*)/english/news\.html(.*)',
                'detailRules':[
                ]
            }
        ]
    },

    # 阿曼 en 通过 已更新
    'om':{
        'allowed_domains':['moh.gov.om'],
        'site_url':'http://www.moh.gov.om',
        'start_urls':[
            'https://www.moh.gov.om/en_US/ebola',
            'https://www.moh.gov.om/en_US/-50',
            'https://www.moh.gov.om/en/web/statistics/annual-reports',
            'https://www.moh.gov.om/en_US/news'
            
        ],
        'rules':[
            r'(.*)/documents/(.*)',
            r'(.*)/en/web/statistics/annual-reports(.*)',
            r'(.*)/en_US/web/statistics/annual-reports(.*)',
            r'(.*)/en_US/web/statistics(.*)',
            r'(.*)/en/web/statistics(.*)',
        ],
        'listRules':[
            {
                'rule':r'(.*)/en/web/statistics/annual-reports(.*)',
                'detailRules':[
                ]
            },
            {
                'rule':r'(.*)/en_US/web/statistics/annual-reports(.*)',
                'detailRules':[

                ]
            },
            {
                'rule':r'(.*)/en_US/web/statistics/(.*)',
                'detailRules':[

                ]
            },
            {
                'rule':r'(.*)/en/web/statistics/(.*)',
                'detailRules':[

                ]
            },
            {
                'rule':r'(.*)/(en_US|en)/news(\?(.*))?',
                'detailRules':[
                    {
                        'rule':r'(.*)/(en_US|en)/-/---(.*)',
                        'content':r'//*[contains(@class,"media-center-content")]',
                        'title':r'//*[contains(@class,"article-meta")]/h1',
                        'publish':[
                            {
                                'rule':'//*[contains(@class,"media-center-item")]//*[contains(@class,"date")]/text()',
                                'format':'%d/%m/%Y'
                            }
                            
                        ]

                    }
                    


                ]
            },
        ]
    },

    # 阿联酋  时间解析问题 ar 通过 已更新
    'ae':{
        'allowed_domains':['mohap.gov.ae'],
        'site_url':'http://www.mohap.gov.ae',
        'start_urls':[
                        'http://www.mohap.gov.ae/en/AwarenessCenter/Pages/posts.aspx',
                        'http://www.mohap.gov.ae/ar/Aboutus/Pages/PublicHealthPolicies.aspx',
                        'http://www.mohap.gov.ae/en/MediaCenter/Pages/news.aspx',
                        'http://www.mohap.gov.ae/en/MediaCenter/Pages/events.aspx',
                        'http://www.mohap.gov.ae/en/OpenData/Pages/default.aspx',
                        'http://www.mohap.gov.ae/en/OpenData/Pages/health-statistics.aspx',
                    ],
        'rules':[
                    r'(.*)/en/AwarenessCenter/Pages/post\.aspx(.*)',
                    r'(.*)/FlipBooks/PublicHealthPolicies/(.*)/mobile/index\.html(.*)',
                    r'(.*)/en/MediaCenter/Pages/news\.aspx(.*)',
                    r'(.*)/en/OpenData/Pages/default\.aspx(.*)',
                    r'(.*)/en/OpenData/Pages/health-statistics\.aspx(.*)',
                    r'(.*)/en/MediaCenter/Pages/EventDetail\.aspx(.*)',
                ],
        'language':'ar',
        'publish':[
                    {"rule":"//div[@class='newsdetailstitle']/p[@class='metadate']/span[2]/text()","format":"%d %b %Y"},
                    {"rule":"//div[@class='contentblock']/p[@class='metadata']/span[1]/text()","format":"%d %A, %B, %Y","extra":ae_time_sub},
                    {"rule":"//div[@class='newsdetailstitle']/p[@class='metadate']/span[2]/text()","format":"%d %B %Y"},
                    {"rule":"//p[@class='metadate']/span/text()","format":"Health and Care / Published in %d %A, %B, %Y "}
        ],
        'listRules':[
            {
                'rule':r'(.*)/en/MediaCenter/Pages/news\.aspx(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)en/MediaCenter/News/Pages/(.*)',
                        'content':r'//*[contains(@class,"newsdetailsp")]',
                        'title':r'//*[contains(@class,"newsdetailstitle")]/h2/span[@id]',
                        'publish':[
                            {"rule":"//div[@class='newsdetailstitle']/p[@class='metadate']/span[2]/text()","format":"%d %b %Y"},
                            {"rule":"//div[@class='contentblock']/p[@class='metadata']/span[1]/text()","format":"%d %A, %B, %Y","extra":ae_time_sub},
                            {"rule":"//div[@class='newsdetailstitle']/p[@class='metadate']/span[2]/text()","format":"%d %B %Y"},
                            {"rule":"//p[@class='metadate']/span/text()","format":"Health and Care / Published in %d %A, %B, %Y "}
                        ],

                    }
                ]
            },
            {
                'rule':r'(.*)/en/OpenData/Pages/default\.aspx(.*)',
                'detailRules':[
                ]
            },
            {
                'rule':r'(.*)/en/OpenData/Pages/health-statistics\.aspx(.*)',
                'detailRules':[
                ]
            },
            {
                'rule':r'(.*)/en/AwarenessCenter/Pages/post\.aspx([^\?]*)$',
                'detailRules':[
                    {
                        'rule':r'(.*)en/AwarenessCenter/Pages/post\.aspx\?PostID=(.*)',
                        'content':r'//*[contains(@class,"newsdetailsp")]',
                        'title':r'//*[contains(@class,"newsdetailstitle")]/h2/span[@id]',
                        'publish':[
                            {"rule":"//div[@class='newsdetailstitle']/p[@class='metadate']/span[2]/text()","format":"%d %b %Y"},
                            {"rule":"//div[@class='contentblock']/p[@class='metadata']/span[1]/text()","format":"%d %A, %B, %Y","extra":ae_time_sub},
                            {"rule":"//div[@class='newsdetailstitle']/p[@class='metadate']/span[2]/text()","format":"%d %B %Y"},
                            {"rule":"//p[@class='metadate']/span/text()","format":"Health and Care / Published in %d %A, %B, %Y "}
                        ],

                    }
                ]
            }
        ]
    },


    # 卡塔尔 en 通过 页面换了 已更新
    'qa':{
        'allowed_domains':['moph.gov.qa'],
        'site_url':'https://www.moph.gov.qa',
        'start_urls':[
                        'https://www.moph.gov.qa/news/Pages/News-Page-1.aspx',
                        'https://www.moph.gov.qa/events/events',
                        'https://www.moph.gov.qa/health-strategies/national-health-strategy'
                    ],
        'rules':[
                r'(.*)/news(.*)',
                r'(.*)/events(.*)',
                r'(.*)/health-strategies(.*)'
        ],
        'publish':[
            {
                "rule":"//header/div[@class='newsDetailsListContainer']/dl[@class='newsDetailsList']/dd[@class='pubDate']/abbr/text()",
                "format":"%d %B %Y"
            },

        ],
        'listRules':[
            {
                'rule':r'(.*)/news/Pages/(News-Page-(.*))|(default)\.aspx',
                'detailRules':[
                    {
                        'rule':r'(.*)/news/Pages/(.*)',
                        'content':r'//*[@id="wideCol"]//article[contains(@class,"newsDetails")]',
                        'title':r'//*[@id="wideCol"]/header/h2',
                        'publish':[
                            {
                                "rule":"//header/div[@class='newsDetailsListContainer']/dl[@class='newsDetailsList']/dd[@class='pubDate']/abbr/text()",
                                "format":"%d %B %Y"
                            },
                        ],
                    }
                ]
            }
        ]



    },

    # 巴林 ar 通过 已更新
    'bh':{
        'allowed_domains':['moh.gov.bh'],
        'site_url':'https://www.moh.gov.bh',
        'start_urls':[
            'https://www.moh.gov.bh/News',
            'https://www.moh.gov.bh/HealthInfo/Publications',
            'https://www.moh.gov.bh/HealthInfo/RecallsAndSafetyAlerts',
            'https://www.moh.gov.bh/HealthInfo/DiseasesAndConditions',
            'https://www.moh.gov.bh/HealthInfo/RecallsAndSafetyAlerts',
            'https://www.moh.gov.bh/Blog',


        ],
        'rules':[
            r'(.*)/News/Details/(.*)',
            r'(.*)/Blog/Article/Details/(.*)',
            r'(.*)HealthInfo/Publication(.*)',
            r'(.*)/HealthInfo/(SwineFlu|Alzheimer|SickleCell|HeartAttack)(.*)'
        ],
        'language':'ar',
        'publish':[
            {
                'rule':'//*[@id="renderbody"]/div[3]/text()',
                'format':'%Y-%m-%d %H:%M:%S',
                'extra':bh_time_sub

            }
        ],
        'listRules':[
            {
                'rule':r'(.*)News(\?Year=[0-9]{4}&Search=(.*))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/News/Details/(.*)',
                        'content':r'//*[@id="renderbody"]',
                        'title':r'//*[@id="renderbody"]//*[contains(@class,"heading_design")]',
                        'publish':[
                            {
                                'rule':r'//*[@id="renderbody"]/div[3]/text()',
                                'format':'%Y-%m-%d %H:%M:%S',
                                'extra':bh_time_sub

                            }
                        ],
                    }
                ]
            },
            {
                'rule':r'(.*)HealthInfo/Publication(.*)',
                'detailRules':[
                ]
            },
            {
                'rule':r'(.*)HealthInfo/RecallsAndSafetyAlerts(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/News/Details/(.*)',
                        'content':r'//*[@id="renderbody"]',
                        'title':r'//*[@id="renderbody"]//*[contains(@class,"heading_design")]',
                        'publish':[
                            {
                                'rule':'//*[@id="renderbody"]/div[3]/text()',
                                'format':'%Y-%m-%d %H:%M:%S',
                                'extra':bh_time_sub

                            }
                        ],
                    }
                ]
            },
            {
                'rule':r'(.*)/HealthInfo/(SwineFlu|Alzheimer|SickleCell|HeartAttack)(.*)',
                'detailRules':[
                ]
            },
            {
                'rule':r'(.*)/Blog(?!.*Details)',
                'detailRules':[
                    {
                        'rule':r'(.*)/Blog/Article/Details/(.*)',
                        'content':r'//*[@id="content"]',
                        'title':r'//*[@id="content"]/div/div[1]/article/div/div[2]/div[1]/h2',
                        'publish':[
                            {
                                'rule':'//*[@id="renderbody"]/div[3]/text()',
                                'format':'%Y-%m-%d %H:%M:%S',
                                'extra':bh_time_sub

                            }
                        ],
                    }
                ]
            },


        ]
    },

    # 科威特 网页打不开
    'kw':{
        'allowed_domains':['moh.gov.kw'],
        'site_url':'http://www.moh.gov.kw'
    },

    # 土耳其 asia 通过 已更新
    'tr':{
        'allowed_domains':['saglik.gov.tr'],
        'site_url':'http://www.saglik.gov.tr',
        'start_urls':[
            'http://www.saglik.gov.tr/EN,15463/news.html',
            'http://www.saglik.gov.tr/EN,15462/documents.html',
        ],
        'rules':[r'(.*)/EN,15(.*)'],
        'language':'tr',
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
        ],
        'listRules':[
            {
                'rule':r'(.*)EN,(.*)/news\.html',
                'detailRules':[
                    {
                        'rule':r'(.*)/EN,15(.*)',
                        'content':r'//*[@id="ctl00"]//*[contains(@class,"bbIcerik1")]',
                        'title':r'//*[@id="ctl00"]/div[4]/div[2]/div/div[3]/div[1]/h1',
                        'publish':[{'rule':r"//section[@class='date']/text()",'format':'UPDATED : %d/%m/%Y'}],

                    }
                ]
            }
        ]
    },

    # 叙利亚 en/ar 通过 维护中
    'sy':{
        'allowed_domains':['moh.gov.sy'],
        'site_url':'http://www.moh.gov.sy',
        'start_urls':[
            'http://www.moh.gov.sy/Default.aspx?tabid=259&language=en-US',
            'http://www.moh.gov.sy/Default.aspx?tabid=248&language=en-US',
            'http://www.moh.gov.sy/Default.aspx?tabid=249&language=en-US',
            'http://www.moh.gov.sy/Default.aspx?tabid=250&language=en-US',
            'http://www.moh.gov.sy/Default.aspx?tabid=251&language=en-US',
            'http://www.moh.gov.sy/Default.aspx?tabid=252&language=en-US',
            'http://www.moh.gov.sy/Default.aspx?tabid=253&language=en-US',
            'http://www.moh.gov.sy/Default.aspx?tabid=254&language=en-US',
            'http://www.moh.gov.sy/Default.aspx?tabid=350&language=ar-YE',

        ],
        'rules':[
                    r'(.*)/Default\.aspx\?tabid=259&language=en-US',
                    r'(.*)/Default\.aspx\?tabid=260&language=en-US',
                    r'(.*)/Default\.aspx\?tabid=261&language=en-US',
                    r'(.*)/Default\.aspx\?tabid=257&language=en-US',
                    r'(.*)/Default\.aspx\?tabid=288&language=en-US'
        ],
        'listRules':[
            {
                'rule':'',
                'detailRules':[
                    {
                        'rule':'',
                        'content':'',
                        'title':'',
                    }
                ]
            }
        ]
    },


    # 伊拉克 ar 已更新
    'iq':{
        'allowed_domains':['moh.gov.iq'],
        'site_url':'https://www.moh.gov.iq',
        'start_urls':['https://moh.gov.iq'],
        'rules':[r'(.*)/index\.php\?name=News(.*)'],
        'language':'ar',
        'publish':[
            {
                'rule':"//table[@class='shadow_table']/tbody/center/table[@dir='rtl']/span[@dir='rtl']/p[2]/text()",
                "format":'%Y-%m-%d %H:%M:%S',
                "extra":iq_time_sub
            }
        ],
        'listRules':[
            {
                'rule':r'(.*)index\.php\?name=News&countpage=(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)index\.php\?name=News&file=article&sid=(.*)',
                        'content':r'/html/body/div[2]/center/table/tbody/tr[7]/td/table[1]/tbody/tr/td[2]/center/table/tbody/tr[2]',
                        'title':r'/html/body/div[2]/center/table/tbody/tr[7]/td/table[1]/tbody/tr/td[2]/center/table/tbody/tr[1]/td/p/font/b',
                        'publish':[
                            {
                                'rule':"//table[@class='shadow_table']/tbody/center/table[@dir='rtl']/span[@dir='rtl']/p[2]/text()",
                                "format":'%Y-%m-%d %H:%M:%S',
                                "extra":iq_time_sub
                            }
                        ],
                    }
                ]
            },
        ]

    },

    # 约旦 网站打不开
    'jo':{
        'allowed_domains':['moh.gov.jo'],
        'site_url':'http://www.moh.gov.jo',
        'start_urls':['http://www.moh.gov.jo/Pages/viewpage.aspx?pageID=262'],
        'rules':[r'(.*)']
    },

    # 巴勒斯坦 en 已更新
    'ps':{
        'allowed_domains':['pna.org','mohiraq.org'],
        'site_url':'http://www.pna.org/moh',
        'start_urls':['http://www.mohiraq.org/news.htm'],
        'rules':[r'(.*)/news/news(.*)'],
        'listRules':[
            {
                'rule':r'(.*)news\.htm(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)news/news(.*)',
                        'content':r'//td[contains(@class,"body")]',
                        'title':r'/html/body/table[1]/tbody/tr[9]/td[1]/h2',
                    }
                ]
            }
        ]
    },


    # 以色列 en 已更新
    "il": {
        'allowed_domains': ['health.gov.il'],
        'site_url': 'https://www.health.gov.il',
        'start_urls': [
            'https://www.health.gov.il/English/News_and_Events/Spokespersons_Messages/Pages/default.aspx',
            
        ],
        'rules':[
                    r'(.*)English/News_and_Events/(.*)', 
                ],
        'publish':[
        
            {
                "rule":'//*[@id="ctl00_PlaceHolderMain_PRDate"]/div/text()',
                "format":"%d/%m/%Y %H:%M"
            }
        ],
        'listRules':[
            {
                'rule':r'(.*)English/News_and_Events/Spokespersons_Messages/Pages/default\.aspx(\?WPID=WPQ6&PN=[0-9]+)?(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)English/News_and_Events/Spokespersons_Messages/Pages/(.*)',
                        'content':r'//*[@id="ctl00_PlaceHolderMain_GovXContentSectionPanel_ctl00__ControlWrapper_RichHtmlField"]',
                        'title':r'//*[@id="ctl00_PlaceHolderMain_GovXMainTitlePanel"]',
                        'publish':[
                            {
                                "rule":'//*[@id="ctl00_PlaceHolderMain_PRDate"]//*[contains(@class,"HealthPRDate")]/text()',
                                "format":"%d/%m/%Y %H:%M"
                            }
                        ],
                    }
                ]
            }
        ]
    },

    # 黎巴嫩 en 通过
    'lb':{
        'allowed_domains':['cas.gov.lb'],
        'site_url':'http://www.cas.gov.lb',
        'start_urls':['http://www.cas.gov.lb/'],
        'rules':[
                    r'(.*)/demographic-and-social-en(.*)',
                    r'(.*)/national-accounts-en(.*)',
                    r'(.*)/housing-characteristics-en(.*)',
                    r'(.*)/economic-statistics-en(.*)',
                    r'(.*)/census-of-building-cbde-en(.*)',
                    r'(.*)/index\.php/mdg-en(.*)',
                    r'(.*)/gender-statistics-en(.*)'
                ],
        'excludes':[r'(.*)/images/(.*)'],
        'listRules':[
            {
                'rule':'',
                'detailRules':[
                    {
                        'rule':'',
                        'content':'',
                        'title':'',
                    }
                ]
            }
        ]
        
    },

    # 塞浦路斯 时间解析有问题 en
    'cy':{
        'allowed_domains':['moh.gov.cy'],
        'site_url':'http://www.moh.gov.cy',
        'start_urls':[
            'https://www.moh.gov.cy/moh/moh.nsf/dmlannouncements_en/dmlannouncements_en?OpenDocument&Start=1&Count=1000&Collapse=1',
            'https://www.moh.gov.cy/moh/moh.nsf/news_archivemain_en/news_archive_en?OpenDocument&Start=1&Count=1000&Expand=2',
            'https://www.moh.gov.cy/moh/moh.nsf/page09_en/page09_en?OpenDocument',

        ],
        'rules':[r'(.*)/Moh/MOH\.nsf/All/(.*)',r'(.*)/moh/moh\.nsf/All/(.*)'],
        'publish':[
                    {
                        'rule':"//form/div[@id='footer']/div[@class='lastupdate']/text()",
                        'format':'Last Modified at: %d/%m/%Y %I:%M:%S PM'
                    },
                    {
                        'rule':"//form/div[@id='footer']/div[@class='lastupdate']/text()",'format':'Last Modified at: %d/%m/%Y %I:%M:%S AM'
                    }
                ]
    },

    # 格鲁吉亚 通过
    'ge':{
        'allowed_domains':['moh.gov.ge'],
        'site_url':'http://www.moh.gov.ge',
        'start_urls':['http://www.moh.gov.ge/en/news/'],
        'rules':[r'(.*)/en/news/[0-9]{4}/(.*)',r'(.*)/en/news/page/(.*)'],
        'publish':[{'rule':"//section[@class='newsInner']/article/section[1]/span/text()",'format':'%d %B, %Y'}]
    },

    # 亚美尼亚 通过
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

    # 乌兹别克斯坦 日期中月份不是英语，无法解析 通过
    'uz':{
        'allowed_domains':['minzdrav.uz'],
        'site_url':'http://www.minzdrav.uz',
        'start_urls':['http://www.minzdrav.uz/en/news/','http://www.minzdrav.uz/en/measure/'],
        'rules':[r'(.*)/en/news/(.*)',r'(.*)/en/measure/(.*)'],
        'publish':[{'rule':"//div[@class='NewsIn']/div[@class='ScrollPane']/span/text()",'format':'%d %B %Y'}]
    },

    # 土库曼斯坦 通过 ru
    'tm':{
        'allowed_domains':['saglykhm.gov.tm'],
        'site_url':'http://www.saglykhm.gov.tm',
        'start_urls':['http://www.saglykhm.gov.tm/ru/news/','http://www.saglykhm.gov.tm/ru/informasionny/'],
        'rules':[r'(.*)/netcat_files/(.*)',r'(.*)/ru/Informasionny/(.*)'],
        'publish':[],
        'excludes':[r'(.*)\.jpg']
    },

    # 吉尔吉斯斯坦 日期中月份为特殊字符，无法解析 ru 通过
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

    # 挪威 en 内容很多 通过 已更新
    'no':{
        'allowed_domains':['regjeringen.no'],
        'site_url':'https://www.regjeringen.no/en/dep/hod/id421',
        'start_urls':[
                        'https://www.regjeringen.no/en/find-document/reports-and-plans/id438817',
                        'https://www.regjeringen.no/en/whatsnew/news-and-press-releases/id2006120',
                    ],
        'rules':[
                    r'(.*)/en/aktuelt/(.*)',
                    r'(.*)/en/dokumenter(.*)',
                    r'(.*)/en/find-document/reports-and-plans/(.*)',
                    r'(.*)/en/whatsnew/news-and-press-releases/(.*)',
                ],
        'publish':[{'rule':'//*[@id="mainContent"]//span[@class="date"]/text()','format':'Date: %Y-%m-%d'}],
        'listRules':[
            {
                'rule':r'(.*)/en/whatsnew/news-and-press-releases/id2006120(/)?(\?page=[0-9]+(.*))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/en/aktuelt/(.*)',
                        'content':r'//*[@id="mainContent"]',
                        'title':r'//*[@id="mainContent"]//header[contains(@class,"article-header")]/h1',
                        'publish':[{'rule':'//*[@id="mainContent"]//span[@class="date"]/text()','format':'Date: %Y-%m-%d'}],

                    }
                ]
            },
            {
                'rule':r'(.*)/en/find-document/reports-and-plans/id438817(/)?(\?page=[0-9]+(.*))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/en/dokumenter/(.*)',
                        'content':r'//*[@id="mainContent"]',
                        'title':r'//*[@id="mainContent"]//header[contains(@class,"article-header")]/h1',
                        'publish':[{'rule':'//*[@id="mainContent"]//span[@class="date"]/text()','format':'Date: %Y-%m-%d'}],

                    }
                ]
            }
        ]
    },

    # 瑞典 en 通过 已更新
    'se':{
        'allowed_domains':['government.se'],
        'site_url':'http://www.government.se/government-of-sweden/ministry-of-health-and-social-affairs',
        'start_urls':['http://www.government.se/government-of-sweden/ministry-of-health-and-social-affairs'],
        'rules':[r'(.*)/articles(.*)'],
        'publish':[{'rule':"//span[@class='published']/time/text()",'format':'%d %B %Y'}],
        'listRules':[
            {
                'rule':r'(.*)/articles(/)?(\?page=[0-9]+(.*))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/articles/[0-9]+/[0-9]+/(.*)',
                        'content':r'//*[@id="content"]',
                        'title':r'//*[@id="content"]/section[1]/h1',
                        'publish':[{'rule':"//span[@class='published']/time/text()",'format':'%d %B %Y'}],

                    }
                ]
            }
        ]
    },

    # 芬兰 en  通过 已更新
    'fi':{
        'allowed_domains':['stm.fi'],
        'site_url':'http://stm.fi/en/frontpage',
        'start_urls':[
            'http://stm.fi/en/frontpage',
            'http://stm.fi/en/publications',
            'http://stm.fi/en/news',
            'http://stm.fi/en/statistics',
            'http://stm.fi/en/press-releases',
        ],
        'rules':[
                    r'(.*)/en/article/-/asset_publisher/(.*)',
                    r'(.*)/en/artikkeli/-/asset_publisher/(.*)',
                    r'(.*)/en/statistics/(.*)',
                    r'(.*)/julkaisu\?pubid=(.*)',
                ],
        'publish':[
            {'rule':"//div[@class='meta clearfix']/div[@class='published row-fluid']/span[@class='date'][1]/text()",'format':'%d.%m.%Y'},
            {'rule':"//div[@class='meta clearfix']/div[@class='published row-fluid']/span[@class='date']/text()",'format':'%d.%m.%Y'}
        ],
        'listRules':[
            {
                'rule':r'(.*)/en/news(\?p_p_auth=(.*))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/en/artikkeli/-/asset_publisher/(.*)',
                        'content':r'//div[contains(@class,"journal-content-article")]',
                        'title':r'//div[contains(@class,"journal-content-article")]//h1[@itemprop="name"]',
                        'publish':[
                            {'rule':"//div[@class='meta clearfix']/div[@class='published row-fluid']/span[@class='date'][1]/text()",'format':'%d.%m.%Y'},
                            {'rule':"//div[@class='meta clearfix']/div[@class='published row-fluid']/span[@class='date']/text()",'format':'%d.%m.%Y'}
                        ],
                    }
                ]
            },
            {
                'rule':r'(.*)/en/press-releases(\?p_p_auth=(.*))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/en/(artikkeli|article)/-/asset_publisher/(.*)',
                        'content':r'//div[contains(@class,"journal-content-article")]',
                        'title':r'//div[contains(@class,"journal-content-article")]//h1[@itemprop="name"]',
                        'publish':[
                            {'rule':"//div[@class='meta clearfix']/div[@class='published row-fluid']/span[@class='date'][1]/text()",'format':'%d.%m.%Y'},
                            {'rule':"//div[@class='meta clearfix']/div[@class='published row-fluid']/span[@class='date']/text()",'format':'%d.%m.%Y'}
                        ],
                    }
                ]
            },
            {
                'rule':r'(.*)en/publications(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/julkaisu\?pubid=(.*)',
                        'content':r'//*[@id="p_p_id_julkarisview_WAR_julkarisportlet_"]',
                        'title':r'//*[@id="p_p_id_julkarisview_WAR_julkarisportlet_"]/div/div/div/div/div[1]/div/h1',
                        'publish':[
                            {'rule':"//div[@class='meta clearfix']/div[@class='published row-fluid']/span[@class='date'][1]/text()",'format':'%d.%m.%Y'},
                            {'rule':"//div[@class='meta clearfix']/div[@class='published row-fluid']/span[@class='date']/text()",'format':'%d.%m.%Y'}
                        ],
                    }
                ]
            },
            {
                'rule':r'(.*)en/statistics(.*)',
                'detailRules':[
                   
                ]
            },


        ]
    },

    # 丹麦 en 通过 已更新
    'dk':{
        'allowed_domains':['stm.dk'],
        'site_url':'http://www.stm.dk/_a_1644.html',
        'start_urls':[
            'http://www.stm.dk/_a_1644.html',
            'http://www.stm.dk/index.dsp?page=11467&action=page_overview_search&l1_valg=-1&l2_valg=-1',
            
        ],
        'rules':[
                    r'(.*)'
        ],
        'listRules':[
            {
                'rule':r'(.*)/index\.dsp(\?page=[0-9]+&action=page_overview_search(.*))?',
                'detailRules':[
                    {
                        'rule':r'(.*)/_p_[0-9]+(.*)',
                        'content':r'//*[@id="main"]',
                        'title':r'//*[@id="main"]/div[contains(@class,"maininner maininner-page")]/h1',
                    }
                ]
            }
        ]
    },

    # 俄罗斯 ru 通过 已更新
    'ru':{
        'allowed_domains':['rosminzdrav.ru'],
        'site_url':'http://www.rosminzdrav.ru',
        'start_urls':[
            'https://www.rosminzdrav.ru/news',
            'https://www.rosminzdrav.ru/regional_news'
        ],
        'rules':[
            r'(.*)/news(.*)',
            r'(.*)/regional_news(.*)'
        ],
        'publish':[
                {'rule':"//p[@class='timestamps']/time[1]/text()",
                'format':'Материал опубликован %d %B %Y в %H:%M. '}
                ],
        'excludes':[
                    r'(.*)\.jpg(.*)',
                    r'(.*)comments.atom',
                    r'(.*)system/attachments/attaches/(.*)'
        ],
        'language':'ru',
        
        'listRules':[
            {
                'rule':r'(.*)/news(/)?(\?page=[0-9]+(.*))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/news/[0-9]+/[0-9]+/[0-9]+/(.*)',
                        'content':r'//*[@id="mz-container"]/article',
                        'title':r'//*[@id="mz-container"]/h1',
                        
                    }
                ]
            },
            {
                'rule':r'(.*)/regional_news(/)?(\?page=[0-9]+(.*))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/regional_news/(.*)',
                        'content':r'//*[@id="mz-container"]/article',
                        'title':r'//*[@id="mz-container"]/h1',
                        
                    }
                ]
            }
        ]
    },

    # 爱沙尼亚 较多 en 通过 已更新
    'ee':{
        'allowed_domains':['valitsus.ee'],
        'site_url':'https://www.valitsus.ee/en',
        'start_urls':['https://www.valitsus.ee/en/news?title=&title_op=word&source=23&date=All&date_custom%5Bmin%5D=&date_custom%5Bmax%5D='],
        'rules':[
            r'(.*)/en/news/(.*)',
            r'(.*)/en/news\?(.*)page=([0-9]{1,3})'

        ],
        'publish':[{'rule':"//footer[@class='submitted']/span[1]/text()",'format':'%d. %B %Y - %H:%M'}],
        'excludes':[r'\.jpg(.*)'],
        'listRules':[
            {
                'rule':r'((?!(/et)|(/ru)).)*/en/news(/)?(\?(.*)page=[0-9]+(.*))?$',
                'detailRules':[
                    {
                        'rule':r'((?!(/et)|(/ru)).)*/en/news/[^\?\"]+$',
                        'content':r'//*[@id="block-system-main"]',
                        'title':r'//*[@id="page-title"]',
                        'publish':[{'rule':"//footer[@class='submitted']/span[1]/text()",'format':'%d. %B %Y - %H:%M'}],

                    }
                ]
            }
        ]
    },

    # 拉脱维亚 网页打不开
    'lv':{
        'allowed_domains':['vza.gov.lv'],
        'site_url':'http://www.vza.gov.lv',
        'start_urls':[]
    },

    # 立陶宛 en 通过 已更新
    'lt':{
        'allowed_domains':['sam.lrv.lt'],
        'site_url':'http://sam.lrv.lt/en',
        'start_urls':['http://sam.lrv.lt/en/news'],
        'rules':[
            r'(.*)/en/news/(.*)',
            r'(.*)/en/news\?years=([0-9]{4})(.*)'
        ],
        'publish':[{'rule':"//div[@class='row startDate_wrap']/div/div[2]/p/text()",'format':'%Y %m %d'}],
        'listRules':[
            {
                'rule':r'(.*)/en/news(/)?(\?years=([0-9]{4}(.*)))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/en/news/[^\?]+',
                        'content':r'//*[@id="module_news"]//*[contains(@class,"content text to_left")]',
                        'title':r'//*[@id="module_news"]//*[contains(@class,"main_content")]/div[2]/h1',
                        'publish':[{'rule':"//div[@class='row startDate_wrap']/div/div[2]/p/text()",'format':'%Y %m %d'}],
                    }
                ]
            }
        ]
    },

    # 白俄罗斯 en 通过 已更新
    'by':{
        'allowed_domains':['minzdrav.gov.by'],
        'site_url':'http://www.minzdrav.gov.by/en',
        'start_urls':[
            'http://www.minzdrav.gov.by/en/static/programmes-of-ministry-of-heal/',
            'http://minzdrav.gov.by/en/static/stat_data',
        ],
        'rules':[
                    r'(.*)/en/static/programmes-of-ministry-of-heal/scientic_progr/(.*)',
                    r'(.*)/en/static/programmes-of-ministry-of-heal/state_progr(.*)'
                    r'(.*)/en/static/stat_data/(.*)'
        ],
        'listRules':[
            {
                'rule':r'(.*)/en/static/programmes-of-ministry-of-heal/scientic_progr(/)?',
                'detailRules':[
                    {
                        'rule':r'(.*)/en/static/programmes-of-ministry-of-heal/scientic_progr/(.*)',
                        'content':r'//*[@id="content"]',
                        'title':r'//*[@id="content"]/*[contains(@class,"section")]/h2',
                    }
                ]
            },
            {
                'rule':r'(.*)/en/static/stat_data/(.*)',
                'detailRules':[
                ]
            },

        ]
    },

    # 乌克兰 en 通过
    'ua':{
        'allowed_domains':['health.gov.ua'],
        'site_url':'http://www.health.gov.ua/www.nsf/all/index_e?opendocument',
        'start_urls':['http://www.health.gov.ua/www.nsf/all/e05-01?opendocument'],
        'rules':[
                    r'(.*)/www\.nsf/all/e05-01-01\?opendocument',
                    r'(.*)/www\.nsf/all/e05-01-02\?opendocument',
                    r'(.*)/www\.nsf/all/u05-01-01\?opendocument'
        ],
        'listRules':[
            {
                'rule':'',
                'detailRules':[
                    {
                        'rule':'',
                        'content':'',
                        'title':'',
                    }
                ]
            }
        ]
    },

    # 波兰 en 通过
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
    
    # 德国 en 通过 已更新
    'de':{
        'allowed_domains':['bundesgesundheitsministerium.de'],
        'site_url':'http://www.bundesgesundheitsministerium.de/en/en.html',
        'start_urls':['http://www.bundesgesundheitsministerium.de/en/ministry/news.html'],
        'rules':[
            r'(.*)/en/ministry/(.*)'
        ],
        'publish':[{'rule':"//p/span[@class='article-date']/text()",'format':'%d %B %Y'}],
        'excludes':[
                        r'(.*)/en/en/ministry/leadership(.*)',
                        r'(.*)/en/en/ministry/international-co-operation(.*)',
                        r'(.*)/en/en/ministry/the-federal-ministry-of-health(.*)',
                        r'(.*)/en/en/ministry/authorities-within-the-remit(.*)',
                        r'(.*)/en/en/ministry/laws(.*)',
                        r'(.*)/en/en/ministry/press-office(.*)'
        ],
        'listRules':[
            {
                'rule':r'(.*)/en/ministry/news\.html(/)?$',
                'detailRules':[
                    {
                        'rule':r'(.*)en/ministry/news/(.*)',
                        'content':r'//*[@id="skiplink2maincontent"]',
                        'title':r'//*[@id="skiplink2maincontent"]/div[1]/h1',
                        'publish':[{'rule':"//p/span[@class='article-date']/text()",'format':'%d %B %Y'}],
                    }
                ]
            }
        ]

    },

    # 捷克 en 通过
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

    # 斯洛伐克 en 通过
    'sk':{
        'allowed_domains':['uvzsr.sk'],
        'site_url':'http://www.uvzsr.sk',
        'start_urls':['http://www.uvzsr.sk/en/index.php/documents','http://www.uvzsr.sk/en/index.php/expert-departments'],
        'rules':[r'(.*)/en/index\.php/documents'],
        'publish':[]
    },
    
    # 奥地利 en 通过
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

    # 瑞士 de 通过 已更新
    'ch':{
        'allowed_domains':['bag.admin.ch'],
        'site_url':'https://www.bag.admin.ch/bag/de/home.html',
        'start_urls':[
                        'https://www.bag.admin.ch/bag/de/home/aktuell/news.html',
                        'https://www.bag.admin.ch/bag/de/home/aktuell/medienmitteilungen.html',
                        'https://www.bag.admin.ch/bag/de/home/aktuell/veranstaltungen.html',
                        'https://www.bag.admin.ch/bag/de/home/service/publikationen.html',

                    ],
        'rules':[
                    r'(.*)/bag/de/home/aktuell/news(.*)',
                    r'(.*)/bag/de/home/aktuell/medienmitteilungen\.msg-id(.*)',
                    r'(.*)/bag/de/home/aktuell/veranstaltungen/(.*)'
                ],
        'publish':[
            {
                'rule':'//*[@id="content"]/div/div[1]/div[8]/p[1]/small/span/text()',
                'format':'%Y-%m-%d',
                'extra':ch_time_sub,
            }
        ],
        'language':'de',
        'listRules':[
            {
                'rule':r'(.*)/bag/de/home/aktuell/news\.html(/)?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/bag/de/home/aktuell/news/(.*)$',
                        'content':r'//*[@id="content"]//*[contains(@class,"mod-text")]',
                        'title':r'//*[@id="content"]//*[contains(@class,"mod-contentpage")]/h1',
                        'publish':[
                            {
                                'rule':'//*[@id="content"]/div/div[1]/div[8]/p[1]/small/span/text()',
                                'format':'%Y-%m-%d',
                                'extra':ch_time_sub,
                            }
                        ],
                    },
                    
                ]
            },
            {
                'rule':r'(.*)/bag/de/home/aktuell/medienmitteilungen\.html(/)?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/bag/de/home/aktuell/medienmitteilungen\.msg-id(.*)$',
                        'content':r'//*[@id="content"]//*[contains(@class,"mod-nsbnewsdetails")]',
                        'title':r'//*[@id="content"]//*[contains(@class,"contentHead")]/h1',
                        'publish':[
                            {
                                'rule':'//*[@id="content"]/div/div[1]/div[8]/p[1]/small/span/text()',
                                'format':'%Y-%m-%d',
                                'extra':ch_time_sub,
                            }
                        ],
                    },
                    
                ]
            },
            {
                'rule':r'(.*)/bag/de/home/service/publikationen(.*)$',
                'detailRules':[
                ]
            }
        ]
    },

    # 列支敦士登 js加载 无法爬取
    'li':{
        'allowed_domains':['llv.li'],
        'site_url':'https://www.llv.li/#/1908/amt-fur-gesundheit',
        'start_urls':['https://www.llv.li/#/40/'],
        'rules':[r'(.*)/[0-9]{2,5}/(.*)',r'(.*)/files/dss/(.*)']
    },

    # 英国 通过 已更新
    'uk':{
        'allowed_domains':['gov.uk'],
        'site_url':'https://www.gov.uk/government/organisations/department-of-health',
        'start_urls':[
            'https://www.gov.uk/government/organisations/public-health-england',
            'https://www.gov.uk/government/announcements?departments%5B%5D=public-health-england',
            'https://www.gov.uk/government/publications?departments%5B%5D=public-health-england',

            'https://www.gov.uk/government/latest?departments%5B%5D=public-health-england',

        ],
        'rules':[
                    r'(.*)/government/publications/(.*)',
                    r'(.*)/government/news/(.*)',
                    r'(.*)/government/consultations/(.*)',
                    r'(.*)/government/latest(.*)'
                ],
        'publish':[{'rule':"//div[@id='history']/p[1]/span[@class='published definition']/text()",'format':'%d %B %Y'}],
        'listRules':[
            {
                'rule':r'(.*)government/announcements\?departments%5B%5D=public-health-england(&page=[0-9](.*))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/government/news/(.*)',
                        'content':r'//*[@id="content"]',
                        'title':r'//*[@id="content"]//h1[contains(@class,"pub-c-title__text")]',
                        
                        'publish':[
                            {
                                'rule':'//*[@id="content"]//*[contains(@class,"app-c-published-dates")][1]/text()',
                                'format':'Published %d %B %Y'
                            },
                        ],
                    }
                ]
            },
            {
                'rule':r'(.*)government/publications\?departments%5B%5D=public-health-england(&page=[0-9](.*))?$',
                'detailRules':[
                ]
            },
            {
                'rule':r'(.*)government/publications/(.*)',
                'detailRules':[
                ]
            },

        ]
    },

    # 爱尔兰 网页打不开
    'ie':{
        'allowed_domains':['doh.ie'],
        'site_url':'http://www.doh.ie',
        'start_urls':[]
    },

    # 荷兰 en 已更新
    'nl':{
        'allowed_domains':['government.nl'],
        'site_url':'https://www.government.nl/ministries/ministry-of-health-welfare-and-sport',
        'start_urls':[
            'https://www.government.nl/ministries/ministry-of-health-welfare-and-sport/news',
            'https://www.government.nl/ministries/ministry-of-health-welfare-and-sport/documents',
            # 'https://www.government.nl/ministries/ministry-of-health-welfare-and-sport/topics',

            ],
        'rules':[
            r'(.*)/ministries/ministry-of-health-welfare-and-sport/news(.*)'
        ],
        'publish':[
            {
                'rule':'//*[@id="content"]//p[contains(@class,"article-meta")]/text()',
                'format':'News item | %d-%m-%Y | %H:%M'
            }
        ],
        'listRules':[
            {
                'rule':r'(.*)/ministries/ministry-of-health-welfare-and-sport/news(/)?(\?page=[0-9]+(.*))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/ministries/ministry-of-health-welfare-and-sport/news/[0-9]+/[0-9]+/[0-9]+/(.*)$',
                        'content':r'//*[@id="content"]',
                        'title':r'//*[@id="content"]/h1',
                        'publish':[
                            {
                                'rule':'//*[@id="content"]//p[contains(@class,"article-meta")]/text()',
                                'format':'News item | %d-%m-%Y | %H:%M'
                            }
                        ],
                    }
                ]
            },
            {
                'rule':r'(.*)/ministries/ministry-of-health-welfare-and-sport/documents(.*)',
                'detailRules':[]
            },

        ]
    },

    # 比利时 en 已更新
    'be':{
        'allowed_domains':['belgium.be'],
        'site_url':'https://www.belgium.be/en/health',
        'start_urls':['https://www.belgium.be/en/news'],
        'rules':[r'(.*)/en/news(.*)'],
        'publish':[
            {
                'rule':"//div[@id='block-system-main']/div/div[@class='submitted']/text()",
                'format':'date: %d %B %Y'
            },
        ],
        'listRules':[
            {
                'rule':r'(.*)/en/news(/)?(/overview\?f\[0\]=created%3A[0-9]+)?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/en/news/[0-9]+/(.*)$',
                        'content':r"//div[@id='block-system-main']",
                        'title':r'//*[@id="content"]//*[contains(@class,"page-title")]',
                        'publish':[
                            {
                                'rule':r"//div[@id='block-system-main']/div/div[@class='submitted']/text()",
                                'format':'date: %d %B %Y'
                            },
                        ],
                    }
                ]
            }
        ]
    },

    # 卢森堡 通过
    'lu':{
        'allowed_domains':['sante.public.lu'],
        'site_url':'http://www.sante.public.lu/fr/politique-sante/ministere-sante/index.html',
        'start_urls':['http://www.sante.public.lu/fr/actualites/index.html'],
        'rules':[r'(.*)/fr/actualites/(.*)'],
        'publish':[{'rule':"//time[@class='article-published']/text()",'format':'%d-%m-%Y'}]
    },

    # 法国 已更新
    'fr':{
        'allowed_domains':['solidarites-sante.gouv.fr'],
        'site_url':'http://solidarites-sante.gouv.fr',
        'start_urls':[
            'http://solidarites-sante.gouv.fr/actualites',
            'http://drees.solidarites-sante.gouv.fr/etudes-et-statistiques/publications',

        ],
        'rules':[
                    r'(.*)/actualites(.*)'
                ],
        'publish':[
            {
                'rule':'//*[@id="content"]//*[contains(@class,"main-article__date date--publication")]/text()',
                'format':'%d.%m.%y'
            }
        ],
        'language':'fr',
        'listRules':[
            {
                'rule':r'(.*)/actualites/presse(/)?(\?(.*))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/actualites/presse/\w+/article/[^\?]+$',
                        'content':r'//*[@id="content"]//*[contains(@class,"main-article__texte")]',
                        'title':r'//*[@id="content"]//*[contains(@class,"main-article__titre")]',
                        'publish':[
                            {
                                'rule':r'//*[@id="content"]//*[contains(@class,"date--publication")]/text()',
                                'format':'%d.%m.%y',    
                            }
                        ]
                    }
                ]
            },
            {
                'rule':r'(.*)/actualites/evenements(/)?(\?(.*))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/actualites/evenements/article/[^\?]+$',
                        'content':r'//*[@id="content"]//*[contains(@class,"main-article__texte")]',
                        'title':r'//*[@id="content"]//*[contains(@class,"main-article__titre")]',
                        'publish':[
                            {
                                'rule':r'//*[@id="content"]//*[contains(@class,"date--publication")]/text()',
                                'format':'%d.%m.%y',    
                            }
                        ]
                    }
                ]
            },
            {
                'rule':r'(.*)/soins-et-maladies/medicaments(/)?(\?(.*))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/soins-et-maladies/medicaments/[^\?]+$',
                        'content':r'//*[@id="content"]//*[contains(@class,"main-article__texte")]',
                        'title':r'//*[@id="content"]//*[contains(@class,"main-article__titre")]',
                        'publish':[
                            {
                                'rule':r'//*[@id="content"]//*[contains(@class,"date--publication")]/text()',
                                'format':'%d.%m.%y',    
                            }
                        ]
                    }
                ]
            },
            {
                'rule':r'(.*)/soins-et-maladies/maladies(/)?(\?(.*))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/soins-et-maladies/maladies/[^\?]+$',
                        'content':r'//*[@id="content"]//*[contains(@class,"main-article__texte")]',
                        'title':r'//*[@id="content"]//*[contains(@class,"main-article__titre")]',
                        'publish':[
                            {
                                'rule':r'//*[@id="content"]//*[contains(@class,"date--publication")]/text()',
                                'format':'%d.%m.%y',    
                            }
                        ]
                    }
                ]
            },
            {
                'rule':r'(.*)/etudes-et-statistiques/publications(/)?(\?(.*))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/etudes-et-statistiques/publications/[^\?]+$',
                        'content':r'//*[@id="content"]//*[contains(@class,"main-article__texte")]',
                        'title':r'//*[@id="content"]//*[contains(@class,"main-article__titre")]',
                        'publish':[
                            {
                                'rule':r'//*[@id="content"]//*[contains(@class,"date--publication")]/text()',
                                'format':'%d.%m.%y',
                            }
                        ]
                    },
                    # {
                    #     'rule':r'(.*)/etudes-et-statistiques/publications/[^\?]+$',
                    #     'content':r'//*[@id="content"]//*[contains(@class,"presentation-rubrique")]',
                    #     'title':r'//*[@id="content"]//*[contains(@class,"page__titre")],
                    #     'publish':[
                    #         {
                    #             'rule':r'//*[@id="content"]//*[contains(@class,"date--publication")]/text()',
                    #             'format':'%d.%m.%Y',    
                    #         }
                    #     ]
                    # }
                ]
            }
        ]
    },

    # 摩纳哥 通过
    'mc':{
        'allowed_domains':['en.gouv.mc'],
        'site_url':'http://en.gouv.mc/Government-Institutions/The-Government/Ministry-of-Health-and-Social-Affairs',
        'start_urls':['http://en.gouv.mc/News'],
        'rules':[r'(.*)/News/(.*)'],
        'publish':[{'rule':"//div[@class='info']/span[@class='date']/text()",'format':'%d %B %Y'}]
    },

    # 西班牙 en 已更新
    'es':{
        'allowed_domains':['msc.es'],
        'site_url':'http://www.msc.es/en/home.htm',
        'start_urls':[
            'http://www.msc.es/en/gabinete/notasPrensa.do?metodo=verHistorico',
            'http://www.msc.es/en/gabinete/notasPrensa.do',
            'http://www.msc.es/en/biblioPublic/publicaciones/home.htm',



        ],
        'rules':[r'(.*)/en/gabinete/notasPrensa\.do(.*)'],
        'publish':[
            {
                'rule':"//section[contains(@class,'informacion']/div[2]/p[1]/strong/text()",
                'format':'%Y-%m-%d',
                'extra':es_time_sub,
            },
        ],
        'listRules':[
            {
                'rule':r'(.*)en/gabinete/notasPrensa\.do(/)?(\?time=[0-9]+(.*))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)en/gabinete/notasPrensa\.do(/)?(\?id=[0-9]+)(.*)$',
                        'title':r'//section[contains(@class,"informacion")]/h2',
                        'content':r'//section[contains(@class,"informacion")]',
                        'publish':[
                            {
                                'rule':"//section[contains(@class,'informacion')]/div[2]/p[1]/strong/text()",
                                'format':'%Y-%m-%d',
                                'extra':es_time_sub,
                            },
                        ],
                    }
                ]
            },
            {
                'rule':r'(.*)en/biblioPublic/publicaciones(.*)',
                'detailRules':[
                ]
            },
            {
                'rule':r'(.*)en/estadEstudios(.*)',
                'detailRules':[
                ]
            }
        ]
    },

    # 葡萄牙 通过 已更新
    'pt':{
        'allowed_domains':['sns.gov.pt'],
        'site_url':'https://www.sns.gov.pt/',
        'start_urls':['https://www.sns.gov.pt/noticias/'],
        'rules':[
                    r'(.*)/noticias/[0-9]{4}/[0-9]{2}/[0-9]{2}/(.*)',
                    r'(.*)/noticias/page/(.*)'
                ],
        'publish':[
            {
                'rule':"//div[@class='post-info-bar']/div[@class='post-info cf col-md-2 col-xs-12']/span/text()",
                'format':'%d/%m/%Y'
            }
        ],
         'listRules':[
            {
                'rule':r'(.*)/noticias(/)?(/page/[0-9]+(.*))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)noticias/[0-9]+/[0-9]+/[0-9]+/(.*)$',
                        'content':r'//article[contains(@class,"content")]',
                        'title':r'//*[@id="page"]//article//*[contains(@class,"page-title")]',
                        'publish':[
                            {
                                'rule':"//*[contains(@class,'post-info-bar')]//*[contains(@class,'post-info')]/span/text()",
                                'format':'%d/%m/%Y'
                            }
                        ],

                    }
                ]
            }
        ]
    },

    # 安道尔 en 通过
    'ad':{
        'allowed_domains':['salutibenestar.ad'],
        'site_url':'http://www.salutibenestar.ad/index2.htm',
        'start_urls':['https://www.salutibenestar.ad/temes-de-salut'],
        'rules':[r'(.*)/temes-de-salut/(.*)']
    },

    # 意大利 已更新
    'it':{
        'allowed_domains':['salute.gov.it'],
        'site_url':'http://http://www.salute.gov.it',
        'start_urls':[
            'http://www.salute.gov.it/portale/home.html',
            'http://www.salute.gov.it/portale/news/p3_2.html',

        ],
        'listRules':[
            {
                'rule':r'(.*)/portale/news/p3_2_1\.jsp(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/portale/news/p3_2_1_1_1\.jsp(.*)id=[0-9]+(.*)',
                        'content':r'//*[@id="main-content"]',
                        'title':r'//*[@id="page-header"]/div/h2',
                        'publish':[
                            {
                                'rule':r'//*[@id="foglia"]//*[contains(@class,"meta")]/div[contains(@class,"update")]/p/strong[1]/text()',
                                'format':'%Y-%m-%d',
                                'extra':it_time_sub,
                            }
                        ]

                    }
                ]
            },
            {
                'rule':r'(.*)/portale/news/p3_2_2\.jsp(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/portale/news/p3_2_2_1_1\.jsp(.*)id=[0-9]+(.*)',
                        'content':r'//*[@id="main-content"]',
                        'title':r'//*[@id="page-header"]/div/h2',
                        'publish':[
                            {
                                'rule':r'//*[@id="foglia"]//*[contains(@class,"meta")]/div[contains(@class,"update")]/p/strong[1]/text()',
                                'format':'%Y-%m-%d',
                                'extra':it_time_sub,
                            }
                        ]

                    }
                ]
            },
            {
                'rule':r'(.*)/portale/news/p3_2_3\.jsp(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/portale/news/p3_2_3_1_1\.jsp(.*)id=[0-9]+(.*)',
                        'content':r'//*[@id="main-content"]',
                        'title':r'//*[@id="page-header"]/div/h2',
                        'publish':[
                            {
                                'rule':r'//*[@id="foglia"]//*[contains(@class,"meta")]/div[contains(@class,"update")]/p/strong[1]/text()',
                                'format':'%Y-%m-%d',
                                'extra':it_time_sub,
                            }
                        ]

                    }
                ]
            },
            {
                'rule':r'(.*)/portale/news/p3_2_6\.jsp(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/portale/news/p3_2_6_1_1\.jsp(.*)id=[0-9]+(.*)',
                        'content':r'//*[@id="main-content"]',
                        'title':r'//*[@id="page-header"]/div/h2',
                        'publish':[
                            {
                                'rule':r'//*[@id="foglia"]//*[contains(@class,"meta")]/div[contains(@class,"update")]/p/strong[1]/text()',
                                'format':'%Y-%m-%d',
                                'extra':it_time_sub,
                            }
                        ]

                    }
                ]
            },
            {
                'rule':r'(.*)/portale/documentazione/p6_2_2\.jsp(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/portale/news/p6_2_2_1\.jsp(.*)id=[0-9]+(.*)',
                        'content':r'//*[@id="main-content"]',
                        'title':r'//*[@id="page-header"]/div/h2',
                        'publish':[
                            {
                                'rule':r'//*[@id="foglia"]//*[contains(@class,"meta")]/div[contains(@class,"update")]/p/strong[1]/text()',
                                'format':'%Y-%m-%d',
                                'extra':it_time_sub,
                            }
                        ]

                    }
                ]
            }








        ]

    },

    # 圣马力诺 没有权限，需要登录
    'sm':{
        'allowed_domains':['sanita.segreteria.sm'],
        'site_url':'http://www.sanita.segreteria.sm'
    },

    # 马耳他 en 通过
    'mt':{
        'allowed_domains':['gov.mt'],
        'site_url':'https://deputyprimeminister.gov.mt/en/Pages/health.aspx',
        'start_urls':['https://deputyprimeminister.gov.mt/en/news/Pages/News.aspx'],
        'rules':[r'(.*)/en/Government/Press%20Releases/Pages/[0-9]{4}/(.*)',r'(.*)/en/news/Pages/News(.*)'],
        'publish':[
            {
                'rule':"//div[@class='content']/div[@class='header']/div[@class='info']/text()",
                'format':'%b %d, %Y'
            },
            {
                'rule':'//*[@id="ctl00_MSO_ContentDiv"]//*[contains(@class,"info")]/text()[3]',
                'format':'%b %d, %Y'
            }
        ]
    },

    # 匈牙利 网页打不开
    'hu':{
        'allowed_domains':['enum.hu'],
        'site_url':'http://www.eum.hu',
        'start_urls':[''],
        'rules':[],

    },

    # 塞尔维亚 ru 通过
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
        'language':'rs',
        'publish':[
            {
                'rule':"//div[@id='content']/div[@id='content_head']/text()",
                'format':"%Y-%m-%d",
                'extra':rs_time_sub,
            }
        ],
    },

     # 保加利亚 ru 通过
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
        'language':'bg',
        'publish':[
            {
                "rule":"//div[@id='top']/ul[@class='newsdate']/time[@datetime]/@datetime",
                "format":"%Y-%m-%dT%H:%M:%S+03:00"
            },
        ]
    },

    # 斯洛文尼亚 es 通过
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
        'rules':[
            r'(.*)/si/medijsko_sredisce(.*)',
            r'(.*)/si/pogoste_vsebine_za_javnost(.*)'
        ],
        'publish':[
            {
                "rule":"//div[@id='mainContainer']//div[@class='newsdate']/text()",
                "format":"%d. %m. %Y"
            }
        ]
    },

    # 梵蒂冈 没有网址

    # 克罗地亚 en 通过
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
        'rules':[
            r'(.*)/vijesti/8(.*)',
            r'(.*)/vijesti(.*)',
            r'(.*)/pristup-informacijama(.*)'
        ],
        'publish':[
            {
                "rule":"//div[@class='article_info']//*[@class='time_info']/text()",
                "format":"Objavljeno: %d.%m.%Y."
            }
        ]

    },

    # 波斯尼亚和黑塞哥维那 es 通过 文件多
    'ba':{
        'allowed_domains':['fmoh.gov.ba'],
        'site_url':'http://www.fmoh.gov.ba',
        'start_urls':[
            'http://www.fmoh.gov.ba/index.php/novosti-iz-ministarstva'
        ],
        'rules':[
            r'(.*)/index\.php/novosti-iz-ministarstva(.*)'
        ],
        'publish':[
            {
                'rule':'//*[@id="system"]//header/p[contains(@class,"meta")]/time/@datetime',
                
                'format':'%Y-%m-%d',
                
            }
        ]
    },

    # 黑山 en 通过
    'me':{
        'allowed_domains':['mzd.gov.me'],
        'site_url':'http://www.mzd.gov.me/en/ministry',
        'start_urls':['http://www.mzd.gov.me/en/news'],
        'rules':[r'(.*)/en/news(.*)'],
        'publish':[
            {
                'rule':"//*[@id='aspnetForm']//div[contains(@class,'detalji-hold')]/div[contains(@class,'detalji')]/text()[2]",
                'format':'%Y-%m-%d %H:%M',
                'extra':me_time_sub,
            }
        ]
    },

    # 罗马尼亚 es 通过
    'ro':{
        'allowed_domains':['ms.ro'],
        'site_url':'http://www.ms.ro',
        'start_urls':['http://www.ms.ro/comunicate/'],
        'rules':[r'(.*)/[0-9]{4}/[0-9]{2}/[0-9]{2}/(.*)',r'(.*)/comunicate/(.*)'],
        'publish':[
            {
                'rule':'//*[@id="main"]//article//time[contains(@class,"date-container")]/text()',
                'format':'%Y-%m-%d',
                'extra':ro_time_sub,
            }
        ]
    },

    # 希腊 en
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

    # 马其顿 ru
    'mk':{
        'allowed_domains':['vlada.mk'],
        'site_url':'http://vlada.mk/?q=node/353&language=en-gb',
        'start_urls':['http://vlada.mk/media-centar'],
        'rules':[r'(.*)/node/(.*)',r'(.*)/media-centar(.*)'],
        'publish':[
            {
                'rule':"//div[@class='meta post-info']/div[@class='meta submitted']/text()",
                'format':'%d.%m.%Y        	'
            },
        ],
        'language':'ru'
    },




    ###############################################
    # 非洲
    ###############################################

    ## 埃及 ar
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
    ## 摩洛哥 fr 通过
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
    ## 突尼斯 fr 通过
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
    ## 塞内加尔 fr 通过
    'sn':{
        'allowed_domains':['sante.gouv.sn'],
        'language':'fr-fr',
        'site_url':'http://www.sante.gouv.sn',
        'start_urls':[
            'http://www.sante.gouv.sn/index.php',
        ],
        'language':'fr',
        'rules':[
            r'(.*)page-reader-les-actualites-get\.php(.*)',
            r'(.*)/page-reader-content-details\.php(.*)',
            r'(.*)page-reader-categories-article-presse(.*)'
        ],
    },
    ## 冈比亚 en 通过
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

    ## 利比里亚 通过
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

    
    ## 加纳 通过
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
    ## 喀麦隆 通过
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
    ## 索马里 通过
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
    ## 坦桑尼亚 痛过
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
    ## 肯尼亚 通过
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
    ## 乌干达 通过
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
    ## 马拉维 en 通过 有些需要登录
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
    ## 毛里求斯 通过 en
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
    ## 塞舌尔 en 通过 样式乱
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
    ## 纳米比亚 通过 en
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
    ## 伯兹瓦纳 通过 en
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
    ## 莱索托 通过
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
    ## 南非 已更新
    'za':{
        'allowed_domains':['health.gov.za'],
        'site_url':'http://www.health.gov.za',
        'start_urls':['http://www.health.gov.za'],
        'rules':[
            r'(.*)/index\.php/(diseases|gf-tb-program)(.*)',
            r'(.*)/index\.php/component/phocadownload(.*)',
            r'(.*)/index\.php/[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}/[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}(.*)'
        ],
        'listRules':[
            {
                'rule':r'(.*)/index\.php/[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}/[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}(.*)',
                'detailRules':[
                ]
            },
            {
                'rule':r'(.*)/index\.php/[0-9]{4}-[0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}-[0-9]{1,2}',
                'detailRules':[
                ]

            },
            {
                'rule':r'(.*)/index\.php/component/phocadownload(.*)',
                'detailRules':[
                ]

            },
           
            {
                'rule':r'(.*)/index\.php/(diseases|gf-tb-program)([^\?])',
                'detailRules':[
                ]

            },

            
        ]
    },

    ###############################################
    # 北美洲
    ###############################################

    ## 美国 通过 en 已更新
    'us':{
        'allowed_domains':['hhs.gov','archive-it.org'],
        'site_url':'https://www.hhs.gov',
        'start_urls':[
            'https://www.hhs.gov',
            'https://www.hhs.gov/blog/index.html',
            'https://archive-it.org/collections/3926?fc=websiteGroup%3AHHS+News+Releases',
            'https://www.hhs.gov/programs/index.html',

        ],
        'rules':[
            r'(.*)/blog(.*)',
            r'(.*)/about/news(.*)',
            # r'(.*)/about/strategic-plan(.*)',
            # r'(.*)/programs/prevention-and-wellness(.*)',
            # r'(.*)/programs/research(.*)',
            # r'(.*)/programs/topic-sites(.*)'
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
        ],
        'listRules':[
            {
                'rule':r'(.*)about/news/(index\.html)|(.*-news-release)(.*)',
                'detailRules':[
                    {
                        'rule':r'((?!3926).)*/about/news/(.*)',
                        'content':r'//*[@id="site-content"]//*[contains(@class,"content")]',
                        'title':r'//*[contains(@class,"news-header")]/h1',
                        'publish':[
                            # {
                            #     'rule':'//*[@id="block-system-main"]//*[contains(@class,"date-display-single") and @content]/@content',
                            #     'format':'%Y-%m-%dT%H:%M:%S-05:00'
                            # },
                            {
                                'rule':'//*[@id="site-content"]//*[contains(@class,"content")]//*[contains(@class,"left")]/b/text()[2]',
                                'format':'%B %d, %Y'
                            }
                        ],
                    },
                ]
            },
            {
                'rule':r'(.*)collections/3926\?fc=websiteGroup:HHS\+News\+Releases(.*)',
                'detailRules':[
                ]
            },
            {
                'rule':r'(.*)/3926/\*/https://www\.hhs\.gov/about/news(.*)',
                'detailRules':[
                     {
                        'rule':r'(.*)/3926/20170127190303/(.*)/about/news(.*)',
                        'content':r'//*[@id="site-content"]//*[contains(@class,"content")]',
                        'title':r'//*[contains(@class,"news-header")]/h1',
                        'publish':[
                            # {
                            #     'rule':'//*[@id="block-system-main"]//*[contains(@class,"date-display-single") and @content]/@content',
                            #     'format':'%Y-%m-%dT%H:%M:%S-05:00'
                            # },
                            {
                                'rule':'//*[@id="site-content"]//*[contains(@class,"content")]//*[contains(@class,"left")]/b/text()[2]',
                                'format':'%B %d, %Y'
                            }
                        ],
                    },

                ]
            },
            {
                'rule':r'(.*)blog/index\.html(\?page=[0-9]+)?(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/blog/[0-9]+/[0-9]+/[0-9]+/(.*)',
                        'content':r'//*[@id="block-system-main"]',
                        'title':r'//*[@id="block-system-main"]/div/h1',
                        'publish':[
                            {
                                'rule':'//*[@id="block-system-main"]//*[contains(@class,"date-display-single") and @content]/@content',
                                'format':'%Y-%m-%dT%H:%M:%S-05:00'
                            },
                            {
                                'rule':'//*[@id="block-system-main"]//*[contains(@class,"date-display-single") and @content]/@content',
                                'format':'%Y-%m-%dT%H:%M:%S-04:00'
                            },
                            # {
                            #     'rule':'//*[@id="site-content"]//*[contains(@class,"content")]//*[contains(@class,"left")]/b/text()[2]',
                            #     'format':'%B %d, %Y'
                            # }
                        ],
                    },
                ]
            },
            {
                'rule':r'((?!8315).)*/blog/archive/[0-9]{4}(.*)',
                'detailRules':[
                    {
                        'rule':r'((?!8315).)*/blog/[0-9]+/[0-9]+/[0-9]+/(.*)',
                        'content':r'//*[@id="block-system-main"]',
                        'title':r'//*[@id="block-system-main"]/div/h1',
                        'publish':[
                            {
                                'rule':'//*[@id="block-system-main"]//*[contains(@class,"date-display-single") and @content]/@content',
                                'format':'%Y-%m-%dT%H:%M:%S-05:00'
                            },
                            {
                                'rule':'//*[@id="block-system-main"]//*[contains(@class,"date-display-single") and @content]/@content',
                                'format':'%Y-%m-%dT%H:%M:%S-04:00'
                            },
                            # {
                            #     'rule':'//*[@id="site-content"]//*[contains(@class,"content")]//*[contains(@class,"left")]/b/text()[2]',
                            #     'format':'%B %d, %Y'
                            # }
                        ],
                    },
                ]
            },
            {
                'rule':r'(.*)8315/[0-9]+/(.*)/https://www\.hhs\.gov/blog/archive(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)8315/[0-9]+/(.*)/blog/[0-9]+/[0-9]+/[0-9]+/(.*)',
                        'content':r'//*[@id="block-system-main"]',
                        'title':r'//*[@id="block-system-main"]/div/h1',
                        'publish':[
                            {
                                'rule':'//*[@id="block-system-main"]//*[contains(@class,"date-display-single") and @content]/@content',
                                'format':'%Y-%m-%dT%H:%M:%S-05:00'
                            },
                            # {
                            #     'rule':'//*[@id="site-content"]//*[contains(@class,"content")]//*[contains(@class,"left")]/b/text()[2]',
                            #     'format':'%B %d, %Y'
                            # }
                        ],
                    },
                ]
            },
        ]
    },
    ## 加拿大 数量大 已更新
    'ca':{
        'allowed_domains':['canada.ca','healthycanadians.gc.ca'],
        'site_url':'',
        'start_urls':[
            'https://www.canada.ca/en/services/health.html',
            'https://www.canada.ca/en/services/health/publications.html',
            'https://www.canada.ca/en/public-health.html',
            'https://www.canada.ca/en/news.html',


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
        ],
        'listRules':[
            {
                'rule':r'(.*)en/services/health/publications(\.html)|(/(.*)\.html)',
                'detailRules':[
                    {
                        'rule':r'(.*)/en/(health-canada|public-health)/services/((?!\.html).)*/(.*)',
                        'content':r'//main[@property="mainContentOfPage"]',
                        'title':r'//*[@id="wb-cont"]',
                        'publish':[
                            {
                                'rule':'//*[@id="wb-dtmd"]//*[contains(@property,"dateModified")]/text()',
                                'format':'%Y-%m-%d'
                            }
                        ],

                    }
                ]
            },
            {
                'rule':r'(.*)en/news\.html(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/en/(.*)/[0-9]+/[0-9]+/.*\.html',
                        'content':r'//*[@id="news-release-container"]',
                        'title':r'//*[@id="wb-cont"]',
                        'publish':[
                            {
                                'rule':'//*[@id="wb-dtmd"]//*[contains(@property,"dateModified")]/text()',
                                'format':'%Y-%m-%d'
                            }
                        ],

                    }
                ]
            }
        ]
        
    },
    ## 墨西哥（没有下全,附件太多应该过滤掉) 通过
    'mx':{
        'allowed_domains':['gob.mx'],
        'site_url':'https://www.gob.mx',
        'start_urls':[
            # 'https://www.gob.mx/salud/en',
            # 'https://www.gob.mx/salud/en/archivo/articulos',
            # 'https://www.gob.mx/salud/en/archivo/prensa',
            # 'https://www.gob.mx/salud/en/archivo/documentos',
            # 'https://www.gob.mx/temas/archivo/galerias/influenza',
            'https://www.gob.mx/salud/archivo/prensa?idiom=en',
            'https://www.gob.mx/salud/en/archivo/articulos',



        ],
        'rules':[
            # r'(.*)/salud/archivo/articulos(.*)',
            # r'(.*)/salud/en/archivo/prensa(.*)',
            # r'(.*)/salud/en/prensa(.*)',
            # r'(.*)salud/en/articulos(.*)',
            # r'(.*)/salud/en/archivo/documentos(.*)',
            # r'(.*)/salud/acciones-y-programas/personal-de-la-salud(.*)',
            # r'(.*)/senasica(.*)',
            # r'(.*)/salud/acciones-y-programas(.*)',
            # r'(.*)/temas/archivo/galerias/influenza(.*)',
            # r'(.*)/salud/censia/galerias(.*)'
            r'(.*)/salud/archivo/prensa\?idiom=en(.*)',
            r'(.*)/salud/en/prensa/(.*)',
            r'(.*)salud/en/archivo/articulos\?idiom=en(.*)',
            r'(.*)/salud/en/articulos/(.*)',


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
    ## 危地马拉 (没有下全)
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
    ## 牙买加 通过 en
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
    ## 特立尼达和多巴哥 时间解析过于不鲁棒 通过 en
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
    ## 巴哈马 没有卫生部网站
    'bs':{
        # 'allowed_domains':['gov.bs'],
        # 'site_url':'http://www.bahamas.gov.bs',
        # 'start_urls':[
        #     'http://www.bahamas.gov.bs/health'
        # ],
        # 'rules':[

        # ],

    },

    ## 伯利兹 通过 en
    'bz':{
        'allowed_domains':['belize.gov.bz'],
        'site_url':'http://www.belize.gov.bz',
        'start_urls':[
            'http://www.belize.gov.bz/index.php/ministry-of-health'
        ],
        'rules':[
  
        ],
        'publish':[

        ]


    },
    ## 尼加瓜拉 通过 内容多需要精细化过滤 es
    'ni':{
        'allowed_domains':['minsa.gob.ni'],
        'site_url':'http://www.minsa.gob.ni',
        'start_urls':[
            'http://www.minsa.gob.ni/index.php',

        ],
        'language':'es',
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

    ## 巴拿马 通过 es 文件多
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
        'language':'es',
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


    ## 安提瓜和巴布达 通过 en
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
    ## 巴巴多斯 通过 en
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
    ## 格林纳达 通过 en
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
    ## 圣文森特和格林纳丁斯 通过 en
    'vc':{
        'allowed_domains':['moh.gov.vc'],
        'site_url':'http://moh.gov.vc',
        'start_urls':[
            'http://moh.gov.vc/health/index.php',
        ],
        'rules':[
            r'(.*)/health/index\.php(.*)',

        ]
    },

    ###############################################
    # 南美洲
    ###############################################

    ## 哥伦比亚 通过 es 样式有点乱v
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

    # 苏里南 通过 en
    'sr':{
        'allowed_domains':['www.gov.sr'],
        'site_url':'http://www.gov.sr',
        'start_urls':['http://www.gov.sr/ministerie-van-volksgezondheid/publicaties.aspx'],
        'rules':[r'(.*)/ministerie-van-volksgezondheid/publicaties(.*)'],
        'publish':[]
    },

     # 秘鲁 通过 es
    'pe':{
        'allowed_domains':['minsa.gob.pe'],
        'site_url':'http://www.minsa.gob.pe',
        'start_urls':[
            'http://www.minsa.gob.pe',
            'http://www.minsa.gob.pe/index.asp\?op=5',
            'http://www.minsa.gob.pe/portalweb/02estadistica/estadistica_1.asp?sub5=2',
            'http://www.minsa.gob.pe/portalweb/index_est03.asp?box=4',
            'http://www.minsa.gob.pe/portalweb/index_pro03.asp?box=1',

        ],
        'language':'es',
        'rules':[
            r'(.*)/portalweb/02estadistica/(.*)',
            r'(.*)/estadisticas/estadisticas(.*)',
            r'(.*)/portalweb/07profesionales(.*)',
            r'(.*)/index\.asp\?op=5(.*)',
            r'(.*)/index\.asp\?op=51(.*)',

        ],
        'publish':[
            {
                'rule':'//div[contains(@class,"fecha")]/text()',
                'format':'%Y-%m-%d',
                'extra':pe_time_sub,
            },
        ]
    },
    
    # 玻利维亚 打不开
    'bo':{
        'allowed_domains':['sns.gov.bo'],
        'site_url':'http://www.sns.gov.bo',
        'start_urls':[],
        'rules':[]    
    },
    ## 巴拉圭 (样式有问题,内容过多需要精细化处理) es digges多
    'py':{
        'allowed_domains':['mspbs.gov.py'],
        'site_url':'https://www.mspbs.gov.py',
        'start_urls':[
            'https://www.mspbs.gov.py',
            'https://www.mspbs.gov.py/portal',
            'https://www.mspbs.gov.py/dgtic',
            'https://www.mspbs.gov.py/dnerhs',
            'http://www.mspbs.gov.py/rrhh','https://www.mspbs.gov.py/dnvs','https://www.mspbs.gov.py/planificacion',
            'http://www.mspbs.gov.py/dggies','https://www.mspbs.gov.py/dgrrii','https://www.mspbs.gov.py/drcps',
        ],
        'language':'es',
        'rules':[
            r'(.*)/portal/(.*)',r'(.*)/digies(.*)',r'(.*)/dgtic(.*)',r'(.*)/dnerhs(.*)',r'(.*)/rrhh(.*)',
            r'(.*)/dnvs(.*)',r'(.*)/planificacion(.*)',r'(.*)/dggies(.*)',r'(.*)/dgrrii(.*)',r'(.*)/drcps(.*)',  
        ],
    },

    # 巴西 (部分样式乱,内容过多需要精细化处理) en 博客多 已更新
    'br':{
        'allowed_domains':['saude.gov.br'],
        'site_url':'http://portalms.saude.gov.br',
        'start_urls':[
            'http://portalms.saude.gov.br',
            'http://portalms.saude.gov.br/noticias',
            'http://www.blog.saude.gov.br',
            'http://www.blog.saude.gov.br/promocao-da-saude'
        ],
        'language':'en',
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
        ],
        'listRules':[
            {
                'rule':r'(.*)/noticias(/)?(\?start=[0-9]+(.*))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/noticias/agencia-saude/(.*)',
                        'content':r'//*[@id="content-section"]//*[contains(@class,"item-page")]',
                        'title':r'//*[@id="content-section"]//*[contains(@class,"documentFirstHeading")]',
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
                        ],
                    }
                ]
            },
            {
                'rule':r'(.*)/blog\.saude\.gov\.br/index\.php(/)?(\?start=[0-9]+(.*))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/blog\.saude\.gov\.br/index\.php/\w+/[0-9]+-\w+',
                        'content':r'//*[@id="content-section"]//*[contains(@class,"item-page")]',
                        'title':r'//*[@id="content-section"]//*[contains(@class,"secondaryHeading")]',
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
                        ],
                    }
                ]
            }
        ]
          
        
    },

    # 智利 scrapy all thing 通过 首页文件多 es 已更新
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
        'language':'es',
        'exludes':[],
        'listRules':[
            {
                'rule':r'(.*)category/noticias(/)?(/page/[0-9]+(.*))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)www\.deis\.cl/[^\?/]+(/)?$',
                        'content':r'//*[@id="content"]//*[contains(@class,"body")]',
                        'title':r'//*[@id="content"]/article/header/*[contains(@class,"title")]',
                    }
                ]
            }
        ]

    },

    # 阿根廷 新旧页面一起出现 需要翻墙 es 通过 notics过多 已更新
    'ar':{
        'allowed_domains':['argentina.gob.ar','msal.gob.ar'],
        'site_url':'http://www.msal.gob.ar',
        'start_urls':[
            'https://www.argentina.gob.ar/salud',
            'http://www.msal.gob.ar/prensa',
            'http://www.msal.gob.ar/prensa/index.php',
            'http://www.msal.gob.ar/index.php?option=com_ryc_contenidos',
        ],
        'rules':[
            r'(.*)/salud/noticias(.*)',
            r'(.*)/prensa/index\.php(.*)',
            r'(.*)/noticias(.*)',

            r'(.*)/index\.php\?option=com_ryc_contenidos(.*)',
            r'(.*)index\.php/component/ryc_contenidos(.*)',

            r'(.*)index\.php\?option=com_bes_contenidos(.*)',
            r'(.*)index\.php/component/bes_contenidos(.*)',

            r'(.*)/salud/epidemiologiaysituacion(.*)',
            r'(.*)/salud/direccionesprogramasplanes(.*)',
            r'(.*)/salud(.*)', 
        ],
        'language':'es',
        'publish':[
            {
                'rule':'//*[@id="page"]/p[1]/span/text()',
                'format':'%Y-%m-%d %H:%M',
                'extra':ar_time_sub,
            },
            {
                'rule':'//*[@id="block-system-main"]//time[contains(@class,"text-muted")]/text()',
                'format':'%Y-%m-%d',
                'extra':ar_time_sub2,
            }
        ],
        'listRules':[
            {
                'rule':r'(.*)/salud/noticias(/)?(\?page=[0-9](.*))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/noticias/[^\?]+',
                        'content':r'//*[@id="block-system-main"]/article/section',
                        'title':r'//*[@id="block-system-main"]/article/header//*[contains(@class,"title-description")]',
                        'publish':[
                             {
                                'rule':r'//*[@id="block-system-main"]//time[contains(@class,"text-muted")]/text()',
                                'format':'%Y-%m-%d',
                                'extra':ar_time_sub2,
                            },
                            {
                                'rule':r'//*[@id="page"]/p[1]/span/text()',
                                'format':'%Y-%m-%d %H:%M',
                                'extra':ar_time_sub,
                            } 
                        ],
                    }
                ]
            },
            {
                'rule':r'(.*)/prensa/index\.php(/noticias-de-la-semana|/)?(\?start=[0-9]+(.*))?$',
                'detailRules':[
                    {
                        'rule':r'(.*)/prensa/index\.php/noticias-de-la-semana/[^\?]+',
                        'content':r'//*[@id="page"]',
                        'title':r'//*[@id="page"]/*[contains(@class,"contentheading_ultimasNoticias")]',
                        'publish':[
                            {
                                'rule':r'//*[@id="page"]/p[1]/span/text()',
                                'format':'%Y-%m-%d %H:%M',
                                'extra':ar_time_sub,
                            },
                            {
                                'rule':r'//*[@id="block-system-main"]//time[contains(@class,"text-muted")]/text()',
                                'format':'%Y-%m-%d',
                                'extra':ar_time_sub2,
                            },
                            
                        ],
                    }
                ]
            },
            {
                'rule':r'(.*)index\.php\?option=com_bes_contenidos(/)?(\?start=[0-9]+(.*))?$',
                'detailRules':[
                ]
            },
            {
                'rule':r'(.*)index\.php\?option=com_ryc_contenidos(/)?(\?start=[0-9]+(.*))?$',
                'detailRules':[
                ]
            },

            
        ]
    },

    # 乌拉圭 通过 es
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

    # 新西兰 通过 过大 en 已更新
    'nz':{
        'allowed_domains':['health.govt.nz'],
        'site_url':'http://www.health.govt.nz',
        'start_urls':[
            'http://www.health.govt.nz',
            'http://www.health.govt.nz/nz-health-statistics',
            'http://www.health.govt.nz/publications'
        ],
        'rules':[
            r'(.*?)/nz-health-statistics(.*)',
            r'(.*?)/publications(/{0,1})\?page=([0-9]{1,2})',

            r'(.*)/publication/(.*)',
            r'(.*)/publication\?page=(.*)'
        ],
        'excludes':[
            r'(.*)/publication(.*)#find-by-region(.*)',
        ],
        'publish':[
            {
                'rule':'//article//*[contains(@class,"date-display-single")]/@content',
                'format':'%Y-%m-%dT%H:%M:%S+13:00'
            },
        ],
        'listRules':[
            {
                'rule':r'(.*?)/nz-health-statistics(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/publication/(.*)',
                        'content':r'//*[@id="block-system-main"]//article[contains(@id,"node")]',
                        'title':r'//*[@id="block-system-main"]//*[contains(@class,"pane-content")][1]/h1',
                        'publish':[
                            {
                                'rule':'//article//*[contains(@class,"date-display-single")]/@content',
                                'format':'%Y-%m-%dT%H:%M:%S+13:00'
                            },
                        ],
                    }
                ]
            },
            {
                'rule':r'(.*?)/publications(\?page=[0-9]+)?(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/publication/(.*)',
                        'content':r'//*[@id="block-system-main"]//article[@id="node-*"]',
                        'title':r'//*[@id="block-system-main"]//*[contains(@class,"pane-content")][1]/h1',
                        'publish':[
                            {
                                'rule':'//article//*[contains(@class,"date-display-single")]/@content',
                                'format':'%Y-%m-%dT%H:%M:%S+13:00'
                            },
                        ],
                    }
                ]
            }
        ]
    },
    # 斐济群岛 通过 en 已更新
    'fj':{
        'allowed_domains':['health.gov.fj'],
        'site_url':['http://www.health.gov.fj'],
        'start_urls':['http://www.health.gov.fj','http://www.health.gov.fj/?page_id=198'],
        'rules':[],
        'listRules':[]
    },

    # 澳大利亚 需要过滤的文件过多 en 已更新
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
            r'(.*)/internet/main/publishing\.nsf/Content/Aboriginal\+and\+Torres\+Strait\+Islander\+Health-1lp(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/health-ethics-index\.htm(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/health-care-homes(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/Healthcare\+systems-1(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/health-medicarebenefits-index\.htm(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/Mental\+Health\+and\+Wellbeing-1(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/national-mens-and-womens-health-1(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/National-Rural-Health-Commissioner(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/norfolk-is(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/palliative-care-and-end-of-life-care(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/consumer-pharmacy(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/primarycare(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/regulation-and-red-tape-reduction(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/Rural\+Health-1(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/Services-1(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/healthiermedicare(.*)',
            ## For Health Professionals
            r'(.*)/internet/main/publishing\.nsf/Content/health-compliance(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/Health\+products\+and\+medicines-2(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/Health\+Workforce-2(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/health-care-homes-professional(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/national-mens-and-womens-health-2(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/Healthcare\+systems-2(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/Rural\+Health-1(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/Services-2(.*)', 
            r'(.*)/internet/main/publishing\.nsf/Content/strongmedicare(.*)',
            ## About us
            r'(.*)/internet/main/publishing\.nsf/Content/health-overview\.htm(.*)',
            r'(.*)/internet/main/publishing\.nsf/Content/health-central\.htm(.*)',
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
            r'(.*)/internet/main/publishing\.nsf/Content/health-history\.htm(.*)',

            ## 过滤掉分类查询的
             
        ],
        'publish':[
            {
                'rule':'//*[@id="read"]//*[contains(@class,"publish-date")]/text()',
                'format':'%Y-%B-%d',
                'extra':au_time_sub,
            },
        ],
        'listRules':[
            {
                'rule':r'(.*)/internet/main/publishing\.nsf/Content/(?!.*\.htm)',
                'detailRules':[
                    {
                        'rule':r'(.*)/internet/main/publishing\.nsf/Content/(.*)',
                        'content':r'//*[@id="read"]',
                        'title':r'//*[@id="read"]/div[1]/div/h1',
                        'publish':[
                            {
                                'rule':'//*[@id="read"]//*[contains(@class,"publish-date")]/text()',
                                'format':'%Y-%B-%d',
                                'extra':au_time_sub,
                            },
                        ],
                    }
                ]
            }
        ]
        
    },

    # 巴布亚新几内亚 通过 en 已更新
    'pg':{
        'allowed_domains':['health.gov.pg'],
        'site_url':'http://www.health.gov.pg',
        'start_urls':[
            'http://www.health.gov.pg',
            'http://www.health.gov.pg/pages/healthpolicyA.htm',
            'http://www.health.gov.pg/pages/healthpolicyD.htm',
            'http://www.health.gov.pg/pages/healthpolicyH.htm',
            'http://www.health.gov.pg/pages/healthpolicyM.htm',
            'http://www.health.gov.pg/pages/healthpolicyP.htm'
        ],
        'rules':[],
        'listRules':[],
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

    # 基里巴斯 通过 en 已更新
    'ki':{
        'allowed_domains':['health.gov.ki'],
        'site_url':'http://health.gov.ki',
        'start_urls':[
            'http://www.health.gov.ki/download.html',
            'http://www.health.gov.ki/health-news.html',
            'http://www.health.gov.ki/documents.html',
            'http://www.health.gov.ki/iec-materials.html',
            'http://www.health.gov.ki/forms.html'
        ],
        'rules':[r'(.*)/download/category/(.*)',r'(.*)/health-news/(.*)'],
        'listRules':[
            {
                'rule':r'(.*)/health-news\.html(.*)',
                'detailRules':[
                    {
                        'rule':r'(.*)/health-news/(.*)',
                        'content':r'//*[@id="main"]',
                        'title':r'//*[@id="main"]/*[contains(@class,"item-page")]/h2',
                        'publish':[]
                    }
                ]
            },
            {
                'rule':r'(.*)/download/category/(.*)',
                'detailRules':[
                ]
            }
        ]
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

    # 汤加 通过 en 已更新
    'to':{
        'allowed_domains':['health.gov.to'],
        'site_url':'http://health.gov.to',
        'start_urls':['http://www.health.gov.to/drupal/?q=node/26','http://www.health.gov.to/drupal/?q=Annual','http://www.health.gov.to/drupal/sites/default/files/MOH%20Corporate%20Plan%202008-2012.pdf','http://www.health.gov.to/drupal/sites/default/files/Tongan%20Registered%20List%20of%20Medicinal%20%20Drugs%20Final%20-%20MARCH%202016.xlsx'],
        'rules':[r'(.*)/drupal/sites/default/file(.*)'],
        'listRules':[
        ]
    },

    # 萨摩亚 通过 en 已更新
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
                'rule':'//*[@id="sp-component"]//*[contains(@class,"article-info")]//time[@datetime]/@datetime',
                'format':'%Y-%m-%dT%H:%M:%S+14:00'
            }
        ],
        'listRules':[
            {
                'rule':r'(.*)/health-warning-alerts/general-health-advisory(.*)$',
                'detailRules':[
                    {
                        'rule':r'(.*)/component/content/article(.*)',
                        'content':r'//*[@id="sp-component"]//*[contains(@class,"article-body")]',
                        'title':r'//*[@id="sp-component"]//article//*[@itemprop="name"]',
                        'publish':[
                            {
                                'rule':'//*[@id="sp-component"]//*[contains(@class,"article-info")]//time[@datetime]/@datetime',
                                'format':'%Y-%m-%dT%H:%M:%S+14:00'
                            }
                        ],
                    }
                ]
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
