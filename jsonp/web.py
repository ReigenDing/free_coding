# coding=UTF-8
import json
from os import abort

from flask import request, Flask, jsonify, render_template

app = Flask(__name__, template_folder='./template')

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]


@app.route('/todo/api/v1.0/tasks', methods=['POST', "GET"])
def create_task():
    print(request.args)
    # if not request.json or not 'title' in request.json:
    #     abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': "test",
        'description': "hah",
        'done': False
    }
    tasks.append(task)
    # 这里定义callback主要是为了动态返回客户端需要执行的全局函数名称
    callback = request.args.get('callback')
    jsonData = "{\"id\":\"3\", \"name\":\"zhangsan\", \"telephone\":\"13612345678\"}"
    retStr = callback + "(" + json.dumps(task) + ")"
    return retStr


@app.route('/todo/api/v1.0/index', methods=['GET'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run()
