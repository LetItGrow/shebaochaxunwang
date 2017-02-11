# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ShebaoItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    name = scrapy.Field()
    url = scrapy.Field()
    DanWeiMingChen = scrapy.Field()
    TongXinDiZhi = scrapy.Field()
    MingChen1 = scrapy.Field()
    DianHua1 = scrapy.Field()
    ChuanZhen1 = scrapy.Field()
    MingChen2 = scrapy.Field()
    DianHua2 = scrapy.Field()
    ChuanZhen2 = scrapy.Field()