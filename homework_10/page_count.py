#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


def pdf_page_count(filename):
    with open(filename, 'rb') as file:
        data = file.read().splitlines()
    head = data[3].split()
    for i in range(len(head)):
        if head[i] == b'/N':
            return int(head[i + 1])

if __name__ == "__main__":
    filename = sys.argv[1]
    print(pdf_page_count(filename))
