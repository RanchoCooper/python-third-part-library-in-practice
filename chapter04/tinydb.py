#!/usr/bin/env python
# encoding: utf-8
from tinydb import TinyDB, Query, where

if __name__ == '__main__':
    db = TinyDB('db.json')
    db.insert({'name': 'rancho', 'age': 26})
    db.insert({'name': 'cooper', 'age': 27})
    print(db.all())

    # 查询
    user = Query()
    print(db.search(user.name == 'cooper'))
    print(db.search(where('name') == 'rancho'))

    # 更新
    db.update({'age': 10}, where('name') == 'rancho')
    db.remove(where('age') > 20)

    # 清空数据库
    db.purge()
