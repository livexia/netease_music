# -*- coding: utf-8 -*-

import scrapy
from netease_music.items import NeteaseMusicItem
from selenium import webdriver
from lxml import etree



class GetListSpider(scrapy.Spider):

    name = "getlist"
    #填入歌单地址url
    start_urls = [
        'https://music.163.com/playlist?id=93043295'
    ]

    def parse(self, response):

        # driver = webdriver.PhantomJS()
        # driver.get(self.start_urls)
        # driver.switch_to.frame("g_iframe")
        # html = driver.page_source

        tree = etree.HTML()

        for song in html.xpath('//div[@class="j-flag"]'):
            item = NeteaseMusicItem()
            item['num'] = song.xpath('//td[@class="left"]/span[@class="num"]/text()').extract()
            item['title'] = song.xpath('//div[@class="f-cb"]//text()').extract()
            item['length'] = song.xpath('///div[@class=" s-fc3"]//text()').extract()
            item['author'] = song.xpath('//*[@id="181026421491009155452"]/td[5]/div/a/text()').extract()
            item['album'] = song.xpath('//*[@id="181026421491009155452"]/td[6]/div/a/text()').extract()
            yield item
