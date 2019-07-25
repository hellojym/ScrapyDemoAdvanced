# -*- coding: utf-8 -*-
import scrapy
from ScrapyAdvanced.items import Gushi


class GushiwenSpider(scrapy.Spider):
    count = 0
    name = 'gushiwen'
    domainPrefix = "https://so.gushiwen.org"
    allowed_domains = ['so.gushiwen.org']
    start_urls = ['https://so.gushiwen.org/shiwen/default_0AA2.aspx']

    def parse(self, response):
        for each in response.xpath("/html/body/div[2]/div[1]//div[@class='sons']"):
            item = Gushi()
            title = each.xpath("div[1]/p[1]/a/b/text()").extract()[0]
            author = each.xpath("div[1]/p[2]/a[2]/text()").extract()[0]
            dynasty = each.xpath("div[1]/p[2]/a[1]/text()").extract()[0]
            content = each.xpath("div[1]/div[2]").xpath("string(.)").extract()[0]
            contentResult = content.replace("<br>", "")
            item['title'] = title
            item['author'] = author
            item['dynasty'] = dynasty
            item['content'] = contentResult
            yield item
        next_page = self.domainPrefix + response.xpath("//*[@id=\"FromPage\"]/div/a[1]/@href").extract()[0]
        self.count = self.count + 1
        if next_page and self.count < 20:
            yield scrapy.Request(next_page, callback=self.parse)
