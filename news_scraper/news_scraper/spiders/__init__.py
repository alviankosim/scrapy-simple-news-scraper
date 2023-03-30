# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

import scrapy
from news_scraper.items import NewsScraperItem
from datetime import datetime

class NewsSpider(scrapy.Spider):
    name = 'news'
    custom_settings = {
        'FEEDS': { 'fetched/news-list' + datetime.today().strftime('%Y%m%d%H%M%S') + '.json': { 'format': 'json',}},
        'CLOSESPIDER_ITEMCOUNT': 100 # <= ITEMCOUNT
    }

    def start_requests(self):
        url = 'https://berita.depok.go.id/kategori/daftar/photo/'
        yield scrapy.Request(url, callback=self.parse)

    def parse(self, response):
        news_item = NewsScraperItem()
        for news in response.css('body > div.container > div > div.col-12.col-sm-8 > div[class="row"]'):
            news_item['title']   = news.css('h5.fw-bold::text').get()
            news_item['summary'] = news.css('p.text-secondary::text').get()
            news_item['url']     = news.css('div.col-8 > a::attr(href)').get()
            news_item['image']   = news.css('img::attr(src)').get()
            news_item['date']    = news.css('h6.text-secondary::text').get()
            yield news_item
        
        # go to next page
        next_page = response.css("a.page-link::attr(href)")[-1].extract()
        if next_page:
            yield response.follow(next_page, callback=self.parse)