import scrapy
from scrapy.spiders import SitemapSpider
from scrapy.crawler import CrawlerProcess

import datetime

# Xpaths
XPATH_LINK_TO_ARTICLE = '//h3[@class="entry-title td-module-title"]/a/@href'
XPATH_TITLE = '//h1[@class="entry-title"]/text()'
XPATH_BODY = '//div/p/text()'

today = datetime.date.today().strftime('%d-%m-%y')


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://lapatria.bo/'
    ]
    custom_settings = {
        'FEED_URI': f'data/{today}.csv',
        'FEED_FORMAT': 'csv',
        'ENCODING': 'UTF8',
    }

    def parse_body(self, response, **kwargs):
        title = response.xpath(XPATH_TITLE).get()
        body = response.xpath(XPATH_BODY).getall()
        # modificaciones
        title = title.replace(',', '')

        paragraph = ""
        for b in body:
            p = b.replace(',', '')
            p = p.replace('\'', '')
            p = p.replace(';', '')
            p = p.replace(':', '')
            p = p.replace('"', '**')
            paragraph = paragraph + p
        # traer link del anterior parse
        if kwargs:
            link = kwargs['link']
        yield{
            'title': title,
            'contents': paragraph,
            'url': link
        }

    def parse(self, response):
        print('*'*500)
        #print(response.status, response.headers)
        links = response.xpath(XPATH_LINK_TO_ARTICLE).getall()
        for link in links:
            if link:
                yield response.follow(link, callback=self.parse_body, cb_kwargs={'link': link})


""" if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(QuotesSpider)
    process.start()

 """