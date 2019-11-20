from api import testHello


@testHello.route('/')
def hello():
    return 'Hello World'
