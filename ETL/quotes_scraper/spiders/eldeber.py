import scrapy
from scrapy.spiders import SitemapSpider
from scrapy.crawler import CrawlerProcess

import datetime
# my lybraries
#import ETL.quotes_scraper.spiders.tools.delete_args as td #para que el scraper funciones desde main.py
import tools.delete_args as td #para que funcione de forma local
# Xpaths
XPATH_LINK_TO_ARTICLE = '//div[@class="block"]//a/@href'
XPATH_TITLE = '//div[@class="text"]/h1/text()'
XPATH_RESUME = '//div[@class="heading  heading-gallery"]//h2/text()'
XPATH_BODY_1 = '//b/text()'
XPATH_BODY_2 = '//article//p/span/text()'

today = datetime.date.today().strftime('%d-%m-%y')


class QuotesSpider(scrapy.Spider):
    name = 'eldeber'
    start_urls = [
        'https://eldeber.com.bo/'
    ]
    custom_settings = {
        'FEED_URI': f'data/{today}/el_deber_data_extract.csv',
        'FEED_FORMAT': 'csv',
        'ENCODING': 'UTF8',
    }

    def parse_body(self, response, **kwargs):
        title = response.xpath(XPATH_TITLE).get()
        resume = response.xpath(XPATH_RESUME).get()
        body_1 = response.xpath(XPATH_BODY_1).getall()
        body_2 = response.xpath(XPATH_BODY_2).getall()
        # modificaciones
        if isinstance(title, str) == True:
            title = td.ReplaceW(title).word_modify()

        # contenido

        if isinstance(resume, str) == True:
            paragraph = td.ReplaceW(resume).word_modify()

        contents_1 = ""
        for b in body_1:
            if isinstance(b, str) == True:
                p = td.ReplaceW(b).word_modify()
                contents_1 = contents_1 + " " + p

        contents_2 = ""
        for b in body_2:
            if isinstance(b, str) == True:
                p = td.ReplaceW(b).word_modify()
                contents_2 = contents_2 + " " + p

        paragraph = paragraph + " "+contents_1+" "+contents_2
        # traer link del anterior parse
        if kwargs:
            link = kwargs['link']
        yield{
            'title': title,
            'contents': paragraph,
            'url': link
        }

    def parse(self, response):
        #print('*'*500)
        #print(response.status, response.headers)
        links = response.xpath(XPATH_LINK_TO_ARTICLE).getall()
        for link in links:
            if link:
                url = 'https://eldeber.com.bo'+link
                yield response.follow(url, callback=self.parse_body, cb_kwargs={'link': url})


if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(QuotesSpider)
    process.start()
