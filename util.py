# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 16:31:46 2020

@author: Korean_Crimson
"""

import sqlite3
import time
import datetime

class DataBaseConnection():
    def __init__(self, db_file):
        self.db_file = db_file
        self.conn = None

    def __enter__(self):
        self.conn = sqlite3.connect(self.db_file)
        return self.conn.cursor()
    
    def __exit__(self, *_):
        self.conn.commit()
        self.conn.close()

def timeit(f):
    def func(*args, **kwargs):
        time0 = time.time()
        result = f(*args, **kwargs)
        print(time.time() - time0)
        return result
    return func

def generate_timestamp():
    return datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

def get_current_date():
    return datetime.datetime.now().strftime('%Y-%m-%d')
