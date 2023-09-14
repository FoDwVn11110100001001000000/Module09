import json

import requests
from bs4 import BeautifulSoup

def response(link: str = ''):
    base_url = f'https://quotes.toscrape.com{link}'
    response = requests.get(base_url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'lxml')
    else:
        raise requests.exceptions.RequestException(f"Запит завершився з кодом помилки {response.status_code}")
    return soup

def get_all_links() -> set:
    pages = [ f'/page/{page_number}/' for page_number in range(1, 11) ]
    links = [ response(page).select('div[class=quote] span a') for page in pages ]
    links_set = set(link.get('href') for sublist in links for link in sublist)
    return links_set

def serialize(name: str, data: list[dict]):
    with open(name, "a", encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)

def authors():
    authors_list = list()

    links = get_all_links()
    for link in links:
        current_link = response(link)
        fullname = current_link.select_one('h3', class_='author-title').text
        born_date = current_link.select_one('div[class=author-details] p span[class=author-born-date]').text
        location = current_link.select_one('div[class=author-details] p span[class=author-born-location]').text
        description = current_link.select_one('div[class=author-description]').text.strip()

        authors_list.append({
            'fullname': fullname,
            'born_date': born_date,
            'born_location': location,
            'description': description
        })
    return authors_list


if __name__ == '__main__':
    data = authors()
    serialize('authors.json', data)
    print('FINISHED')



