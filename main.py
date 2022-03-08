
import scrapy
from scrapy.spiders import SitemapSpider
from scrapy.crawler import CrawlerProcess
import datetime
#mis librerias
import ETL.quotes_scraper.spiders.quotes as scraper


def extract():
    process=CrawlerProcess()
    process.crawl(scraper.QuotesSpider)
    process.start()

def transform():
    pass

if __name__ == '__main__':
    today = datetime.date.today().strftime('%d-%m-%y')
    #extract()
    transform(today)