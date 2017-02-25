# -*- coding: utf-8 -*-
from bottle import Bottle


base_app = Bottle()


@base_app.route('/active')
def active():
    return {'active': True}


