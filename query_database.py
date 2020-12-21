# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 17:09:26 2020

@author: Korean_Crimson
"""

import time
from util import DataBaseConnection

def timeit(f):
    def func(*args, **kwargs):
        time0 = time.time()
        result = f(*args, **kwargs)
        print(time.time() - time0)
        return result
    return func

@timeit
def user_test_1(cursor):
    #get name, number of transactions, total cost of all male users that spent over 1000 euro and were born in 2004
    data = cursor.execute('SELECT l.first_name, l.last_name, l.dob, COUNT(*), SUM(r.cost) FROM users l INNER JOIN transactions r ON l.user_id = r.user_id WHERE l.gender="m" AND l.dob GLOB "2004*" GROUP BY r.user_id HAVING SUM(r.cost) > 1000 ORDER BY SUM(r.cost)')
    for row in data:
        print(row)

with DataBaseConnection('main.db') as cursor:
    data = cursor.execute('SELECT * FROM users LIMIT 100')
    for row in data:
        print(row)

    data = cursor.execute('SELECT date, cost, user_id FROM transactions ORDER BY cost ASC LIMIT 10')
    for row in data:
        pass
    
    data = cursor.execute('SELECT user_id, COUNT(*), SUM(cost) FROM transactions GROUP BY user_id HAVING COUNT(*) > 20 ORDER BY SUM(cost) DESC')
    for row in data:
        print(row)

    data = cursor.execute('SELECT user_id FROM users WHERE last_name LIKE "P%s" ORDER BY first_name')
    user_id = [point for point in data][0]
    data = cursor.execute('SELECT * FROM transactions WHERE user_id IN (?)', user_id)
    for row in data:
        print(row)

    user_test_1(cursor)