from bottle import Bottle

from .controllers.home import home_app


Routes = Bottle()
# provides welcome page.
Routes.merge(home_app)
