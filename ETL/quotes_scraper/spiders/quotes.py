import scrapy
from scrapy.spiders import SitemapSpider
from scrapy.crawler import CrawlerProcess

import datetime

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
        'FEED_URI': f'data/{today}/data_extract.csv',
        'FEED_FORMAT': 'csv',
        'ENCODING': 'UTF8',
    }

    def parse_body(self, response, **kwargs):
        title = response.xpath(XPATH_TITLE).get()
        body = response.xpath(XPATH_BODY).getall()
        # modificaciones
        if isinstance(title, str)==True:
            title = title.replace(',', '')
            title = title.replace(':', '')
            title = title.replace(';', '')
            title = title.replace('"', '')
            title = title.replace("'", '')
            title = title.replace("-", '')
            title = title.replace("\n", '')
            title = title.replace('\\', '')

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
                print(link)
                yield response.follow(link, callback=self.parse_body, cb_kwargs={'link': link})


""" if __name__ == '__main__':
    process = CrawlerProcess()
    process.crawl(QuotesSpider)
    process.start()

 """