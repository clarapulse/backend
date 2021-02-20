from flask_restful import Resource
from flask import session, request, jsonify
import requests
import os
from db import *
from endpoints import require_login


class Auth(Resource):
    def get(self):
        if os.getenv('FLASK_ENV') == 'development':
            session['registered'] = True
            session['user_id'] = 1
            return {'success': 'You have successfully authenticated!'}            
        else:
            login =  requests.get('https://backend.allthenticate.net/externallogin?email=eddie@allthenticate.net&website=Allthentibank&prompted=true')
            if login.status_code == 200 and login.json()['firstName'] == 'Eddie':        
                session['registered'] = True            
                return {'success': 'You have successfully authenticated!'}
            else:
                return login.json()

    @require_login
    @CDB.connection_context()
    def put(self):
        user_id = "1"
        name = request.form.get("name")
        email = request.form.get("email")
        url = request.form.get("url")
        try:
            User.create(
                user_id=user_id,
                name=name,
                email=email,
                url=url
            )
        except IntegrityError as e:
            return jsonify({"success": False})
        return jsonify({"success": True})


class Logout(Resource):
    def get(self):
        session.clear()
        return {'success': 'Your session has been cleared.'}