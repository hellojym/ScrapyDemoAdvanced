# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class Gushi(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title = scrapy.Field()
    content = scrapy.Field()
    author = scrapy.Field()
    dynasty = scrapy.Field()


class LianjiaItem(scrapy.Item):
    agent = scrapy.Field()
    info = scrapy.Field()
    floor = scrapy.Field()
    date = scrapy.Field()
    feature = scrapy.Field()
    guapai = scrapy.Field()
    price = scrapy.Field()
    avg = scrapy.Field()
    title = scrapy.Field()


class HouseItem(scrapy.Item):
    title = scrapy.Field()
    xiaoqu = scrapy.Field()
    info = scrapy.Field()
    area = scrapy.Field()
    floor = scrapy.Field()
    market = scrapy.Field()
    total = scrapy.Field()
    avg = scrapy.Field()


class MeiziItem(scrapy.Item):
    img_urls = scrapy.Field()
    images = scrapy.Field()
    image_paths = scrapy.Field()
