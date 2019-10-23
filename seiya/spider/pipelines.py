# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
from seiya.db.base import DataAnalysis, JobModel, HouseModel, RestaurantModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from seiya.web.app import config_dict
import re

engine = create_engine(config_dict.get('SQLALCHEMY_DATABASE_URI'))

class SpiderPipeline(object):
    def process_item(self, item, spider):
        if spider.name == 'jobs':
            item['salary_lower'] = int(re.findall('\d+', item['salary_lower'])[0])
            item['salary_upper'] = int(re.findall('\d+', item['salary_upper'])[0])
            item['experience_lower'] = int(item['experience_lower'])
            item['experience_upper'] = int(item['experience_upper'])
            self.session.add(JobModel(**item))
        elif spider.name == 'houses':
            item['area'] = int(item['area'])
            item['building_height'] = int(item['building_height'])
            item['price'] = int(item['price'])
            self.session.add(HouseModel(**item))
        elif spider.name == 'restaurant':
            item['score'] = int(self.to_int(item['score']))
            item['review_count'] = int(self.to_int(item['review_count']))
            item['consumption'] = int(self.to_int(item['consumption']))
            item['taste'] = float(self.to_int(item['taste']))#
            item['ambience'] = float(self.to_int(item['ambience']))
            item['service'] = float(self.to_int(item['service']))
            self.session.add(RestaurantModel(**item))
        self.session.commit()
        return item

    def open_spider(self, spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        
        self.session.close()

    def to_int(self, string):
        if string:
            string = float(re.findall('[\d\.]+', string)[0])
        else:
            string = 0
        return string
