import tornado.options
import tornado.web, tornado.ioloop
import config
"""
通过配置文件config.py 来配置变量
"""

class IndexHanlder(tornado.web.RequestHandler):
    """路由处理类"""

    def get(self, ):
        self.write("hello I am domain, this is get request of server")

    def post(self, *args, **kwargs):
        self.write("hello I am domain, this is post request of server")


if __name__ == '__main__':

    tornado.options.parse_config_file("config")

    print("list is ",config.options["port"])
    print("port is ",config.options["list"])


    app = tornado.web.Application(
        [
            (r"/", IndexHanlder)
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(config.options["port"]) #绑定刚刚用options创建的变量 port,所有的定义的变量都存在于 tornado.options.options
    http_server.start(1)
    tornado.ioloop.IOLoop.current().start()

