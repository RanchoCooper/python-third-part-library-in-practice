#!/usr/bin/env python
# encoding: utf-8
from abc import ABC

import tornado.ioloop
import tornado.web


class zi(tornado.web.RequestHandler, ABC):
    def get(self, uid):
        self.write("hello your uid is %s" % uid)


if __name__ == '__main__':
    app = tornado.web.Application([
        (r"/(0-9+)", zi),
    ], debug=True)

    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
