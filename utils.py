import logging

from mongoengine import StringField, ListField, Document, ReferenceField


def setup_log():
    logging.basicConfig(
        filename='file.log',
        level=logging.INFO, 
        format='%(asctime)s - %(levelname)s - %(message)s'
        )


class Author(Document):
    fullname = StringField()
    born_date = StringField()
    born_location = StringField()
    description = StringField()

class Quotes(Document):
    tags = ListField()
    author = ReferenceField(Author)
    quote = StringField()