#!/usr/bin/env python
# encoding: utf-8
from abc import ABC

import tornado.ioloop
import tornado.web
import tornado.escape


class aaaa(tornado.web.RequestHandler, ABC):
    def get(self):
        self.set_cookie('odn_cookie', tornado.escape.url_escape("未加密cookie串"))
        self.set_secure_cookie('scr_cookie', "加密cookie串")
        self.write("<a href='/shcook>查看设置的cookie</a>")


class shcookHdl(tornado.web.RequestHandler, ABC):
    def get(self):
        odn_cookie = tornado.escape.url_unescape(self.get_cookie('odn_cookie'))
        scr_cookie = self.get_secure_cookie('scr_cookie').decode('utf-8')
        self.write("普通cookie:%s, <br/>安全cookie:%s" % (odn_cookie, scr_cookie))


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/sscook', aaaa),
        (r'/shcook', shcookHdl),
    ], cookie_secret='1234asdf')
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
