#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from MyORM import Base, IntegerField, FloatField, StringField, DateTimeField, TimeField
import datetime
import pytest


class Book(Base):
    id_ = IntegerField()
    name = StringField(max_len=30)
    cost = FloatField()
    date = DateTimeField()
    tm = TimeField()

@pytest.fixture()
def init_db():
    Base.conn("C:/sqlite/test.db")
    Book.create_table()
    yield
    Base.conn_close()

def test_1(init_db):
    book1 = Book()
    book1.id_ = 1
    book1.name = "Harry Potter"
    book1.cost = 20.5
    book1.date = datetime.datetime(2020, 4, 12)
    book1.tm = datetime.time(12, 45, 30)
    book1.insert()
    book2 = Book()
    book2.id_ = 2
    book2.name = "The Great Gatsby"
    book2.cost = 24.1
    book2.date = datetime.datetime(2020, 3, 25)
    book2.tm = datetime.time(7, 35, 21)
    book2.insert()
    assert Book.select() == [{'id_': 1, 'name': 'Harry Potter', 'cost': 20.5, 'date': '2020-04-12 00:00:00', 'tm': '12:45:30'},
                             {'id_': 2, 'name': 'The Great Gatsby', 'cost': 24.1, 'date': '2020-03-25 00:00:00', 'tm': '07:35:21'}]
    assert Book.select('name', 'cost') == [{'name': 'Harry Potter', 'cost': 20.5},
                                           {'name': 'The Great Gatsby', 'cost': 24.1}]
    assert Book.select('cost', id_=1) == [{'cost': 20.5}]


def test_2(init_db):
    Book.update('name', 'Harry Potter', cost=30.1)
    Book.update('name', 'The Great Gatsby', cost=36.8)
    assert Book.select('name', 'cost') == [{'name': 'Harry Potter', 'cost': 30.1},
                                           {'name': 'The Great Gatsby', 'cost': 36.8}]


def test_3(init_db):
    Book.delete(name='Harry Potter')
    assert Book.select() == [{'id_': 2, 'name': 'The Great Gatsby', 'cost': 36.8, 'date': '2020-03-25 00:00:00', 'tm': '07:35:21'}]


def test_4(init_db):
    d = datetime.datetime(2020, 5, 8)
    Book.update('name', 'The Great Gatsby', date=str(d))
    assert Book.select('date', name='The Great Gatsby') == [{'date': '2020-05-08 00:00:00'}]
    assert Book.update('name', 'The Great Gatsby') == "No settable values"


def test_5(init_db):
    Book.delete()
    assert Book.select() == []
