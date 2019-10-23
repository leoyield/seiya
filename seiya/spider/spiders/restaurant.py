# -*- coding: utf-8 -*-
import scrapy
from seiya.spider.items import RestaurantsItem
from scrapy.http import HtmlResponse
import re
from seiya.spider.spiders.woffdict import Woff



class RestaurantSpider(scrapy.Spider):
    name = 'restaurant'
    allowed_domains = ['dianping.com']
    start_urls = ['http://www.dianping.com/guiyang/ch10/p{}'.format(x) for x in range(1,31)]

    def parse(self, response):
        url = response.url
        body = response.text
        this_css = re.findall(r'//s3plus.+?\.css', body)[0]
        woff = Woff(this_css)
        r1 = '<svgmtsi class="shopNum">&#x(....);</svgmtsi>'
        r1r = '<svgmtsi class="shopNum">&#x{};</svgmtsi>'
        r2 = '<svgmtsi class="address">&#x(....);</svgmtsi>'
        r2r = '<svgmtsi class="address">&#x{};</svgmtsi>'
        r3 = '<svgmtsi class="tagName">&#x(....);</svgmtsi>'
        r3r = '<svgmtsi class="tagName">&#x{};</svgmtsi>'
        rep = re.findall(r1, body)
        for i in set(rep):
            try:
                body = body.replace(r1r.format(i), Woff.woff_string[Woff.font1.getGlyphID('uni{}'.format(i))-2])
            except:
                continue
        rep = re.findall(r2, body)
        for i in set(rep):
            try:
                body = body.replace(r2r.format(i), Woff.woff_string[Woff.font2.getGlyphID('uni{}'.format(i))-2])
            except:
                continue
        rep = re.findall(r3, body)
        for i in set(rep):
            try:
                body = body.replace(r3r.format(i), Woff.woff_string[Woff.font3.getGlyphID('uni{}'.format(i))-2])
            except:
                continue
        myresponse = HtmlResponse(url=url, body=body.encode('utf8'))
        for restaurant in myresponse.css('div.shop-list.J_shop-list.shop-all-list ul li'):
            item = RestaurantsItem({
                'title' : restaurant.xpath('.//div[@class="tit"]/a/h4/text()').extract_first().strip(),
                'score' : re.findall('\d+',restaurant.xpath('.//div[@class="comment"]/span/@class').extract_first())[0],
                'review_count' : restaurant.xpath('.//div[@class="comment"]/a[@data-click-name="shop_iwant_review_click"]/b/text()').extract_first(),
                'consumption' : restaurant.xpath('.//div[@class="comment"]/a[@class="mean-price"]/b/text()').extract_first(),
                'classification' : restaurant.xpath('.//div[@class="tag-addr"]/a[@data-click-name="shop_tag_cate_click"]/span[@class="tag"]/text()').extract_first(),
                'business_district' : restaurant.xpath('.//div[@class="tag-addr"]/a[@data-click-name="shop_tag_region_click"]/span[@class="tag"]/text()').extract_first(),
                'taste' : restaurant.xpath('.//span[@class="comment-list"]/span[1]/b/text()').extract_first(),
                'ambience' : restaurant.xpath('.//span[@class="comment-list"]/span[2]/b/text()').extract_first(),
                'service' : restaurant.xpath('.//span[@class="comment-list"]/span[3]/b/text()').extract_first()
            })
            yield item