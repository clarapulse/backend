from flask_restful import Resource
from flask import session, request, jsonify
import requests
import os
from db import *
from endpoints import require_login


class Lol(Resource):
    def get(self):
        return {"lol": 5}


class Auth(Resource):
    @require_login
    @CDB.connection_context()
    def put(self):
        user_id = session.get("user").get("uid")
        name = request.form.get("name")
        email = request.form.get("email")
        url = request.form.get("url")
        try:
            User.create(user_id=user_id, name=name, email=email, url=url)
        except IntegrityError as e:
            return {"success": False}
        return {"success": True}


class University(Resource):
    @require_login
    @CDB.connection_context()
    def put(self):
        # set whether they are highschool student or univ student
        user_id = session.get("user").get("uid")
        university_name = request.form.get(
            "university_name"
        )  # null if they are hs student
        hs_name = request.form.get("highschool_name")  # null if they are univ student
        intended_university_name = request.form.get(
            "intended_university_name"
        )  # seperated by comma
        if not intended_university_name:
            return {"success": False}
        for i in intended_university_name.split(","):
            Intention.create(user_id=user_id, intended_university_name=i)
        User.update(
            is_highschool=university_name is None,
            highschool=hs_name,
            university=university_name,
        ).where(User.user_id == user_id).execute()
        return {"success": True}


class Logout(Resource):
    @require_login
    def get(self):
        session.clear()
        return {"success": "Your session has been cleared."}
