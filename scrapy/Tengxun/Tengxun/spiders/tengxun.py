# -*- coding: utf-8 -*-
import scrapy
from Tengxun.items import TengxunItem


class TengxunSpider(scrapy.Spider):
    name = 'tengxun'
    allowed_domains = ['careers.tencent.com']
    # 定义1个基准的url,方便后期拼接290个URL
    url = "https://careers.tencent.com/search.html?index="
    start = 1
    # 这个start_urls是必须要有的，不能舍弃；
    # 拼接初始的url
    start_urls = [url + str(start)]

    # parse函数是第1次从start_urls中初始URL发请求后
    # 得到响应后必须要调用的函数，第一次必须得走parse函数
    # 后面再走什么可以自己决定，这里决定后面走parseHtml

    # 这里交给的是调度器
    def parse(self, response):
        # 记住最后一页的值
        for i in range(1,3):
            # scrapy.Request()
            # 把290页的URL给调度器入队列,然后出队列给下载器
            # 指定一个回调函数：self.parseHtml(随便写的函数名)
            yield scrapy.Request\
               (self.url + str(i),
                callback=self.parseHtml)

    # 这里交给管道文件
    def parseHtml(self,response):
        # 每个职位的节点对象列表
        baseList = response.xpath('//div[@class="recruit-list"]')
        for base in baseList:
            item = TengxunItem()
            # 使用extract变成文本，里面只有一个元素，所以用[0]拿出来即可
            item["zhName"] = base.xpath('/a/h4/text()').extract()[0]
            # item["zhLink"] = base.xpath('')
            item["zhJob"] = base.xpath('/a/p/span[1]/text()').extract()[0]
            if item["zhJob"]:
                item["zhJob"] = item["zhJob"][0]
            else:
                item["zhJob"] = "无"
            item["zhAddress"] = base.xpath('/a/p/span[2]/text()').extract()[0]
            item["zhType"] = base.xpath('/a/p/span[3]/text()').extract()[0]
            item["zhTime"] = base.xpath('/a/p/span[4]/text()').extract()[0]
            yield item

