#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import socket
import json


with socket.create_connection(('localhost', 9090)) as sock:
    url = input("Enter page address: ")
    sock.sendall(url.encode('utf-8'))
    data = sock.recv(1024)
try:
    print(json.loads(data))
except json.JSONDecodeError:
    print(data.decode('utf-8'))
