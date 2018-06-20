from flask import Flask  #模块名字 flask 从flask模块导入Flask类
from vsearch import search4letters
app = Flask(__name__) #创建Flask对象的一个实例，并把它赋值给“app”
@app.route('/')
def hello()->str:
    return "hello world from flask!"
@app.route('/search4')
def do_search()->str:
    return str(search4letters('life,the universe,and everything','eiru,!'))
app.run()