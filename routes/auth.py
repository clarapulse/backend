from flask_restful import Resource
from flask import session
import requests
import os
class Auth(Resource):
    def get(self):
        if os.getenv('FLASK_ENV') == 'development':
            session['registered'] = True
            return {'success': 'You have successfully authenticated!'}            
        else:
            login =  requests.get('https://backend.allthenticate.net/externallogin?email=eddie@allthenticate.net&website=Allthentibank&prompted=true')
            if login.status_code == 200 and login.json()['firstName'] == 'Eddie':        
                session['registered'] = True            
                return {'success': 'You have successfully authenticated!'}
            else:
                return login.json()

class Logout(Resource):
    def get(self):
        session.clear()
        return {'success': 'Your session has been cleared.'}