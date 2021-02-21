from flask_restful import Resource
from flask import session, request, jsonify
import requests
import os
from db import *
from endpoints import require_login


class Lol(Resource):
    def get(self):
        return {"lol": 5}


class AddUser(Resource):
    @require_login
    @CDB.connection_context()
    def post(self):
        user = session.get("user")
        try:
            User.create(
                user_id=user.get("uid"),
                name=user.get("name"),
                email=user["firebase"]["identities"]["email"][0],
                url=user.get("picture"),
                is_highschool=True,
                highschool="lmao",
            )
        except IntegrityError as e:
            print(e)
            return {"success": False}, 500

        return {"success": True}


class University(Resource):
    @require_login
    @CDB.connection_context()
    def post(self):
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