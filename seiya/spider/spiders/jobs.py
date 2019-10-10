# -*- coding: utf-8 -*-
import scrapy
from seiya.spider.items import JobsItem
import re

class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['lagou.com']
    start_urls = ['http://www.lagou.com/zhaopin/{}'.format(x) for x in range(1,2)]

    def parse(self, response):
        for job in response.css('ul.item_con_list li'):
            experience = re.findall('\d+-\d+', job.xpath('.//div[@class="li_b_l"]/text()').extract()[2].split('/')[0].strip())
            if len(experience) > 0:
                experience_lower, experience_upper = experience[0].split('-')
            else:
                experience_lower = 0
                experience_upper = 0
            item = JobsItem({
                'title' : job.xpath('.//h3/text()').extract_first().strip(),
                'city' : job.xpath('.//em/text()').extract_first().split('·')[0].strip(),
                'salary_lower' : job.xpath('.//span[@class="money"]/text()').extract_first().split('-')[0].strip(),
                'salary_upper' : job.xpath('.//span[@class="money"]/text()').extract_first().split('-')[1].strip(),
                'experience_lower' : experience_lower,
                'experience_upper' : experience_upper,
                'education' : job.xpath('.//div[@class="li_b_l"]/text()').extract()[2].split('/')[1].strip(),
                'tags' : ' '.join(job.xpath('.//div[@class="list_item_bot"]/div[@class="li_b_l"]/span/text()').extract()),
                'company' : job.xpath('.//div[@class="company_name"]/a/text()').extract_first().strip()
            })
            yield item

