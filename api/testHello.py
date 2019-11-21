from api import testHello
from flask import current_app   #日志使用 (flask使用的是python标准的logger)


@testHello.route('/')
def hello():
    current_app.logger.info('hello world logging test info!')
    current_app.logger.warning('warning logger!')
    current_app.logger.error('error logger!')
    # current_app.logger.exception('exception logger!')
    # current_app.logger.critical('critical logger!')
    # current_app.logger.debug('debug logger!')
    return 'Hello World'
