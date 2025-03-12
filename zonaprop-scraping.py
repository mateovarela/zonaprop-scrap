import sys

import pandas as pd

from src import utils
from src.browser import Browser
from src.scraper import Scraper


def main(url):
    base_url = utils.parse_zonaprop_url(url)
    print(f'Running scraper for {base_url}')
    print(f'This may take a while...')
    browser = Browser()
    scraper = Scraper(browser, base_url)
    
    urls = set()
    estates = scraper.scrap_website()
    estates_quantity = len(estates)
    urls.update(estates)

    while estates_quantity > len(urls):
        print("Duplicate estates found, scraping again... ({0}/{1} scraped)".format(len(urls), estates_quantity))
        estates = scraper.scrap_website()
        urls.update(estates)

    df = pd.DataFrame(urls, columns=['url'])
    
    print('Scraping finished !!!')
    print('Saving data to csv file')
    filename = utils.get_filename_from_datetime(base_url, 'csv')
    utils.save_df_to_csv(df, filename)
    print(f'Data saved to {filename}')
    print('Scrap finished !!!')

if __name__ == '__main__':
    url = sys.argv[1]
    url = 'https://www.zonaprop.com.ar/departamentos-alquiler.html' if url is None else url
    main(url)
