import functools
from flask_restful import Resource
from flask import session, render_template, make_response

def registered(session):
    def decorator(f):
        @functools.wraps(f)
        def func(*args, **kwargs):
            if session.get('registered'):            
                val = f(*args, **kwargs)
                return make_response(val, 200, {'Content-Type': 'text/html'})
            else:
                return {}, 401        
        return func

    return decorator

class Dashboard(Resource):
    @registered(session)
    def get(self):
        return render_template('dashboard.html')

