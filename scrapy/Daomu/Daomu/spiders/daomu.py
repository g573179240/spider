import scrapy
# 从items.py中导入类：DaomuItem
from Daomu.items import DaomuItem

class DaomuSpider(scrapy.Spider):
    # 爬虫名
    name = "daomu"
    # 作用范围
    allowed_domains = ["www.daomubiji.com"]
    # 起始url
    start_urls = ["http://www.daomubiji.com/dao-mu-bi-ji-1"]

    def parse(self,response):
        # 定义item对象
        item = DaomuItem()
        # 书的名称单独匹配(因为只有1个)
        item["bookName"] = response.xpath('//h1[@class="focusbox-title"]/text()').extract()[0]
        # 匹配所有文章的列表
        articles = response.xpath('//article[@class="excerpt excerpt-c3"]/a/text()').extract()
        # articles : ["七星 第一章 钥匙","",""]
        i = 0
        for article in articles:
            info = article.split(" ")
            # info : ["七星","第一章","钥匙"]
            item["bookTitle"] = info[0]
            item["zhNum"] = info[1]
            item["zhName"] = info[2]
            item["zhLink"] = response.xpath\
                    ('//article[@class="excerpt excerpt-c3"]/a/@href').extract()[i]
            i += 1

            yield item







