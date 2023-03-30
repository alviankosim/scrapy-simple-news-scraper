# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy

class NewsScraperItem(scrapy.Item):
    # define the fields for your item here like:
    title   = scrapy.Field()
    summary = scrapy.Field()
    url     = scrapy.Field()
    image   = scrapy.Field()
    date    = scrapy.Field()
    pass
