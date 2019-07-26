# -*- coding: utf-8 -*-
import scrapy
from ScrapyAdvanced.items import HouseItem


def get_urls():
    result = []
    for i in range(2, 12):
        result.append("https://bj.lianjia.com/ershoufang/tongzhou/pg%ddp1l2a3p4" % i)
    return result


class HouseSpider(scrapy.Spider):
    name = 'house'
    allowed_domains = ['bj.lianjia.com']
    start_urls = get_urls()

    def parse(self, response):
        for each in response.xpath("//*[@id=\"content\"]/div[1]/ul/li"):
            item = HouseItem()
            item['title'] = each.xpath("div[1]/div[1]/a/text()").extract()
            item['xiaoqu'] = each.xpath("div[1]/div[2]/div/a/text()").extract()
            item['info'] = each.xpath("div[1]/div[2]/div/text()").extract()
            item['floor'] = each.xpath("div[1]/div[3]/div/text()").extract()
            item['area'] = each.xpath("div[1]/div[3]/div/a/text()").extract()
            item['market'] = each.xpath("div[1]/div[4]/text()").extract()
            item['total'] = each.xpath("div[1]/div[6]/div[1]/span/text()").extract()
            item['avg'] = each.xpath("div[1]/div[6]/div[2]/span/text()").extract()
            yield item
