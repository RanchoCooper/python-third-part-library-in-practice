#!/usr/bin/env python
# encoding: utf-8
import tornado.ioloop
import tornado.web

html_txt = """
<!DOCTYPE html>
<html>
    <body>
        <h2>收到GET请求</h2>
        <form method='post'>
        <input type='text' name='name' placeholder='请输入你的姓名'/>
        <input type='submit' value='发送POST请求'/>
        </form>
    </body>
</html>
"""


class zi(tornado.web.RequestHandler):
    def get(self):
        self.write(html_txt)

    def post(self):
        name = self.get_argument('name', default='匿名', strip=True)
        self.write("你的姓名是%s" % name)


if __name__ == '__main__':
    app = tornado.web.Application([
        (r'/get', zi),
    ], debug=True)
    app.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
