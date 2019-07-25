# -*- coding: utf-8 -*-
import scrapy
from ScrapyAdvanced.items import LianjiaItem


def get_urls():
    result = []
    for i in range(2, 100):
        result.append("https://bj.lianjia.com/chengjiao/tongzhou/pg%d/" % i)
    return result


class LianjiaSpider(scrapy.Spider):
    name = 'lianjia'
    allowed_domains = ['bj.lianjia.com']
    start_urls = get_urls()
    i = 0

    def parse(self, response):
        for each in response.xpath("/html/body/div[5]/div[1]/ul/li"):
            item = LianjiaItem()
            item['title'] = each.xpath("div/div[1]/a/text()").extract()[0]
            item['agent'] = each.xpath("div/div[6]/a/text()").extract()
            item['floor'] = each.xpath("div/div[3]/div[1]/text()").extract()[0]
            item['info'] = each.xpath("div/div[2]/div[1]/text()").extract()[0]
            item['feature'] = each.xpath("div/div[4]/span[2]").xpath("string(.)").extract()
            item['avg'] = each.xpath("div/div[3]/div[3]/span/text()").extract()
            item['date'] = each.xpath("div/div[2]/div[2]/text()").extract()[0]
            item['guapai'] = each.xpath("div/div[5]/span[2]").xpath("string(.)").extract()
            item['price'] = each.xpath("div/div[2]/div[3]").xpath("string(.)").extract()[0]
            yield item
