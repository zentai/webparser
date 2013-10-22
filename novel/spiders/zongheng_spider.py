from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from novel.items import NovelItem

class NovelSpider(BaseSpider):
    name = "bubaizhanshen"
    allowed_domains = ["big5.zongheng.com"]
    start_urls = [
        "http://big5.zongheng.com/book/251393.html",
        "http://book.zongheng.com/book/293409.html"
    ]

    def parse(self, response):
       hxs = HtmlXPathSelector(response)
       sites = hxs.select('//span[@itemprop="name"]')
       title = ''

       for site in sites:
           title = site.select('text()').extract()

       sites = hxs.select('//div[@class="fir"]')
       items = []
       for site in sites:
           item = NovelItem()
           item['title'] = title
           item['link_text'] = site.select('h3/a/text()').extract()
           item['link'] = site.select('h3/a/@href').extract()
           items.append(item)
       return items