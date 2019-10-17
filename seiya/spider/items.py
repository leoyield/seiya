# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class JobsItem(scrapy.Item):
    title = scrapy.Field()
    city = scrapy.Field()
    salary_lower = scrapy.Field()
    salary_upper = scrapy.Field()
    experience_lower = scrapy.Field()
    experience_upper = scrapy.Field()
    education = scrapy.Field()
    tags = scrapy.Field()
    company = scrapy.Field()

class HousesItem(scrapy.Item):
    title = scrapy.Field()
    region = scrapy.Field()
    street = scrapy.Field()
    community = scrapy.Field()
    area = scrapy.Field()
    direction = scrapy.Field()
    house_type = scrapy.Field()
    floor = scrapy.Field()
    building_height = scrapy.Field()
    tags = scrapy.Field()
    price = scrapy.Field()

class SpiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
