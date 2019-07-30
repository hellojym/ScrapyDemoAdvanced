# -*- coding: utf-8 -*-
import scrapy
from ScrapyAdvanced.items import MeiziItem


# 妹子图网站的所有妹子图片
class MeiziSpider(scrapy.Spider):
    index = 0
    name = 'meizi'
    allowed_domains = ['meizitu.com']
    headers = {
        "Referer": "http://www.meizitu.com/a/5013.html",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/77.0.3833.0 Safari/537.36 "
    }
    urls = []
    for i in range(5050, 5100):
        urls.append("http://www.meizitu.com/a/%s.html" % i)
    # start_urls = ["http://www.meizitu.com/a/5102.html"]
    start_urls = urls

    def parse(self, response):
        print(".................%d" % self.index)
        self.index = self.index + 1
        for e in response.xpath("//*[@id=\"picture\"]/p/img"):
            item = MeiziItem()
            link = e.xpath("@src").extract()
            if link:
                print(link)
                item['img_urls'] = link
                yield item
