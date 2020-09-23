#!/usr/bin/env python
# encoding: utf-8
import pickledb

db = pickledb.load('example.db', False)
db.set('key', 'value')


if __name__ == '__main__':
    print(db.get('key'))
