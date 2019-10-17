# -*- coding: utf-8 -*-
import scrapy


class RestaurantSpider(scrapy.Spider):
    name = 'restaurant'
    allowed_domains = ['dianping.com']
    start_urls = ['http://www.dianping.com/guiyang/ch10/p{}'.format(x) for x in range(1,31)]

    def parse(self, response):
        for restaurant in response.css(''):
            item = HousesItem({
                'title' : restaurant.xpath('').extract_first().strip(),

            })
            yield item