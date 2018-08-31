import tornado.web, tornado.ioloop

"""
web:tornado的基础web模块
ioloop:tornado的核心IO循环模块,是tornado高效的基础

"""

class IndexHanlder(tornado.web.RequestHandler):
    """路由处理类"""

    def get(self, ):
        """get请求方法"""
        self.write("hello I am domain, this is get request") #输出一句话

    def post(self, *args, **kwargs):
        """post请求方法"""
        self.write("hello I am domain, this is post request") #输出一句话


if __name__ == '__main__':
    # 用APPlication生成app对象，里面保存了路由映射表，其初始化接收的第一个参数就是一个路由信息映射元组的列表；其listen(端口)方法用来创建一个http服务器实例，并绑定到8000端口
    app = tornado.web.Application(
        [
            (r"/", IndexHanlder)
        ]
    )
    app.listen(8000)

    #IOLoop.current:返回当前线程的实例
    #IOLoop.start:启动IoLoop的I/O 循环，同时开启监听
    tornado.ioloop.IOLoop.current().start()



