# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

# 导入scrapy定义好的图片管道类
from scrapy.pipelines.images import ImagesPipeline
import scrapy

class DouyuImagePipeline(ImagesPipeline):
    # 此方法名不能变
    def get_media_requests(self,item,info):
        # 1.获取图片链接
        imageLink = item["imgLink"]
        # 2.向图片链接发请求,响应会保存在settings.py中
        #   的 IMAGES_STORE 路径中
        yield scrapy.Request(imageLink)













class DouyuPipeline(object):
    def process_item(self, item, spider):
        return item


