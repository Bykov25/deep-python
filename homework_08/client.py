#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import sys
import json
from concurrent.futures import ThreadPoolExecutor


def worker(url):
    sock.sendall(url.encode('utf-8'))
    data = sock.recv(1024)
    try:
        print(json.loads(data))
    except json.JSONDecodeError:
        print(data.decode('utf-8'))

def create_data(filename):
    with open(filename, 'r') as file:
        list_of_urls = file.read().splitlines()
    new_list = []
    for url in list_of_urls:
        new_list.append(url + ' ')
    return list_of_urls

if __name__ == "__main__":
    filename = sys.argv[1]
    n_threads = sys.argv[2]
    data = create_data(filename)
    with socket.create_connection(('localhost', 9090)) as sock:
        with ThreadPoolExecutor(max_workers=int(n_threads)) as pool:
            pool.map(worker, data)
