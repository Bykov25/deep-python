#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys


class Theater:

    def __init__(self, filename):
        self.filename = filename
        with open(self.filename, 'r') as file:
            data = file.read().splitlines()
        self.data = data

    def num_free_places(self):
        places = ''.join(self.data)
        return places.count('0')

    def check_place(self, row, place):
        places = []
        row = int(row)
        place = int(place)
        for line in self.data:
            places.append(line.split())
        if row > len(places) or place > len(places[0]) or row <= 0 or place <= 0:
            return "There is no such place"
        if places[row - 1][place - 1] == '1':
            return "Place is not free"
        else:
            return "Place is free"

def check():
    row = sys.argv[2]
    place = sys.argv[3]
    return theater.check_place(row, place)

if __name__ == "__main__":
    filename = sys.argv[1]
    theater = Theater(filename)
    free_places = theater.num_free_places()
    print("Number of free places:", free_places)
    if len(sys.argv) == 4:
        is_free = check()
        print(is_free)
