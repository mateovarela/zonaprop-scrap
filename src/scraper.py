import re
import time
from bs4 import BeautifulSoup

PAGE_URL_SUFFIX = '-pagina-'
HTML_EXTENSION = '.html'
BASE_SITE_URL = "https://www.zonaprop.com.ar"

class Scraper:
    def __init__(self, browser, base_url):
        self.browser = browser
        self.base_url = base_url

    def scrap_page(self, page_number):
        if page_number == 1:
            page_url = f'{self.base_url}{HTML_EXTENSION}'
        else:
            page_url = f'{self.base_url}{PAGE_URL_SUFFIX}{page_number}{HTML_EXTENSION}'

        print(f'URL: {page_url}')
        page = self.browser.get_text(page_url)
        soup = BeautifulSoup(page, 'lxml')
        estate_posts = soup.find_all('div', attrs={'data-posting-type': True})
        
        urls = [BASE_SITE_URL + post.get('data-to-posting') for post in estate_posts if post.get('data-to-posting')]
        return urls

    def scrap_website(self):
        page_number = 1
        urls = []
        estates_scraped = 0
        estates_quantity = self.get_estates_quantity()
        
        while estates_quantity > estates_scraped:
            print(f'Page: {page_number}')
            urls += self.scrap_page(page_number)
            page_number += 1
            estates_scraped = len(urls)
            time.sleep(1)
        
        return urls

    def get_estates_quantity(self):
        page_url = f'{self.base_url}{HTML_EXTENSION}'
        page = self.browser.get_text(page_url)
        soup = BeautifulSoup(page, 'lxml')
        
        estates_text = soup.find_all('h1')[0].text
        estates_quantity = int(re.findall(r'\d+', estates_text.replace('.', ''))[0])
        return estates_quantity
