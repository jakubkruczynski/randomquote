import os
import django
import csv

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_project.settings')
django.setup()

from quotes.models import Quote

filename = 'data/quotes.csv'  # Replace with the path to your quotes file

with open(filename, newline='', encoding='utf-8') as csvfile:
    quote_reader = csv.reader(csvfile)
    for row in quote_reader:
        text, author = row
        Quote.objects.create(text=text.strip(), author=author.strip())

print("Quotes imported!")