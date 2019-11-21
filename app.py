#导入flask模块
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config

#导入注册的蓝图
from api.testHello import testHello
from api.testGoodBye import testGoodBye

#定义app
app = Flask(__name__)
app.config.from_object(config)

#注册蓝图到app
app.register_blueprint(testHello)
app.register_blueprint(testGoodBye)

db = SQLAlchemy(app)

# class Country(db.Model)

#程序入口
if __name__ == '__main__':
    print(db)
    app.run()
