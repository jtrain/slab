from bottle import Bottle

from .controllers.base import base_app


Routes = Bottle()
# provides the API for connectivity checks.
Routes.merge(base_app)
