#导入蓝图模块
from flask import Blueprint

#注册一个蓝图
testHello = Blueprint('test', __name__, url_prefix='/test')

testGoodBye = Blueprint('bye', __name__, url_prefix='/bye')
