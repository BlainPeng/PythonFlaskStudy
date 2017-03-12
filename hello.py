# -*- coding:utf-8 -*-
# 导入Flask模块
from flask import Flask
from flask import redirect
from flask_script import Manager
# 创建一个程序实例，该实例就是Flask类的对象
app = Flask(__name__)
manager = Manager(app)

# 处理URL和函数之间的关系称为路由。当在客户端输入url时就会触发
# 服务器执行index函数，这个函数的返回值称为响应
@app.route('/')
# 像这种函数被称为视图函数
def index():
    return '<h1>Hello World</h1>'

# 路由中的尖括号中内容就是动态部分，调用视图函数时，Flask会将动态部分作为参数传入函数
# 动态部分也可使用类型定义，如：/user/<int:id>
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' % name

@app.route('/hello')
def set_redirect():
    return redirect('http://www.baidu.com')

# 启动服务器
if __name__ == '__main__':
    # 程序实例用run方法启动Flask集成的开发Web服务器
    # app.run(debug = True)
    manager.run()
