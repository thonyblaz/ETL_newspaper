import scrapy
from scrapy.spiders import SitemapSpider
from scrapy.crawler import CrawlerProcess
#librerias de python
import re
import datetime
# my lybraries
import ETL.quotes_scraper.spiders.tools.delete_args as td #para que el scraper funciones desde main.py
#import tools.delete_args as td #para realizar modificaciones en local
# Xpaths
XPATH_LINK_TO_ARTICLE = '//div[@id="content"]//a/@href'
XPATH_TITLE = '//div[1]//div/div[1]/header/h1/text()'
XPATH_BODY = '//div[@class="entry-content herald-entry-content"]/p/text()'

today = datetime.date.today().strftime('%d-%m-%y')


class QuotesSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = [
        'https://lapatria.bo/',
        'https://lapatria.bo/oruro/',
        'https://lapatria.bo/bolivia/'
        'https://lapatria.bo/politica/'
        'https://lapatria.bo/estilo-de-vida/',
        'https://lapatria.bo/internacional/',
        'https://lapatria.bo/policial/'
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
            patron = re.compile(r'\d\d\d\d/\d\d/\d\d')
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