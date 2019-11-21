from api import testHello
from flask import current_app, request, jsonify   #日志使用 (flask使用的是python标准的logger)


@testHello.route('/')
def hello():
    current_app.logger.info('hello world logging test info!')
    current_app.logger.warning('warning logger!')
    current_app.logger.error('error logger!')
    # current_app.logger.exception('exception logger!')
    # current_app.logger.critical('critical logger!')
    # current_app.logger.debug('debug logger!')
    return 'Hello World'


@testHello.route('/param', methods=['POST'])
def test_post():
    current_app.logger.info('this is a post request')
    name = request.values.get('python')
    print(name)
    return 'Hello World Post'


@testHello.route('/endpoint', methods=['GET'])
def test_get():
    name = request.values.get('haha')
    msg = 'this is a get request by params with {}'.format(name)
    print(name)
    current_app.logger.info(msg)
    return 'Hello World Get'


#uri
@testHello.route('/uri/<int:number>', methods=['GET'])
def test_get_1(number):
    if isinstance(number, int):
        print(str(number)+' is a number')
    else:
        print('is not a number')
    return jsonify(code=200, msg='uri request', data=number)
