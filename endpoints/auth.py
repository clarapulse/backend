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
            login = requests.get(
                'https://backend.allthenticate.net/externallogin?email=eddie@allthenticate.net&website=Allthentibank&prompted=true')
            if login.status_code == 200 and login.json()['firstName'] == 'Eddie':
                session['registered'] = True
                return {'success': 'You have successfully authenticated!'}
            else:
                return login.json()

    @require_login
    @CDB.connection_context()
    def put(self):
        user_id = session.get("user_id")
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


class University(Resource):
    @require_login
    @CDB.connection_context()
    def put(self):
        # set whether they are highschool student or univ student
        user_id = session.get("user_id")
        university_name = request.form.get("university_name")  # null if they are hs student
        hs_name = request.form.get("highschool_name")  # null if they are univ student
        intended_university_name = request.form.get("intended_university_name")  # seperated by comma
        if not intended_university_name:
            return jsonify({"success": False})
        for i in intended_university_name.split(","):
            Intention.create(
                user_id=user_id,
                intended_university_name=i
            )
        User.update(
            is_highschool=university_name is None,
            highschool=hs_name,
            university=university_name
        ).where(User.user_id == user_id).execute()
        return jsonify({"success": True})


class Logout(Resource):
    def get(self):
        session.clear()
        return {'success': 'Your session has been cleared.'}
