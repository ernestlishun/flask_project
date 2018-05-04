# coding:utf-8
# 导入Flask类
from flask import Flask, current_app, url_for, request
from werkzeug.routing import BaseConverter

#Flask类接收一个参数__name__
app = Flask(__name__)

@app.route("/id/<path:id>")
def hello_id(id):
    # 通过return字符串返回响应信息
    return "hello id=%s" % id

# @app.route("/id/<name>")
# def hello_id(name):
#     # 通过return字符串返回响应信息
#     return "hello fl=%s" % name

# 装饰器的作用是将路由映射到视图函数index
# @app.route('/')
# def index():
#     return 'Hello World'

# 自定义路由转换器
class ReConverter(BaseConverter):
    """自定义的支持传入正则表达式的转换器"""
    def __init__(self, url_map, *args):
        # 调用父类的初始化方法
        super(ReConverter, self).__init__(url_map)
        # 将传入进来的参数args （是我们在route中定义的正则表达式）保存到对象的regex属性中
        self.regex = args[0]  # args[0]就是我们定义的正则表达式

    def to_python(self, value):
        # 路由从地址中提取参数时使用，其中value为从正则表达式提取的参数，经过to_python调用，将调用的结果返回，再传给视图函数, 可以对value进行相关操作
        return '456'

    def to_url(self, value):
        # 从Python的变量转换到URL时被调用
        return '34'

        # app中维护的所有路由转换器， converters是一个字典
app.url_map.converters["re"] = ReConverter


@app.route("/id/<re('\d{3}'):id>")
def hello(id):
    # 通过return字符串返回响应信息
    return "hello id=%s" % id

@app.route('/redirect')
def redirect_post_only():
    return '<a href=%s>post_only</a>' % url_for('hello', id='123')

@app.route('/')     # 访问时直接加上?name=lishun
def hello_name():
    name = request.args.get('name')
    return 'hello %s' % name

# 文件上传
@app.route('/upload', methods = ['POST'])
def upload():
    # 获取用户上传文件对象， 
    pic_file = request.files.get('pic')
    # Flask应用程序实例的run方法启动WEB服务器
    if pic_file:
        pic_file.save('./ upload_image')
        return 'success'
    else:
        return 'miss pic_file'
if __name__ == '__main__':
    app.run()

