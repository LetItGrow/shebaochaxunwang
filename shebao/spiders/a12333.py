# -*- coding: utf-8 -*-
import scrapy
from shebao.items import ShebaoItem
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class A12333Spider(scrapy.Spider):
    name = "12333"
    allowed_domains = ["12333sb.com/yibao.html"]
    start_urls = (
        'http://www.12333sb.com/yibao.html',
    )

    def parse(self, response):
        item = ShebaoItem()
        for site in response.xpath('//div[@class="neirong"]/a'):
            item['name'] = site.xpath('text()').extract()
            item['url'] = site.xpath('@href').extract()
            yield item

