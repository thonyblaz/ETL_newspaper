import scrapy
from scrapy.spiders import SitemapSpider
from scrapy.crawler import CrawlerProcess

import datetime
import re
# my lybraries
# para que el scraper funciones desde main.py
import ETL.quotes_scraper.spiders.tools.delete_args as td
# import tools.delete_args as td #para que funcione de forma local
# Xpaths
XPATH_LINK_TO_ARTICLE = '//div[@class="block"]//a/@href'
XPATH_TITLE = '//div[@class="text"]/h1/text()'
XPATH_RESUME = '//div[@class="heading  heading-gallery"]//h2/text()'
XPATH_BODY_1 = '//b/text()'
XPATH_BODY_2 = '//article//p/span/text()'
XPATH_BODY_3 ='//article//p/text()'
XPATH_DATE = '//div[@class="bottom"]/h6/span/text()'

today = datetime.date.today().strftime('%d-%m-%y')


class QuotesSpider(scrapy.Spider):
    name = 'eldeber'
    start_urls = [
        'https://eldeber.com.bo/',
        'https://eldeber.com.bo/santa-cruz',
        'https://eldeber.com.bo/pais',
        'https://eldeber.com.bo/economia',
        'https://eldeber.com.bo/opinion',
        'https://eldeber.com.bo/mundo',
        'https://eldeber.com.bo/sociales'
    ]
    custom_settings = {
        'FEED_URI': f'data/{today}/data_extracted.csv',
        'FEED_FORMAT': 'csv',
        'ENCODING': 'UTF8',
    }

    def parse_body(self, response, **kwargs):
        title = response.xpath(XPATH_TITLE).get()
        resume = response.xpath(XPATH_RESUME).get()
        body_1 = response.xpath(XPATH_BODY_1).getall()
        body_2 = response.xpath(XPATH_BODY_2).getall()
        body_3 = response.xpath(XPATH_BODY_3).getall()
        date = response.xpath(XPATH_DATE).get()
        if resume:
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
            contents_3 = ""
            for b in body_3:
                if isinstance(b, str) == True:
                    p = td.ReplaceW(b).word_modify()
                    contents_3 = contents_3 + " " + p

            paragraph = paragraph + " "+contents_1+" "+contents_2+" "+contents_3
            # traer link del anterior parse
            if kwargs:
                link = kwargs['link']
            # para modificar la fecha mediante expresiones regulares
            patron = re.compile(r' \d\d:\d\d  ')
            patron = patron.findall(date)
            date = date.replace(patron[0], '')

            yield{
                'title': title,
                'contents': paragraph,
                'url': link,
                'date': date
            }

    def parse(self, response):
        # print('*'*500)
        #print(response.status, response.headers)
        links = response.xpath(XPATH_LINK_TO_ARTICLE).getall()
        for link in links:
            if link:
                url = 'https://eldeber.com.bo'+link
                yield response.follow(url, callback=self.parse_body, cb_kwargs={'link': url})


""" if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(QuotesSpider)
    process.start() """
