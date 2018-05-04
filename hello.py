# coding:utf-8
# 导入Flask类
from flask import Flask, current_app, url_for

#Flask类接收一个参数__name__
app = Flask(__name__
            # static_url_path="/python",  # 控制访问静态资源url的前缀， 默认是static
            # static_folder="static",  # 存放静态文件的文件夹，默认是static
            # template_folder="templates",  # 存放模板文件的文件夹，默认是templates
            )

# 为flask添加配置参数
# 通过配置文件读取配置参数
# app.config.from_pyfile("MyConfig.cfg")

# 通过对象的方式读取配置参数
class MyConfig(object):
    """配置信息"""
    DEBUG = True
    ITCAST = "python"

app.config.from_object(MyConfig)

# 装饰器的作用是将路由映射到视图函数index
@app.route('/')
def hello():
    # a = 1 / 0
    # 在视图函数中读取配置参数
    # print(app.config.get("ITCAST"))
    # 或者
    print(current_app.config.get("ITCAST"))
    return 'Hello World'

# @app.route('/') 同一个路由装饰多个视图
# def hello1():
#     # a = 1 / 0
#     # 在视图函数中读取配置参数
#     # print(app.config.get("ITCAST"))
#     # 或者
#     # print(current_app.config.get("ITCAST"))
#     return 'Hello 1'

# 一个视图函数中出现多个路径，添加多个装饰器
# @app.route('/index')

# 对于请求方式限制的演示
# @app.route('/hi', methods=['POST', 'GET'])
# def index():
#     return 'index page'
@app.route('/itcast')
def itcast():
    return 'index page'

@app.route('/hi')
def index():
    return "<a href='/itcast'>post_only</a>"

@app.route('/redirect')
def redirect_post_only():
    return '<a href=%s>post_only</a>' % url_for('index')

# Flask应用程序实例的run方法启动WEB服务器
if __name__ == '__main__':
    # 查看所有的路由映射
    print(app.url_map)
    app.run(host='0.0.0.0', port=5000)

