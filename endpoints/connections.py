from flask_restful import Resource
from flask import session, request
import requests
import os
from endpoints import require_login
from playhouse.shortcuts import model_to_dict
from db import *


class Connections(Resource):
    @require_login
    @CDB.connection_context()
    def get(self):
        user_id = session.get("user").get("uid")
        dbRes = Connection.select().where(
            Connection.user_id_one == user_id or Connection.user_id_two == user_id
        )
        if len(dbRes) == 0:
            return []

        other_people = [x.user_id_two for x in dbRes]

        res = []
        for other_person in other_people:
            other = User.select().where(User.user_id == other_person).get()
            res.append(model_to_dict(other))
        print(res)
        return res

    @require_login
    @CDB.connection_context()
    def post(self):
        user_id = session.get("user").get("uid")

        another_assholes_id = request.form.get("who")
        try:
            Connection.create(user_id_one=user_id, user_id_two=another_assholes_id)
        except IntegrityError as e:
            print(e)
            return {"success": False}, 500
        return {"success": True}


class PotentialConnections(Resource):
    @require_login
    @CDB.connection_context()
    def get(self):
        # get a <REQUESTED_AMD> random other people. guranteed not to include the requested user

        user_id = session.get("user").get("uid")

        REQUESTED_AMT = 4

        people = [
            model_to_dict(p)
            for p in User.select().order_by(fn.Random()).limit(REQUESTED_AMT + 1)
        ]

        people = filter(lambda p: p.get("user_id") != user_id, people)
        return people[:4]