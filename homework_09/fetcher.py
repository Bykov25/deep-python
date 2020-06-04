#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import nltk
import re
import sys
import aiohttp
import asyncio
import time
from nltk.corpus import stopwords
from bs4.element import Comment
from bs4 import BeautifulSoup
from collections import Counter


IGNORED_TAGS = ['head', 'style', 'script', 'meta', 'title', '[document]']
STOP_WORDS = stopwords.words('russian') + stopwords.words('english')

class Response:

    def __init__(self, req):
        self.req = req

    def create_response(self):
        text = Response.get_text(self.req)
        text = nltk.word_tokenize(text)
        data = Response.get_valid_words(text)
        resp = self.search_most_common(data)
        return resp

    @staticmethod
    def get_text(req):
        soup = BeautifulSoup(req, 'html.parser')
        text = soup.findAll(text=True)
        text = filter(Response.valid_tags, text)
        string = u" ".join(t.strip() for t in text)
        return string

    @staticmethod
    def get_valid_words(word_list):
        r = re.compile("[а-яА-Яa-zA-Z]")
        word_list = list(filter(r.match, word_list))
        word_list = list(filter(lambda w: w.lower() not in STOP_WORDS, word_list))
        return word_list

    @staticmethod
    def valid_tags(item):
        if item.parent.name in IGNORED_TAGS or isinstance(item, Comment):
            return False
        return True

    def search_most_common(self, data):
        most_common = dict(Counter(data).most_common(10))
        return most_common

async def get_data(url, session):
    try:
        async with session.get(url) as resp:
            req = await resp.text()
            resp = Response(req)
            response = resp.create_response()
            print(response)
    except aiohttp.client_exceptions.ClientConnectionError:
        print(f"ConnectionError by url: {url}")
    except asyncio.TimeoutError:
        print(f"TimeoutError by url: {url}")
    except aiohttp.client_exceptions.TooManyRedirects:
        pass

async def main(filename, *count):
    with open(filename, "r") as f:
        urls = f.read().splitlines() 
    if count:
        cnt = count[0]
    else:
        cnt = len(urls)
    tasks = set()
    timeout = aiohttp.ClientTimeout(total=7)
    async with aiohttp.ClientSession(timeout=timeout) as session:
        for url in urls:
            if len(tasks) >= int(cnt):
                _done, tasks = await asyncio.wait(tasks, return_when=asyncio.FIRST_COMPLETED)
            tasks.add(asyncio.create_task(get_data(url, session)))
        await asyncio.wait(tasks)

if __name__ == "__main__":
    start = time.time()
    if len(sys.argv) == 4:
        count = sys.argv[2]
        filename = sys.argv[3]
        asyncio.run(main(filename, count))
    else:
        filename = sys.argv[1]
        asyncio.run(main(filename))
    print(time.time() - start)
