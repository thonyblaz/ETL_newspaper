import scrapy
from scrapy.spiders import SitemapSpider
from scrapy.crawler import CrawlerProcess

import datetime
import re
# my lybraries
# para que el scraper funciones desde main.py
import ETL.quotes_scraper.spiders.tools.delete_args as td
#import tools.delete_args as td #para que funcione de forma local
# Xpaths
XPATH_LINK_TO_ARTICLE = '//div[@class="article-meta "]/a/@href'
XPATH_TITLE = '//div[@class="article-content"]//h1[@class="title"]/text()'
XPATH_BODY = '//div[@class="article-content"]//div[@class="article-body"]/p/text()'


today = datetime.date.today().strftime('%d-%m-%y')


class QuotesSpider(scrapy.Spider):
    name = 'larazon'
    start_urls = [
        'https://www.la-razon.com/',
        'https://www.la-razon.com/nacional/',
        'https://www.la-razon.com/ciudades/',
        'https://www.la-razon.com/economia/',
        'https://www.la-razon.com/mundo/',
        'https://www.la-razon.com/sociedad/'
    ]
    custom_settings = {
        'FEED_URI': f'data/{today}/data_extracted.csv',
        'FEED_FORMAT': 'csv',
        'ENCODING': 'UTF8',
    }

    def parse_body(self, response, **kwargs):
        title = response.xpath(XPATH_TITLE).get()
        body = response.xpath(XPATH_BODY).getall()
        if body:

            # modificaciones
            if isinstance(title, str)==True:
                title = td.ReplaceW(title).word_modify()
            #modificamos el contenido
            paragraph = ""
            for b in body:
                if isinstance(b, str) == True:
                    p = td.ReplaceW(b).word_modify()
                    paragraph = paragraph +" "+ p
            # traer link del anterior parse
            if kwargs:
                link = kwargs['link']
            #la fecha mediante expresiones regulares
            patron = re.compile(r'\d+/\d+/\d+')
            date = patron.findall(link)
            yield{
                'title': title,
                'contents': paragraph,
                'url': link,
                'date':date
            }

    def parse(self, response):
        #print('*'*500)
        #print(response.status, response.headers)
        links = response.xpath(XPATH_LINK_TO_ARTICLE).getall()
        for link in links:
            if link:
                print(link)
                yield response.follow(link, callback=self.parse_body, cb_kwargs={'link': link})


""" if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(QuotesSpider)
    process.start()
 """
