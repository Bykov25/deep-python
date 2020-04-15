#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sqlite3
import datetime


class MyBase:
    
    def __init__(self, db_name):
        self.conn = sqlite3.connect(db_name)
        self.cursor = self.conn.cursor()
        self.execute = self.cursor.execute
        self.commit = self.conn.commit
        self.close = self.conn.close
    
    def get_data(self, sql_query):
        self.execute(sql_query)
        return self.cursor.fetchall()


class Base:
    
    __flag = None
    
    @classmethod
    def conn(cls, db_name):
        if not cls.__flag:
            cls.__flag = MyBase(db_name)
            
    @classmethod
    def conn_close(cls):
        Base.__flag.close()
        Base.__flag = None
    
    @classmethod
    def create_table(cls):
        tablename = cls.__name__
        attrs = [col for col in dict(cls.__dict__).keys() if not col.startswith('__')]
        cols = ', '.join(attrs)
        sql_query = f"CREATE TABLE {tablename} ({cols})"
        try:
            Base.__flag.execute(sql_query)
            Base.__flag.commit()
        except sqlite3.OperationalError as e:
            return e
        
    def insert(self):
        name = self.__class__.__name__
        cols = ', '.join([col for col in self.__dict__.keys()])
        if cols == '':
            return "Try to add an empty entry to the database"
        values = ', '.join([f"'{val}'" if isinstance(val, str) else f"{val}" for key, val in self.__dict__.items()])
        sql_query = f"INSERT INTO {name} ({cols}) VALUES ({values})"
        try:
            Base.__flag.execute(sql_query)
            Base.__flag.commit()
        except sqlite3.OperationalError as e:
            return e
    
    @classmethod
    def select(cls, *args, **kwargs):
        if not args:
            cols = "*"
        else:
            cols = ', '.join(args)
        if not kwargs:
            where = ""
        else:
            lst = []
            for key, val in kwargs.items():
                if isinstance(val, str):
                    string = f"{key}='{val}'"
                else:
                    string = f"{key}={val}"
                lst.append(string)
            where = " WHERE " + ' AND '.join(lst)
        sql_query = f"SELECT {cols} FROM {cls.__name__}" + where
        resp = cls.__flag.get_data(sql_query)
        if kwargs and args:
            attrs = args
        elif args or kwargs:
            if args:
                attrs = args
            if kwargs:
                attrs = [v for v in cls.__dict__.keys() if not v.startswith('__')]
        else:
            attrs = [v for v in cls.__dict__.keys() if not v.startswith('__')]
        result = []
        for s in resp:
            result.append(dict(zip(attrs, s)))
        return result
    
    @classmethod            
    def delete(cls, **kwargs):
        if not kwargs:
            where = ""
        else:
            lst = []
            for key, val in kwargs.items():
                if isinstance(val, str):
                    string = f"{key}='{val}'"
                else:
                    string = f"{key}={val}"
                lst.append(string)
            where = " WHERE " + ' AND '.join(lst)
        sql_query = f"DELETE FROM {cls.__name__}" + where
        cls.__flag.execute(sql_query)
        cls.__flag.commit()
    
    @classmethod
    def update(cls, col, value, **kwargs):
        if not kwargs:
            return "No settable values"
        lst = []
        for key, val in kwargs.items():
            if isinstance(val, str):
                string = f"{key}='{val}'"
            else:
                string = f"{key}={val}"
            lst.append(string)
        sets = " SET " + ', '.join(lst)
        if isinstance(value, str):
            where = f" WHERE {col}='{value}'"
        else:
            where = f" WHERE {col}={value}"
        sql_query = f"UPDATE {cls.__name__}" + sets + where
        cls.__flag.execute(sql_query)
        cls.__flag.commit()

        
class Column:
    
    def __get__(self, obj, cls):
        return obj.__dict__[self.name]
    
    def __delete__(self, obj):
        del obj.__dict__[self.name]
    
    def __set_name__(self, cls, name):
            self.name = name
    
class IntegerField(Column):
                      
    def __set__(self, obj, val):
        if isinstance(val, int):
            obj.__dict__[self.name] = val
        else:
            raise TypeError
    
class FloatField(Column):
        
    def __set__(self, obj, val):
        if isinstance(val, float):
            obj.__dict__[self.name] = val
        else:
            raise TypeError

class StringField(Column):
        
    def __init__(self, max_len):
        self.max_len = max_len
        
    def __set__(self, obj, val):
        if isinstance(val, str):
            if len(val) > self.max_len:
                print("too long")
            obj.__dict__[self.name] = val
        else:
            raise TypeError

class DateTimeField(Column):
    
    def __set__(self, obj, val):
        if isinstance(val, datetime.datetime):
            obj.__dict__[self.name] = str(val)
        else:
            raise TypeError

class TimeField(Column):
    
    def __set__(self, obj, val):
        if isinstance(val, datetime.time):
            obj.__dict__[self.name] = str(val)
        else:
            raise TypeError
