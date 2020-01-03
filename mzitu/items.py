# -*- coding: utf-8 -*-

import scrapy

class ImageItem(scrapy.Item):
    titles = scrapy.Field()
    image_urls = scrapy.Field()
