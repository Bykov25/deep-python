#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import xlwt
import sys
import datetime


def handler(path, level):
    result = []
    level += 1
    for item in os.listdir(path):
        full_path = os.path.join(path, item)
        info = {}
        if os.path.isfile(full_path):
            if not item.startswith('.'):
                info["name"] = item
                info["type"] = "file"
                info["size"] = os.path.getsize(full_path)
                info["date_of_change"] = get_time(os.path.getmtime(full_path))
                info["full_path"] = full_path
                info["level"] = level
                result.append(info)
        if os.path.isdir(full_path):
            if not item.startswith('.'):
                info["name"] = item
                info["type"] = "dir"
                info["size"] = size_of_dir(full_path)
                info["date_of_change"] = get_time(os.path.getmtime(full_path))
                info["full_path"] = full_path
                info["level"] = level
                result.append(info)
                result += handler(full_path, level)
    return result

def size_of_dir(path_to_dir):
    size = 0
    for _dir, _, files in os.walk(path_to_dir):
        for file in files:
            if os.path.isfile(path_to_dir + file):
                size += os.path.getsize(os.path.join(_dir, file))
    return size

def get_time(sec):
    return datetime.datetime.fromtimestamp(sec).strftime('%Y-%m-%d %H:%M:%S')

def create_excel(name):
    data = handler(path, 0)
    if not data:
        return "Empty directory"
    book = xlwt.Workbook('utf8')
    sheet = book.add_sheet('list1')
    rows = list(data[0].keys())
    for i in range(len(rows)):
        sheet.write(0, i, rows[i])
    col = 0
    row = 1
    for elem in data:
        col = 0
        for _, val in elem.items():
            sheet.write(row, col, val)
            col += 1
        row += 1        
    sheet.portrait = False
    book.save(name + '.xls')

if __name__ == "__main__":
    path = sys.argv[1]
    tmp = path.split('/')
    if tmp[-1] == '':
        name = tmp[-2]
    else:
        name = tmp[-1]
    create_excel(name)
