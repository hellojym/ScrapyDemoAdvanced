# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from scrapy.pipelines.images import ImagesPipeline
from scrapy.exceptions import DropItem
from scrapy import Request


class ImagePipeLine(ImagesPipeline):
    default_headers = {
        "Referer": "http://www.meizitu.com/a/5013.html",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/77.0.3833.0 Safari/537.36 "
    }

    def get_media_requests(self, item, info):
        print("process_item")
        # url = item['img_urls']
        # self.default_headers['Referer'] = url
        # yield Request(item['img_urls'], headers=self.default_headers)
        for image_url in item['img_urls']:
            self.default_headers['referer'] = image_url
            yield Request(image_url, headers=self.default_headers)

    def item_completed(self, results, item, info):
        print("process_item_done")
        image_paths = [x['path'] for ok, x in results if ok]
        if not image_paths:
            raise DropItem("Item contains no images")
        item['image_paths'] = image_paths
        return item
