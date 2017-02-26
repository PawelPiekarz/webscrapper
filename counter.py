import re
from lxml import html
import requests
import collections
import json
from peewee import *

database = SqliteDatabase('counter.db')


class Text(Model):
    text = TextField(unique=True)
    class Meta:
        database = database


def most_common(sentence):
    #cleaning sentence, lower case, counting words in sentence
    #returning top 10 words
    words = re.findall(r'\w+', sentence.lower())
    m_comm = collections.Counter(words).most_common(10)

    return m_comm


def request_words(url):
    #returning article in pointed section on requested site
    page = requests.get(url)
    tree = html.fromstring(page.content)
    html_resp = tree.xpath('//*[@id="content"]/main/article[*]/section/p/text()')
    return ' '.join(html_resp)


def request_urls(url):
    #finding links to articles on site
    #returning them as a list
    links_list = []
    pref = url
    page = requests.get(url)
    tree = html.fromstring(page.content)
    for link_element in tree.xpath('//*[@id="content"]/main/article[*]/section/div/a'):
        href = link_element.get('href')
        full_link = pref + href
        links_list.append(full_link)
    return links_list


def make_texts_list():
    #making a list with texts in articles at found urls
    texts_list = []
    for link in request_urls('http://build.sh'):
        texts_list.append(request_words(link))

    return texts_list


def put_in_database():
    #saving/updating database
   for text in make_texts_list():
        try:
            Text.create(text=text)
        except IntegrityError:
            Text.update(text=text)


def get_and_count():
    #get sentences from db and find most common words
    entries = Text.select()
    text_list_for_stats = []
    for entry in entries:
        text_list_for_stats.append(entry.text)
    joined = ' '.join(text_list_for_stats)
    return most_common(joined)


def run():
    #main function
    #run database and scrapping
    database.connect()
    database.create_tables([Text], safe=True)
    put_in_database()

    #return most common words found in database
    return(dict(get_and_count()))