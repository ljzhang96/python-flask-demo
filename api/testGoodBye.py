from api import testGoodBye


@testGoodBye.route('/')
def show():
    return 'Good Bye!!'


@testGoodBye.route('/no')
def save():
    return 'No!!'
