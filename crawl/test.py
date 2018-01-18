# !bin/python
# -*- coding: utf-8 -*-
import requests
import html2text
import codecs
from lxml import etree
import sys
# try:
#     reload(sys)
#     sys.setdefaultencoding('utf-8')
# except:
#     pass

# r = requests.get("https://www.valitsus.ee/en/news/european-council-stresses-implementation-minsk-agreements-russias-responsibility")
# p = r'//*[@id="block-system-main"]'
# html = r.text 
# selector = etree.HTML(html)
# ele = selector.xpath(p)[0]
# text = etree.tostring(ele)

# text_maker = html2text.HTML2Text()
# text_maker.ignore_links = True
# text_maker.skip_internal_links = True
# text_maker.bypass_tables = False
# text_maker.ignore_images = True
# t = text_maker.handle(text)
# with codecs.open('text.txt','w','utf-8') as f:
#     f.write(t)

# headers = {
#     'X-AA-Challenge-ID':"32973750",
# 	'X-AA-Challenge-Result':"-1133695143",
# 	'X-AA-Challenge':"377890",
# 	'Content-Type':'text/plain'
# }

r = requests.get('http://www.salute.gov.it/portale/news/p3_2_1_1_1.jsp?lingua=italiano&menu=notizie&p=dalministero&id=3245')



with codecs.open('it.html','w','utf-8') as f:
    f.write(r.text)

a = {

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

}

