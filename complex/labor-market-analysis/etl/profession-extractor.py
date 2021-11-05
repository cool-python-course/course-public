from typing import List, Dict

import requests
from bs4 import BeautifulSoup, Tag

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
        'description': job_card.find('div', {'class': 'job-card__text'}).text.strip(),
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


if __name__ == '__main__':
    print('Hello World')
    html_doc = fetch_profession_page(BASE_URL)
    job_cards = extract_job_cards(html_doc)
    for job_card in job_cards:
        print(f'{transform_job_card(job_card)}')
