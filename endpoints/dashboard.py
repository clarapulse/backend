import functools
from flask_restful import Resource
from flask import session, render_template, make_response
from endpoints import require_login

class Dashboard(Resource):
    
    @require_login
    def get(self):
        return render_template('dashboard.html')

