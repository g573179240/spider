from selenium import webdriver
import csv
import time

class JingdongSpider:
    def __init__(self):
        opt = webdriver.ChromeOptions()
        opt.set_headless()
        self.driver = webdriver.Chrome(options=opt)

    def getPage(self):
        self.driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        self.parsePage()

    def parsePage(self):
        r_list = self.driver.find_elements_by_xpath('//div[@id="J_goodsList"]//li')
        self.writePage(r_list)

    def writePage(self,r_list):
        for onePro in r_list:
            m = onePro.text.split('\n')
            price = m[0]
            name = m[1]
            commit = m[2]
            market = m[3]
            L = [name,price,commit,market]
            with open("G:\\spyder\\京东商品.csv",'a',newline="",encoding='gb18030') as f:
                writer = csv.writer(f)
                writer.writerow(L)

    def workOn(self):
        pro = input("请输入要爬取的商品:")
        begin = int(input("开始页:"))
        end = int(input("结束页:"))
        self.driver.get("https://www.jd.com/")
        self.driver.find_element_by_class_name("text").send_keys(pro)
        self.driver.find_element_by_class_name("button").click()
        time.sleep(2)
        for i in range(begin,end+1):
            self.getPage()
            self.driver.find_element_by_class_name("pn-next").click()
            if self.driver.page_source.find("pn-next disable") == 1:
                break
        print("爬取结束")
        
if __name__ == "__main__":
    spider = JingdongSpider()
    spider.workOn()