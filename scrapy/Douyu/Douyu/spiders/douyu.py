# -*- coding: utf-8 -*-
import scrapy
import json
from Douyu.items import DouyuItem

class DouyuSpider(scrapy.Spider):
    name = 'douyu'
    allowed_domains = ['capi.douyucdn.cn']

    baseUrl = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
    offset = 0

    start_urls = [ baseUrl + str(offset) ]

    def parse(self, response):
        # response为json格式的数据
        # 先把响应转成python数据类型
        nickList = json.loads(response.text)["data"]
        # nickList : [{},{},{}]
        # 如果nickList为空,说明爬取完毕
        if len(nickList) == 0:
            return


        for nick in nickList:
            # nick : {1个主播的详细信息}
            item = DouyuItem()
            item["imgLink"] = nick["vertical_src"]
            item["nickName"] = nick["nickname"]
            item["nickCity"] = nick["anchor_city"]

            yield item

        # 实现翻页功能
        self.offset += 20
        yield scrapy.Request(
            self.baseUrl+str(self.offset),
            callback = self.parse
            )



# {
#     "errorcode":0,
#     "data":[
#         {
#             vertical_src: "https://rpic.douyucdn.cn/live-cover/roomCover/2018/10/31/8edeac935f91eafb7aa90a24a8932598_small.jpg",
#             nickname: "一坨柠檬酱",
#             anchor_city: "成都市"
#         },
#     ]

# }
