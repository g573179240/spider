import requests
import pymysql
import json

class DoubanSpider:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0"}
        self.baseurl = "https://movie.douban.com/j/chart/top_list?"
        self.db = pymysql.connect("localhost","root","123456","douban",charset="utf8")
        self.cursor = self.db.cursor()

    def getPage(self,params):
        res = requests.get(self.baseurl,params=params,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        self.parsePage(html)

    def parsePage(self,html):
        info = json.loads(html)
        for film in info:
            name = film["title"]
            score = float(film["score"].strip())
            exe_list = [name,score]
            self.writePage(exe_list)

    def writePage(self,exe_list):
        ins = 'insert into Film values (%s,%s)'
        self.cursor.execute(ins,exe_list)
        self.db.commit()

    def workOn(self):
        kinds = ['剧情','喜剧','爱情']
        tpList = {
                "剧情":"11",
                "喜剧":"24",
                "爱情":"13"}    
        print("************")
        print("|剧情|喜剧|爱情|")
        print("**************")
        kind = input("请输入电影类型:")
        if kind in kinds:
            number = input("请输入要爬取数量:")
            filmType = tpList[kind]
            params={
                "type":filmType,
                "interval_id":"100:90",
                "action":"",
                "start":"0",
                "limit":number
            }
            self.getPage(params)
            self.cursor.close()
            self.db.close()
        else:
            print("您输入的电影类型不存在")

if __name__ == "__main__":
    spider = DoubanSpider()
    spider.workOn()