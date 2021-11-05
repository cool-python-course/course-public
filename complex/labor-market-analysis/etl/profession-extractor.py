import sys
import logging
import requests
from pymongo import MongoClient
from bs4 import BeautifulSoup, Tag
from typing import List, Dict

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(
    filename='analitics.log',
    filemode='w',
    format=LOG_FORMAT,
    level=logging.DEBUG
)
LOG = logging.getLogger()
LOG.addHandler(logging.StreamHandler(sys.stdout))

BASE_URL = 'http://www.profession.hu/allasok'


def fetch_profession_page(url: str) -> BeautifulSoup:
    r = requests.get(BASE_URL)
    return BeautifulSoup(r.text, 'html.parser')


def extract_job_cards(page: BeautifulSoup) -> List[Tag]:
    # job_cards_panels = page.find('ul', {'class': 'job-cards'})
    job_cards = page.find('ul', {'class': 'job-cards'}).find_all('li')
    return job_cards


def transform_job_card(job_card: Tag) -> Dict:
    job_advertisement_link = job_card.attrs['data-link']
    job_prof_name = job_card.attrs['data-prof-name']
    company = {
        'name': job_card.find('div', {'class': 'card-body-header'}).find('div', {
            'class': 'job-card__company-name'}).text.strip(),
        'address': job_card.find('div', {'class': 'card-body-header'}).find('div', {
            'class': 'job-card__company-address'}).text.strip()
    }
    job_description = {
        'description': job_card.find('div', {'class': 'job-card__text'}).text.strip() if job_card.find('div', {'class': 'job-card__text'}) != None else '',
        'tags' : [tag.text.strip() for tag in job_card.find('div', {'class': 'job-card__tags'}).find_all('span')]
    }
    return {
        'job_advertisement_url': job_advertisement_link,
        'prof_name': job_prof_name,
        'company': company,
        'job_description': job_description
    }

def extract_next_url(page : BeautifulSoup) -> str:
    next_btn = page.find('a', {'class': 'next'})
    return next_btn.attrs['href'] if next_btn != None else None

def get_collection():
    USERNAME = 'root'
    PASSWORD = 'example'
    DB_NAME = 'sample'
    HOST = 'localhost'
    PORT = 27017
    CONNECTION_STRING = f'mongodb://{USERNAME}:{PASSWORD}@{HOST}:{PORT}/{DB_NAME}?authSource=admin'
    client = MongoClient(CONNECTION_STRING)
    return client[DB_NAME]['jobs']

if __name__ == '__main__':
    print('Hello World')
    html_doc = fetch_profession_page(BASE_URL)
    job_cards = extract_job_cards(html_doc)
    data_lake = get_collection()
    for job_card in job_cards:
        data_lake.insert(transform_job_card(job_card))
        print(f'{transform_job_card(job_card)}')
