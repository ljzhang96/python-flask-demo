#导入flask模块
from flask import Flask,jsonify
from flask_sqlalchemy import SQLAlchemy
import config   #数据库配置
import logging  #日志配置
from logging.handlers import RotatingFileHandler

#导入注册的蓝图
from api.testHello import testHello
from api.testGoodBye import testGoodBye

#日志配置参数
log_path = './logs/engine.log'
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(module)s - %(funcName)s - %(message)s')   #格式化
file_handler = RotatingFileHandler(log_path, maxBytes=10*1024*1024, backupCount=10)   #文件切割大小，按字节计算，10个文件后覆盖之前的
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.INFO)     #日志等级

#定义app
app = Flask(__name__)
app.config.from_object(config)

#注册蓝图到app
app.register_blueprint(testHello)
app.register_blueprint(testGoodBye)

#注册数据库连接
db = SQLAlchemy(app)

#为app程序添加 文件日志处理器 默认是stream out handler
app.logger.addHandler(file_handler)
app.logger.setLevel(logging.INFO)


def page_not_found(e):
    return jsonify(msg=str(e), code=404), 404


def bad_request(e):
    return jsonify(msg=str(e), code=400), 400


def method_not_allowed(e):
    return jsonify(msg=str(e), code=405), 405


def internal_server_error(e):
    return jsonify(msg=str(e), code=500), 500


#全局处理API错误
app.register_error_handler(404, page_not_found)
app.register_error_handler(400, bad_request)
app.register_error_handler(405, method_not_allowed)
app.register_error_handler(500, internal_server_error)


# class Country(db.Model)

#程序入口
if __name__ == '__main__':
    # print(db)
    app.run()
