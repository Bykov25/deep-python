#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import json


def url_handler(sock, url):
    if not url:
        print("URL was not entered")
    else:    
        sock.sendall(url.encode('utf-8'))
        data = sock.recv(1024)
        try:
            print(json.loads(data))
        except json.JSONDecodeError:
            print(data.decode('utf-8'))


if __name__ == "__main__":
    with socket.create_connection(('localhost', 9090)) as sock:
        url = input("Enter page address: ")
        url_handler(sock, url)