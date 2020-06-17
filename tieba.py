#获取每个帖子的图片和视频内容
import requests
from lxml import etree
import urllib.parse
import time

class TiebaSpider:
    def __init__(self):
        self.baseurl = "https://tieba.baidu.com/f?"
        self.headers = {"User-Agent":"Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0)"}

    def getTieUrl(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding = 'utf-8'
        html = res.text
        parseHtml = etree.HTML(html)
        t_list = parseHtml.xpath('//div[@class="t_con cleafix"]/div[2]/div/div/a/@href')
        for t_link in t_list:
            t_url = "http://tieba.baidu.com" + t_link
            self.getDataUrl(t_url)

    def getDataUrl(self,t_url):
        res = requests.get(t_url,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        parseHtml = etree.HTML(html)
        data_list = parseHtml.xpath('//div[@class="d_post_content j_d_post_content "]/img/@src | //embed/@data-video')
        for data_link in data_list:
            self.writeData(data_link)

    def writeData(self,data_link):
        res = requests.get(data_link,headers=self.headers)
        res.encoding = 'utf-8'
        html = res.content 
        filename = data_link[-10:]
        with open('G:\\spyder\\%s'%filename,'wb') as f:
            f.write(html)
            time.sleep(0.5)
            print(filename,'下载成功')

    def workOn(self):
        name = input("要爬取的贴吧:")
        begin = int(input("开始页:"))
        end = int(input("结束页:"))
        key = urllib.parse.urlencode({"kw":name})
        for pn in range(begin,end+1):
            pn = (pn-1)*50
            url = self.baseurl + key + '&pn' + str(pn)
            self.getTieUrl(url)
        print("爬取结束")

if __name__ == '__main__':
    spider = TiebaSpider()
    spider.workOn()