# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class DaomuItem(scrapy.Item):
    # 书名称
    bookName = scrapy.Field()
    # 书标题
    bookTitle = scrapy.Field()
    # 章节数量 
    zhNum = scrapy.Field()
    # 章节名称
    zhName = scrapy.Field()
    # 章节链接
    zhLink = scrapy.Field()
