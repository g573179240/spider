from selenium import webdriver
from lxml import etree
import csv
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("https://www.douyu.com/directory/all")


class DouyuSpider:
    def __init__(self):
        self.n = 0
        self.page = 1

    #循环遍历的获取数据
    def getData1(self):
        parseHtml = etree.HTML(driver.page_source)
        info_list = parseHtml.xpath('//li[@class="layout-Cover-item"]/div/a/div[2]/div[2]')
        for info in info_list:
            name = info.xpath('./h2/text()')
            number = info.xpath('./span/text()')
            #获取拼接的name和number列表
            L = name + number 
            self.writeData(L)
            self.n += 1
    #单独匹配每个获得
    def getData2(self):
        parseHtml = etree.HTML(driver.page_source)
        names = parseHtml.xpath('//li[@class="layout-Cover-item"]/div/a/div[2]/div[2]/h2')
        numbers = parseHtml.xpath('//li[@class="layout-Cover-item"]/div/a/div[2]/div[2]/span')
        for name,number in zip(names,numbers):
            L = [name.strip(),number.strip()]
            self.writeData(L)
            self.n += 1

    def writeData(self,L):
        with open("G:\\spyder\\斗鱼直播.csv",'a',newline="",encoding='gb18030') as f:
            writer = csv.writer(f)
            writer.writerow(L)

    def workOn(self):
        self.getData1()
        print("第%d页爬取成功"%self.page) 
        while True:
            pn = input("继续爬取请按y,退出请按q:")
            if pn.strip().lower() == 'y':
                driver.find_element_by_xpath('//ul[@class="dy-Pagination ListPagination"]//li[@title="下一页"]/span').click()
                self.getData1()
                self.page += 1
                print("第%d页爬取成功"%self.page) 
            else:
                break


if __name__ == "__main__":
    spider = DouyuSpider()
    spider.workOn()