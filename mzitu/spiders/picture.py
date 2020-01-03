# -*- coding: utf-8 -*-
import sys
import scrapy
from mzitu.items import ImageItem

class MzituSpider(scrapy.Spider):
    name = 'mzitu'
    allowed_domains = ['www.mzitu.com']
    start_urls = ['https://www.mzitu.com/']

    item = ImageItem()
    def parse(self, response):
        #step 1: get image title and url
        sel = response.xpath('//div[@class="postlist"]/ul')
        ttls= sel.xpath('.//img/@alt').extract()
        self.item['titles'] = ttls

        lks = sel.xpath('.//img/@data-original').extract()
        self.item['image_urls'] = lks
        yield self.item

        #step 2: get next page url
        href=response.xpath('//div[@class="nav-links"]/a[@class="next page-numbers"]/@href').extract_first()
        next_url=response.urljoin(href)
        if next_url:
            yield scrapy.Request(next_url, callback=self.parse)
