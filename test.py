#蓝图应用不分路由类测试
from flask import Flask
from flask import Blueprint


test = Blueprint('test',__name__)

app = Flask(__name__)


@test.route('/')
def show():
    return 'test Page'


app.register_blueprint(test)

if __name__ == '__main__':
    app.run()

