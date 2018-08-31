import tornado.options
import tornado.web, tornado.ioloop

# options定义一个变量port,默认值为8000,类型为int
tornado.options.define("port", default=8000, type=int, help="这是一个端口号的定义")
# 定义一个变量list,默认值为[],类型为str,可有多个值
tornado.options.define("list", default=[], type=str, multiple=True)


class IndexHanlder(tornado.web.RequestHandler):
    """路由处理类"""

    def get(self, ):
        self.write("hello I am domain, this is get request of server")

    def post(self, *args, **kwargs):
        self.write("hello I am domain, this is post request of server")


if __name__ == '__main__':
    tornado.options.options.parse_command_line()  # 支持命令行输入参数，转换命令行参数，并将转换后的值对应的设置到全局options对象相关属性上。

    print("list is ", tornado.options.options.list)
    print("port is ", tornado.options.options.port)

    app = tornado.web.Application(
        [
            (r"/", IndexHanlder)
        ]
    )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(tornado.options.options.port)  # 绑定刚刚用options创建的变量 port,所有的定义的变量都存在于 tornado.options.options
    http_server.start(1)
    tornado.ioloop.IOLoop.current().start()
