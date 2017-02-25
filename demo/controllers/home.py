from bottle import Bottle, view


home_app = Bottle()


@home_app.route('/')
@view('index.html')
def index():
    return {}
