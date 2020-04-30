#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
from collections import Counter
import requests
import re


req = requests.get("https://mail.ru")
soup = BeautifulSoup(req.text, 'html.parser')
r = re.compile("[а-яА-Я]+")
#r = re.compile("")
lst = soup.get_text().split()
result = [w for w in filter(r.match, lst)]
print(result)

