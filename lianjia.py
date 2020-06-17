#获取二手房数据
import requests
import re
import pymysql
import warnings

class LianjiaSpider:
    def __init__(self):
        self.baseurl = "https://bj.lianjia.com/ershoufang/pg"
        self.headers = {"User-Agent":"Mozilla/5.0"}
        self.page = 1
        self.db = pymysql.connect('localhost','root','123456','lianjia',charset="utf8")
        self.cursor = self.db.cursor()

    def getPage(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        self.parsePage(html)

    def parsePage(self,html):
        p = re.compile('<div class="houseInfo">.*?data-el="region">(.*?)</a>.*?<div class="totalPrice">.*?<span>(.*?)</span>',re.S)
        r_list = p.findall(html)
        self.writeTomysql(r_list)

    def writeTomysql(self,r_list):
        c_db = 'create database if not exists lianjia charset utf8'
        u_db = 'use lianjia'
        c_tab = 'create table if not exists lianjia(\
                id int primary key auto_increment,\
                name varchar(50),\
                price float)charset utf8'
        ins = 'insert into house(name,price) values(%s,%s)'
        warnings.filterwarnings('ignore')
        try:
            self.cursor.execute(c_db)
            self.cursor.execute(u_db)
            self.cursor.execute(c_tab)
        except warnings:
            pass
        for r in r_list:
            L = [r[0].strip(),float(r[1].strip())*10000]
            self.cursor.execute(ins,L)
            self.db.commit()
        print("存入数据成功")

    def workOn(self):
        while True:
            c = input("爬取y,退出q:")
            if c.strip().lower() == 'y':
                url = self.baseurl+str(self.page) + '/'
                self.getPage(url)
                self.page += 1
            else:
                self.cursor.close()
                self.db.close()
                break
if __name__ == '__main__':
    spider = LianjiaSpider()
    spider.workOn()