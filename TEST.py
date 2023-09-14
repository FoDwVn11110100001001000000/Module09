import requests
from bs4 import BeautifulSoup

def response():
    url = 'https://quotes.toscrape.com/'
    resp = requests.get(url)
    return resp

def authors_info():
    soup = BeautifulSoup(response().text, 'lxml')
    authors = []

    author_elements = soup.select('small.author')
    for author_element in author_elements:
        author_name = author_element.get_text(strip=True)
        authors.append({'author': author_name})

    return authors

def main():
    authors_data = authors_info()

    for author_info in authors_data:
        print(f"Автор: {author_info['author']}")

if __name__ == "__main__":
    main()
