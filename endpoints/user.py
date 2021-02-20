import functools
from flask_restful import Resource
from flask import session, render_template, make_response
from endpoints import require_login

class GetUserInfo(Resource):

    @require_login
    def get(self):
        session['user']['user_id']
        return user_id
