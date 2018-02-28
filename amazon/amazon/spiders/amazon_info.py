#!/usr/bin/python
#coding:utf-8

from scrapy import Request
from scrapy.spiders import Spider
from amazon.items import AmazonItem
import re



class AmazonSpider(Spider):
    name = 'amazoninfo'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36',
    }

    def start_requests(self):
        #url = 'https://www.amazon.co.uk/s/ref=nb_sb_noss/258-5909564-6278423?url=search-alias%3Daps&field-keywords=iphone+5s+case'
        url = 'https://www.amazon.co.uk/s/ref=nb_sb_ss_i_4_6?url=search-alias%3Daps&field-keywords=iphone+6+case&sprefix=iphone%2Caps%2C408&crid=21QB5X7EUCMBK&rh=i%3Aaps%2Ck%3Aiphone+6+case'

        yield Request(url, headers=self.headers)

    def parse(self, response):
        for i in range(20):
            item = AmazonItem()
            #链接
            link_list = response.xpath('//*[@id="result_%d"]/div/div/div/div[2]/*[@class="a-row a-spacing-small"]/div[1]/a/@href' % i).extract()[0]
            url_1 = 'https://www.amazon.co.uk/dp/'
            try:
                match = re.search(r'%2Fdp%2F(.*)%2Fref%', link_list)
                item['link'] = '%s%s' % (url_1, match.group(1))
            except:
                try:
                    match = re.search(r'/dp/(.*)/ref', link_list)
                    item['link'] = '%s%s' % (url_1, match.group(1))
                except:
                    item['link'] = '------'

            # item['ASIN'] = match.group(1)


            link_url = item['link']
            if link_url != '------':
                yield Request(link_url, meta={'key': item}, callback=self.parse_info)


    def parse_info(self,response):
        item = response.meta['key']

        #标题
        try:
            title = response.xpath('//*[@id="productTitle"]/text()').extract()[0]
            item['title'] = title.strip()
        except:
            item['title'] = '---'


        #品牌
        try:
            brand = response.xpath('//*[@id="brand"]/text()').extract()[0]
            item['brand'] = brand.strip()
        except:
            item['brand'] = '---'


        #星数
        try:
            item['star'] = response.xpath('//*[@id="acrPopover"]/span[1]/a/i[1]/span/text()').extract()[0]
        except:
            item['star'] = '---'


        #评论人数
        try:
            num = response.xpath('//*[@id="acrCustomerReviewText"]/text()').extract()[0]
            item['num'] = re.search(r'([0-9]*)', num).group(1)
        except:
            item['num'] = '---'


        #价格
        try:
            price = response.xpath('//*[@class="a-size-medium a-color-price"]/text()').extract()[0]
            item['price'] = price.strip()
        except:
            item['price'] = '---'


        # 类目排名
        try:
            rank = response.xpath('//*[@id="SalesRank"]/ul/li[2]/span[1]/text()').extract()[0]
            item['rank'] = rank.replace('#', '')
        except:
            item['rank'] = '---'



        # 产品描述
        try:
            description = response.xpath('//*[@id="feature-bullets"]/ul/li').extract()
            description_1 = ''.join(description)
            redescription = '<li><span class="a-list-item">\s*(.*)\s*</span></li>'
            item['description'] = re.findall(redescription, description_1)
        except:
            item['description'] = '---'


        case = response.xpath('//*[@class="content"]/ul/li').extract()
        case1 = ''.join(case)

        # 商品编号（用parse方法里的也可以）
        try:
            reASIN = '<li><b>ASIN:\s*</b>(.*)</li>'
            ASIN = re.findall(reASIN, case1)[0]
            strinfo = re.compile('<.*')
            item['ASIN'] = strinfo.sub('', ASIN).strip()
        except:
            item['ASIN'] = '---'


        # 上市时间
        try:
            redate = '<li><b> Date first available at Amazon.co.uk:</b>(.*)</li>'
            date = re.findall(redate, case1)[0]
            item['date'] = date.strip()
        except:
            item['date'] = '---'


        #评论
        comments_list = response.xpath('//*[@class="a-section celwidget"]')
        for comment in comments_list:
            pass



        yield item





