# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
from seiya.db.base import db, DataAnalysis, JobModel

class SpiderPipeline(object):
    def process_item(self, item, spider):
        item['salary_lower'] = int(item['salary_lower'])
        item['salary_upper'] = int(item['salary_upper'])
        item['experience_lower'] = int(item['experience_lower'])
        item['experience_upper'] = int(item['experience_upper'])
        db.session.add(JobModel(**item))
        return item

    def close_spider(self, spider):
        db.session.commit()
