# -*- coding: utf-8 -*-

from os.path import basename
from scrapy.http import Request 
from scrapy.pipelines.images import ImagesPipeline

class RenameImagesPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        for img_url in item['image_urls']:
            img_type = basename(img_url).split('.')[1]  #jpg,jpeg,png
            img_idex = item['image_urls'].index(img_url)
            img_name = item['titles'][img_idex]         
            img_name = ''.join([img_name,'.',img_type])
            yield Request(img_url, meta={'img_name': img_name})

    def file_path(self, request, response=None, info=None):
        return request.meta['img_name']
