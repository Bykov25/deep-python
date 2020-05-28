#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import requests
import time
import queue
import threading
import json
import nltk
import re
from nltk.corpus import stopwords
from bs4.element import Comment
from bs4 import BeautifulSoup
from collections import Counter
from serv_config import N_MOST_COMMON, N_WORKERS


IGNORED_TAGS = ['head', 'style', 'script', 'meta', 'title', '[document]']
STOP_WORDS = stopwords.words('russian') + stopwords.words('english')

class Response:

    def __init__(self, req, url):
        self.req = req
        self.url = url

    def create_response(self):
        text = Response.get_text(self.req)
        text = nltk.word_tokenize(text)
        data = Response.get_valid_words(text)
        resp = self.search_most_common(data)
        return resp

    @staticmethod
    def get_text(req):
        soup = BeautifulSoup(req.text, 'html.parser')
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
        most_common = dict(Counter(data).most_common(N_MOST_COMMON))
        most_common['url'] = self.url
        return json.dumps(most_common)


class Worker(threading.Thread):
    
    def __init__(self, queue):
        super().__init__()
        self.__queue = queue
        self.need_exit = False
        self.daemon = True
        self.start()

    def run(self):
        while not self.need_exit:
            try:
                conn, url = self.__queue.get_nowait()
                req = requests.get(url, timeout=3)
                resp = Response(req, url)
                response = resp.create_response()
                conn.sendall(response.encode('utf-8'))
                self.__queue.task_done()
            except queue.Empty:
                time.sleep(0.1)
            except (requests.exceptions.ConnectionError, requests.exceptions.ReadTimeout):
                conn.sendall(f'ConnectionError by url {url}'.encode('utf-8'))
                self.__queue.task_done()
            except requests.exceptions.MissingSchema:
                conn.sendall(f'{url} - Invalid URL'.encode('utf-8'))
                self.__queue.task_done()


class Server(threading.Thread):

    def __init__(self, port, queue):
        super().__init__()
        self.__queue = queue
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.socket.bind(('localhost', port))
        self.start()

    def run(self):
        self.socket.listen(5)
        while True:
            conn, addr = self.socket.accept()
            with conn:
                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    tasks = data.decode('utf-8').split()
                    if len(tasks) > 1:
                        for task in tasks:
                            self.__queue.put((conn, task))
                    else:
                        self.__queue.put((conn, tasks[0]))


class Master:

    def __init__(self, n_workers):
        self.queue = queue.Queue()
        self.n_workers = n_workers
        self.server = Server(9090, self.queue) 
        self.threads = []
        self.start_threads()
    
    def start_threads(self):
        if self.threads:
            self.stop_threads()
        self.threads = [Worker(self.queue) for _ in range(self.n_workers)]

    def stop_threads(self):
        for item in self.threads:
            item.need_exit = True
            item.join()

    def main(self):  
        while True:
            self.start_threads()


if __name__ == "__main__":
    m = Master(N_WORKERS)
    m.main()
       