#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from nltk.corpus import stopwords
from bs4.element import Comment
from bs4 import BeautifulSoup
from collections import Counter
import requests
import socket
import json
import nltk
import re


IGNORED_TAGS = ['head', 'style', 'script', 'meta', 'title', '[document]']

def get_valid_words(word_list):
    r = re.compile("[а-яА-Яa-zA-Z]")
    word_list = list(filter(r.match, word_list))
    stop_words_rus = stopwords.words('russian')
    stop_words_eng = stopwords.words('english')
    stop_words = stop_words_rus + stop_words_eng
    word_list = list(filter(lambda w: w.lower() not in stop_words, word_list))
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

def conn_client(sock):
    conn, addr = sock.accept()
    conn.settimeout(30)
    return conn, addr

def create_response(conn, addr):
    while True:
        try:
            url = conn.recv(1024)
            if not url:
                break
            req = requests.get(url.decode('utf-8'), timeout=3)
            text = get_text(req)
            text = nltk.word_tokenize(text)
            data = get_valid_words(text)
            response = search_most_common(data)
            conn.send(response.encode('utf-8'))
        except socket.timeout:
            print("Close connection by timeout from addr: ", addr)
            break
        except requests.exceptions.ConnectionError:
            conn.send("ConnectionError".encode('utf-8'))
        except requests.exceptions.MissingSchema:
            conn.send("Invalid URL".encode('utf-8'))

def run_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        sock.bind((host, port))
        sock.listen(10)
        while True:
            conn, addr = conn_client(sock)
            with conn:
                create_response(conn, addr)

if __name__ == "__main__":
    run_server('', 9090)
