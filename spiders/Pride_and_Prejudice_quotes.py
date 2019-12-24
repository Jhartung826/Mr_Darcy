# -*- coding: utf-8 -*-
import scrapy


class PrideAndPrejudiceQuotesSpider(scrapy.Spider):
    name = 'Pride_and_Prejudice_quotes'
    # allowed_domains = ['https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice']
    # start_urls = ['https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=1', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=2', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=3', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=4', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=5', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=6', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=7', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=8', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=9', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=10', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=11', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=12', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=13', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=14', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=15', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=16', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=17', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=18', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=19', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=20', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=21', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=22', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=23', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=24', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=25', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=26', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=27', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=28', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=29', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=30', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=31', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=32', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=33', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=34', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=35', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=36', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=37', 'https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=38']
    start_urls = ['https://www.goodreads.com/work/quotes/3060926-pride-and-prejudice?page=1']
    def parse(self, response):
        print('processing:'+response.url)
        quote = response.css(".quoteText::text").extract()
        list_of_quotes = quote

        for i in list_of_quotes:
            soto = i.rstrip("\n")
            soto = soto.strip('“')
            soto = soto.strip('”')
            scraped_info = {
                'Quotes': soto,
                'Author': 'Jane Austen'
            }
            yield scraped_info
        

        
