# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy

class TengxunItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # 职位名称
    zhName = scrapy.Field()
    zhJob = scrapy.Field()
    zhType = scrapy.Field()
    zhAddress = scrapy.Field()
    zhTime = scrapy.Field()






