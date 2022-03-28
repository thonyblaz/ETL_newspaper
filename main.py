import scrapy
from scrapy.spiders import SitemapSpider
from scrapy.crawler import CrawlerProcess
#para que funcionen varios spyders al mismo tiempo
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.log import configure_logging
from scrapy.utils.project import get_project_settings


import datetime
import os

# mis librerias
#scrapers
import ETL.quotes_scraper.spiders.quotes as scraper1
import ETL.quotes_scraper.spiders.eldeber as scraper2
#data analist
import ETL.data_analysis.data_analysis as tr


def extract():
    #para utilizar varios spyder al mismo tiempo
    configure_logging()
    settings = get_project_settings()
    runner = CrawlerRunner(settings)
    runner.crawl(scraper1.QuotesSpider)
    runner.crawl(scraper2.QuotesSpider)
    d = runner.join()
    d.addBoth(lambda _: reactor.stop())

    reactor.run()
    #Codigo para un solo spyder
    """ process = CrawlerProcess()
    process.crawl(scraper1.QuotesSpider)
    process.start() """

def transform(today):
    tr.transform_data(today)


def new_folder(today):
    if not os.path.isdir(f'data/{today}'):
        os.mkdir(f'data/{today}')


if __name__ == '__main__':
    today = datetime.date.today().strftime('%d-%m-%y')
    new_folder(today)
    #extract()
    transform(today)