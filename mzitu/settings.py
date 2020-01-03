# -*- coding: utf-8 -*-

BOT_NAME = 'mzitu'
SPIDER_MODULES = ['mzitu.spiders']
NEWSPIDER_MODULE = 'mzitu.spiders'

USER_AGENT = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64 ; rv:71) Gecko/20100101 Firefox/71.0'
ROBOTSTXT_OBEY = False

ITEM_PIPELINES = {
    'mzitu.pipelines.RenameImagesPipeline': 300,
}
IMAGES_STORE='/home/username/Downloads/scrapy/mzitu/' #修改此处为自己的路径以存储图片
IMAGES_MIN_WIDTH=110
IMAGES_MIN_HEIGHT=110
