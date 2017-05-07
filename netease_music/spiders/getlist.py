# -*- coding: utf-8 -*-

import scrapy
from netease_music.items import NeteaseMusicItem
from scrapy_splash import SplashRequest


class GetListSpider(scrapy.Spider):
    name = "getlist"
    #填入歌单地址url
    start_urls = [
        'http://music.163.com/#/playlist?id=697601210'
    ]
    #http://music.163.com/#/playlist?id=697601210
    #http://music.163.com/api/v3/playlist/detail?id=93043295csrf_token=

    def start_requests(self):
        meta = {
            'splash':{
                'endpoint': 'render.html',
                'args': {
                    'wait': 10,
                    'html': 1,
                    'images': 0,
                    'iframe': 1
                }
            }
        }
        for url in self.start_urls:
            yield SplashRequest(url,self.parse,meta=meta)

    def parse(self, response):
        response
        for song in response.xpath('//ul[@class="f-hide"]'):
            item = NeteaseMusicItem()
            item['title'] = song.xpath('/li/a/text()')
            yield item
