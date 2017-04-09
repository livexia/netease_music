# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NeteaseMusicListItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    num = scrapy.Field()
    title = scrapy.Field()
    length = scrapy.Field()
    author = scrapy.Field()
    album = scrapy.Field()
    pass

class NeteaseMusicItem(scrapy.Item):
    num = scrapy.Field()
    title = scrapy.Field()
    length = scrapy.Field()
    author = scrapy.Field()
    album = scrapy.Field()
    pass
