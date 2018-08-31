import tornado.web, tornado.ioloop,tornado.httpserver

"""
httpserver
通过httpserver 创建服务

app_listen中我们说在tornado.web.Application.listen()（示例代码中的app.listen(8000)）的方法中，创建了一个http服务器实例并绑定到给定端口，下面手动通过httpserver来创建这个实例
"""


class IndexHanlder(tornado.web.RequestHandler):
    """路由处理类"""

    def get(self, ):
        self.write("hello I am domain, this is get request of server")

    def post(self, *args, **kwargs):
        self.write("hello I am domain, this is post request of server")


if __name__ == '__main__':
    # 用APPlication生成app对象，里面保存了路由映射表，其初始化接收的第一个参数就是一个路由信息映射元组的列表；其listen(端口)方法用来创建一个http服务器实例，并绑定到给定端口
    app = tornado.web.Application(
        [
            (r"/", IndexHanlder)
        ]
    )
    # ------------------------------
    # 我们修改这个部分
    # app.listen(8000)为：
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.bind(8000) #1.先绑定8000端口
    http_server.start(0)  #2.开启指定线程 默认为1，=none 或者 <=0 为cpu核心数, >0为指定的核心数
    # ------------------------------
    # IOLoop.current:返回当前线程的实例
    # IOLoop.start:启动IoLoop的I/O 循环，同时开启监听
    tornado.ioloop.IOLoop.current().start()




