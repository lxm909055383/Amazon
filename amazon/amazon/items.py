# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class AmazonItem(scrapy.Item):

    link = scrapy.Field()

    ASIN = scrapy.Field()
    title = scrapy.Field()
    brand = scrapy.Field()
    price = scrapy.Field()
    star = scrapy.Field()
    num = scrapy.Field()
    rank = scrapy.Field()
    date = scrapy.Field()
    description = scrapy.Field()


    pass
