# -*- coding: utf-8 -*-
import scrapy
# 导入链接规则匹配类,用来提取符合规则的链接
from scrapy.linkextractors import LinkExtractor
# 导入spiers的派生类CrawlSpider,Rule指定特定操作
from scrapy.spiders import CrawlSpider, Rule
from Tengxuncrawl.items import TengxuncrawlItem

class TengxunSpider(CrawlSpider):
    name = 'tengxun'
    allowed_domains = ['hr.tencent.com']
    # 指定第1页的URL,后续不用拼接
    start_urls = ['https://hr.tencent.com/position.php?start=0']
   # 使用LinkExtractor,提取页面中的所有link
        # 每个职位的链接规则
        #用xpaht匹配需要的link
        link = LinkExtractor(restrict_xpaths='//ul[@class="cont_xiaoqu"]/li')
        #用allow接收一个正则表达式或正则表达式列表
        link = LinkExtractor(allow=r'start=\d+')
        # 获取的links是一个列表
        links = zhLink.extract_links(response)
        for link in links:
            print(link.url,link.text)
       
        rules = (
                # 对每个职位发起请求,调用parsZh解析
                Rule(link,callback='parseHtml',follow=True)
                )

    def parseHtml(self,response):
        # 每个职位的节点对象列表
        baseList = response.xpath('//tr[@class="odd"] | //tr[@class="even"]')
        for base in baseList:
            item = TengxuncrawlItem()
            item["zhName"] = base.xpath('./td[1]/a/text()').extract()[0]
            # 链接
            item["zhLink"] = base.xpath('./td[1]/a/@href').extract()[0]
            
            # 类别
            item["zhType"] = base.xpath('./td[2]/text()').extract()
            if item["zhType"]:
                item["zhType"] = item["zhType"][0]
            else:
                item["zhType"] = "无"

            # 人数
            item["zhNum"] = base.xpath('./td[3]/text()').extract()[0]
            # 地点
            item["zhAddress"]= base.xpath('./td[4]/text()').extract()[0]
            # 时间
            item["zhTime"] = base.xpath('./td[5]/text()').extract()[0]

            yield item

    def parseZh(self,response):
        # 职位页面的解析函数
        pass