#!/usr/bin/env python
# encoding: utf-8
from abc import ABC

import tornado.web
import tornado.ioloop


class MainHandler(tornado.web.RequestHandler, ABC):
    def get(self):
        self.write("hello, world")


def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()