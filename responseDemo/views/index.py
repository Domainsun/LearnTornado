from tornado.web import RequestHandler
import json, os
from responseDemo import config


class IndexHandler(RequestHandler):
    def get(self):
        url = self.reverse_url("url")
        self.write("<a href='%s'>去home页面</a>" % url)


class HomeHandler(RequestHandler):

    def get(self):
        self.write("weclome to Home!")


class ParameterHandler(RequestHandler):

    def initialize(self, name, age):  # 获取传递过来的值，赋值给self对应的变量，之后就可以通过self调用
        self.name = name
        self.age = age

    def get(self):
        self.write("name:%s age: %s" % (self.name, self.age))


# 响应json数据
class JsonHandler(RequestHandler):

    def get(self):
        data = {
            "name": "domian",
            "age": 18,
            "sex": 1
        }
        self.write(data)


# 设置响应header
class HeaderHandler(RequestHandler):
    def set_default_headers(self):
        self.set_header("Content-Type", "text/html;chartset=utf-8")
        self.set_header("name", "domain")

    def get(self, *args, **kwargs):
        self.write("test for header")
        pass


# 设置响应状态码status
class StatusHandler1(RequestHandler):
    def get(self, *args, **kwargs):
        self.set_status(404)  # 只给状态码，用于已知状态


class StatusHandler2(RequestHandler):
    def get(self, *args, **kwargs):
        self.set_status(999, "未知原因")  # 给状态码和原因，用于未知状态
        self.write(111)


class RedirectHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.redirect('/')


class ErrorHandler(RequestHandler):

    def write_error(self, status_code, **kwargs):
        if status_code == 404:
            code = 404
            self.write("404 错误")
        elif status_code == 500:
            code = 500
            self.write("500 错误")

    def get(self, *args, **kwargs):
        flag = self.get_query_argument("flag")
        if flag == "0":  # flas参数为0，发送error，error code为404，send_error之后，下面的代码不执行，跳到write_error
            self.send_error(404)
        elif flag == "2":  # flas参数为2，发送error，error code为500
            self.send_error(500)
        self.write("you are right ")  # flas参数不为2和0，输出 "you are right"


class GetUriHandler(RequestHandler):
    def get(self, h1, h2, h3, *args, **kwargs):
        print(h1 + "-" + h2 + "-" + h3)
        self.write("get uri successful.")


class GetParameter(RequestHandler):

    def get(self, *args, **kwargs):
        # 通过self.get_query_argument获取url传递过来的参数，同名参数以最后一个为准
        parameter1 = self.get_query_argument(name="parameter1", default="defaultParamter",
                                             strip=True)  # name：key 名字、default：默认值、strip:值去除左右空格。不传递值和不设置默认值，抛出缺少参数异常
        parameter2 = self.get_query_argument(name="parameter2", default="defaultParamter", strip=True)
        parameter3 = self.get_query_argument(name="parameter3", default="defaultParamter", strip=True)
        # self.write("Get Parameter:parameter1 is %s parameter2 is %s parameter3 is %s"%(parameter1,parameter2,parameter3))

        # 通过self.get_query_arguments 获取多个同名参数
        parameters = self.get_query_arguments('name')
        print(parameters[0], parameters[1])
        self.write(parameters[0] + parameters[1])


class LoginHandler(RequestHandler):

    def get(self, *args, **kwargs):  # get 方式返回login 界面 html
        self.render('login.html', num=100, list=["hello", "domain"])

    def post(self, *args, **kwargs):  # post 方式处理登陆逻辑
        user = self.get_body_argument("user", "", False)
        password = self.get_body_argument("password", "", False)
        hobbyList = self.get_body_arguments("hobby")

        print(user, password, hobbyList)


class GetAndPostParameter(RequestHandler):

    def get(self, *args, **kwargs):
        name = self.get_argument("name")  # 在get请求中用self.get_argument("name") 获取传递过来的参数
        self.write("name in get:" + name)
        print("name in get:" + name)

    def post(self, *args, **kwargs):
        name = self.get_argument("name")  # 在post请求中用self.get_argument("name") 获取传递过来的参数
        print("name in post" + name)
        self.write("name in post" + name)


class RequestObjectHandler(RequestHandler):
    def get(self, *args, **kwargs):
        print(self.request.method)
        print(self.request.host)
        print(self.request.uri)
        print(self.request.query)
        print(self.request.version)
        print(self.request.headers)
        print(self.request.remote_ip)
        print(self.request.files)


class UpFileHandler(RequestHandler):

    def get(self, *args, **kwargs):
        # self.write("successful")
        self.render('upfile.html')

    def post(self, *args, **kwargs):
        fileDict = self.request.files
        print(fileDict)

        for input_name in fileDict:
            file_list = fileDict[input_name]
            for file_obj in file_list:
                file_path = os.path.join(config.BASE_DIRS, "upfile/" + file_obj.filename)
                with open(file_path, "wb") as f:
                    f.write(file_obj.body)

        self.write("upload successful")


# self.write响应请求
class WriteHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.write("hello")
        self.write("domain")
        self.write("world")
        # 刷新当前缓冲区，关闭单次请求通道，finish之后的write无效
        self.finish()


class CallOrderHandler(RequestHandler):
    def set_default_headers(self):
        print("set default headers")

    def initialize(self):
        print("initialize")

    def prepare(self):
        print("prepare")

    def get(self, *args, **kwargs):
        print("get")

    def write_error(self, status_code, **kwargs):
        print("write error")

    def on_finish(self):
        print("on finish")


class TemplatesHandler(RequestHandler):
    def get(self, *args, **kwargs):  # get 方式返回界面 html,并向html 传递变量 列表 字典
        num = 100
        list = ["hello", "domain"]
        dic = {
            "name": "domain",
            "age": 18,
            "sex": "男"
        }
        self.render('templatesDemo.html', num=num, list=list, dic=dic)


class FunctionHandler(RequestHandler):
    def get(self, *args, **kwargs):  # get 方式返回界面 html,并向html 传递变量 列表 字典
        def func(n):
            n = n + 100
            return n

        self.render('function.html', func=func)


class TransHandler(RequestHandler):
    def get(self, *args, **kwargs):  # get 方式返回界面 html,并向html 传递变量 str
        str1 = "<h1>hello</h1>"
        self.render('trans.html', str1=str1)


class shopCartHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('shopCart.html')

class studentsHandler(RequestHandler):
    def get(self, *args, **kwargs):
        self.render('students.html')
