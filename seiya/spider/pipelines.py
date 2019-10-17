# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
from seiya.db.base import DataAnalysis, JobModel, HouseModel
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import re

engine = create_engine('mysql+mysqldb://root:123456@localhost:3306/seiya?charset=utf8')

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
        
        return item

    def open_spider(self, spider):
        Session = sessionmaker(bind=engine)
        self.session = Session()

    def close_spider(self, spider):
        self.session.commit()
        self.session.close()
