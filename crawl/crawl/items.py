 # -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field

class ResourceItem(scrapy.Item):
     url = Field()
     md5 = Field()
     content = Field()
     type = Field()
     location = Field()
     title = Field()
     local_url = Field()
     language = Field()
     publish = Field()
     nation = Field()
     keywords = Field()

     def __repr__(self):
         return repr({"url": self['url']})

     def __str__(self):
         return str({"url": self['url']})

    


