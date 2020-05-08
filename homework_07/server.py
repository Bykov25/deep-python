#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from bs4.element import Comment
from collections import Counter
import requests
import socket
import json
import re


IGNORED_TAGS = ['head', 'style', 'script', 'meta', 'title', '[document]']
PUNC_CHARS = ['.', ',', ':', ';', '!', '?', '(', ')']

def get_valid_words(word_list):
    word_list = list(filter(lambda w: False if len(w) < 3 else True, word_list))
    i = 0
    for word in word_list:
        if word[-1] in PUNC_CHARS:
            word_list[i] = word[:-1]
            word = word_list[i]
        if word[0] in PUNC_CHARS:
            word_list[i] = word[1:]
        i += 1
    r = re.compile("[а-яА-Яa-zA-Z]{3,}")
    word_list = list(filter(r.match, word_list))
    return word_list

def get_text(req):
    soup = BeautifulSoup(req.text, 'html.parser')
    text = soup.findAll(text=True)
    text = filter(valid_tags, text)
    string = u" ".join(t.strip() for t in text)
    return string
    
def search_most_common(data):
    most_common = dict(Counter(data).most_common(10))
    return json.dumps(most_common)

def valid_tags(item):
    if item.parent.name in IGNORED_TAGS or isinstance(item, Comment):
        return False
    return True

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind(('', 9090))
    sock.listen(10)
    conn, addr = sock.accept()
    conn.settimeout(30)
    with conn:
        while True:
            try:
                url = conn.recv(1024)
                if not url:
                    break
                req = requests.get(url.decode('utf-8'), timeout=3)
                text = get_text(req)
                data = get_valid_words(text.split())
                response = search_most_common(data)
                conn.send(response.encode('utf-8'))
            except socket.timeout:
                print("Close connection by timeout")
                break
            except requests.exceptions.ConnectionError:
                conn.send("ConnectionError".encode('utf-8'))
            except requests.exceptions.MissingSchema:
                conn.send("Invalid URL".encode('utf-8'))
