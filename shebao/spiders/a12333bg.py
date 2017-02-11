# -*- coding: utf-8 -*-
import scrapy
from shebao.items import ShebaoItem
from shebao.spiders.UrlsTools import Json_GetData
from string import strip
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class A12333bgSpider(scrapy.Spider):
    name = "12333bg"
    allowed_domains = ["12333sb.com"]
    start_urls = ('http://www.12333sb.com/shebao/neimeng/wlcb.html',)#Json_GetData('sbsy.json','url')

    def parse(self, response):
        item = ShebaoItem()
        for site in response.xpath('//tr'):
            if site.xpath('td[1]/text()').extract() == [u'\u540d\u79f0'] or site.xpath('td[1]/text()').extract() ==[u'\u5355\u4f4d\u540d\u79f0']or site.xpath('td[1]/text()').extract() ==[] or site.xpath('td[1]/text()').extract() ==["      "]or site.xpath('td[1]/text()').extract() ==["            "]or site.xpath('td[1]/text()').extract() ==[" 当前位置：", " >> ", " >> ", " >> 浏览文章"]or site.xpath('td[1]/text()').extract() ==[" 当前位置：", " >> ", " >> 浏览文章"]or site.xpath('td[1]/text()').extract() ==["\r\n              \r\n            "]or site.xpath('td[1]/text()').extract() ==["\r\n", "\r\n", "\r\n"]:
                continue
            else:
                item['DanWeiMingChen'] = site.xpath('td[1]/text()').extract()
                item['TongXinDiZhi'] = site.xpath('td[2]/text()').extract()
                item['MingChen1'] = site.xpath('td[3]/text()').extract()
                item['DianHua1'] = site.xpath('td[4]/text()').extract()
                item['ChuanZhen1'] = site.xpath('td[5]/text()').extract()
                item['MingChen2'] = site.xpath('td[6]/text()').extract()
                item['DianHua2'] = site.xpath('td[7]/text()').extract()
                item['ChuanZhen2'] = site.xpath('td[8]/text()').extract()
                yield item
