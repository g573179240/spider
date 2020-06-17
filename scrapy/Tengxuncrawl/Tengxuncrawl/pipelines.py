# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class TengxuncrawlPipeline(object):
    def process_item(self, item, spider):
        print("=================")
        print(item["zhName"])
        print(item["zhLink"])
        print(item["zhType"])
        print(item["zhNum"])
        print(item["zhAddress"])
        print(item["zhTime"])
        print("=================")

        return item
