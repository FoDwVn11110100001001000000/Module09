import logging

from faker import Faker

from mongoengine import Document
from mongoengine.fields import StringField, BooleanField


fake = Faker(['uk_UA'])

class Newsletter(Document):
    name = StringField(unique=True)
    email = StringField()
    phone = StringField()
    job = StringField()
    check = BooleanField(default=False)

def seed():
    customer = Newsletter(
        name = fake.name(),
        email = fake.email(),
        phone = fake.phone_number(),
        job = fake.job(),
        check = False
    )
    customer.save()









