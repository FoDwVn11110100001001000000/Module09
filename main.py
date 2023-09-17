import json
import logging

from utils import Author, Quotes
from utils import setup_log
from connect_db import fill_data, connector
from parse import main_parse

def add_authors():
    with open('authors.json', 'r', encoding='UTF-8') as f:
        data = json.load(f)

    for item in data:
        authors = Author(
            fullname=item['fullname'], 
            born_date=item['born_date'],
            born_location = item['born_location'],
            description=item['description']
            )
        authors.save()

def add_quotes():
    with open('quotes.json', 'r', encoding='UTF-8') as f:
        data = json.load(f)

    for item in data:
        author_ids = [autor.id for autor in Author.objects if autor.fullname == item['author']]

        quote = Quotes(tags=item['tags'], author=author_ids, quote=item['quote'])
        quote.save()

def search():
    while True:
        text_input = input('Please, input your request: ')
        if text_input == "exit":
            break
        text_input = text_input.split(':')
        if text_input[0] == 'name':
            author_name = text_input[1].strip()
            quote = Quotes.objects.filter(Author.fullname == author_name)
            for quotee in quote:
                print(quotee.quote)
        elif text_input[0] == 'tag':
            tag = text_input[1].strip()
            for quote in Quotes.objects:
                if tag in quote.tags:
                    print(quote.quote)
        elif text_input[0] == 'tags':
            tags = text_input[1].split(',')
            for quote in Quotes.objects:
                if all(tag in quote.tags for tag in tags):
                    print(quote.quote) 
        else:
            logging.error('Invalid request')


if __name__ == '__main__':
    main_parse()

    setup_log()
    connector()
    
    authors = add_authors()
    quotes = add_quotes()

    fill_data(authors, 'author')
    fill_data(quotes, 'quote')

    search()