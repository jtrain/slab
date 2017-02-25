import os

from bottle import Bottle, static_file, TEMPLATE_PATH

from .controllers.home import home_app


PROJECT_PATH = os.path.join(os.path.abspath(os.path.dirname(__file__)))
TEMPLATE_PATH.insert(0, os.path.join(PROJECT_PATH, 'views'))
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')


Routes = Bottle()
# provides welcome page.
Routes.merge(home_app)

@Routes.route('/static/<filename:path>')
def send_static(filename):
    return static_file(filename, root=STATIC_ROOT)
