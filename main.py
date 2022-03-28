
import scrapy
from scrapy.spiders import SitemapSpider
from scrapy.crawler import CrawlerProcess
import datetime
import os
# mis librerias
#scrapers
import ETL.quotes_scraper.spiders.quotes as scraper1
import ETL.quotes_scraper.spiders.eldeber as scraper2
#data analist
import ETL.data_analysis.data_analysis as tr


def extract():
    process = CrawlerProcess()
    process.crawl(scraper1.QuotesSpider)
    process.start()
    #process.crawl(scraper2.QuotesSpider)
    #process.start()


def transform(today):
    tr.transform_data(today)


def new_folder(today):
    if not os.path.isdir(f'data/{today}'):
        os.mkdir(f'data/{today}')


if __name__ == '__main__':
    today = datetime.date.today().strftime('%d-%m-%y')
    new_folder(today)
    extract()
    transform(today)
