# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request


class ScrapyadvancedPipeline(object):
    def process_item(self, item, spider):
        return item


class ImagePipeLine(ImagesPipeline):
    default_headers = {
        "Referer": "http://www.meizitu.com/a/101.html",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/77.0.3833.0 Safari/537.36 "
    }

    def get_media_requests(self, item, info):
        for image_url in item['link']:
            self.default_headers['referer'] = image_url
            yield Request(image_url)

    def item_completed(self, results, item, info):
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['path'] = image_paths
        return item
