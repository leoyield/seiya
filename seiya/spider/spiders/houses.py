# -*- coding: utf-8 -*-
import scrapy
from seiya.spider.items import HousesItem
import re


class HousesSpider(scrapy.Spider):
    name = 'houses'
    allowed_domains = ['gy.lianjia.com']
    start_urls = ['https://gy.lianjia.com/zufang/pg{}rt200600000001/'.format(x) for x in range(1,31)]

    def parse(self, response):
        for house in response.css('div.content__list--item'):
            item = HousesItem({
                'title' : house.xpath('.//p[contains(@class, "content__list--item--title twoline")]/a/text()').extract_first().strip(),
                'region' : house.xpath('.//p[@class="content__list--item--des"]/a/text()').extract()[0].strip(),
                'street' : house.xpath('.//p[@class="content__list--item--des"]/a/text()').extract()[1].strip(),
                'community' : house.xpath('.//p[@class="content__list--item--des"]/a/text()').extract()[2].strip(),
                'area' : re.findall('\d+', house.xpath('.//p[@class="content__list--item--des"]/text()').extract()[4].strip())[0],
                'direction' : house.xpath('.//p[@class="content__list--item--des"]/text()').extract()[5].strip(),
                'house_type' : house.xpath('.//p[@class="content__list--item--des"]/text()').extract()[6].strip(),
                'floor' : house.xpath('.//p[@class="content__list--item--des"]/span/text()').extract()[1].strip().split()[0],
                'building_height' : re.findall('\d+', house.xpath('.//p[@class="content__list--item--des"]/span/text()').extract()[1].strip().split()[1])[0],
                'tags' : ' '.join(house.xpath('.//p[contains(@class,"content__list--item--bottom oneline")]/i/text()').extract()),
                'price' : house.xpath('.//span[@class="content__list--item-price"]/em/text()').extract_first().strip()
            })
            yield item
