import requests
from bs4 import BeautifulSoup

def fetch_data(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

def fetch_popular_games_data(soup):
    pop_results = soup.find('div', class_='tab_content', id='tab_newreleases_content')
    results = pop_results.find_all('div', class_='tab_item_content')
    return results
