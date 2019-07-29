# -*- coding: utf-8 -*-
import scrapy
from ScrapyAdvanced.items import MeiziItem


class MeiziSpider(scrapy.Spider):
    name = 'meizi'
    allowed_domains = ['meizitu.com']
    custom_settings = {
        "Referer": "http://www.meizitu.com/a/101.html",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/77.0.3833.0 Safari/537.36 "
    }
    headers = {
        "Referer": "http://www.meizitu.com/a/101.html",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/77.0.3833.0 Safari/537.36 "
    }
    urls = []
    for i in range(1, 3):
        urls.append("http://www.meizitu.com/a/%s.html" % i)
    start_urls = ["http://www.meizitu.com/a/1.html"]

    def parse(self, response):
        print(".................")
        print(response)
        for e in response.xpath("//*[@id=\"maincontent\"]/div[2]/p[1]/img"):
            item = MeiziItem()
            link = e.xpath("@src").extract()
            print(link)
            item['link'] = link
            yield item
