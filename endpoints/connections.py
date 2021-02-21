from flask_restful import Resource
from flask import session, request
import requests
import os
from endpoints import require_login
from db import *


class Connections(Resource):
    @require_login
    @CDB.connection_context()
    def get(self):
        user_id = session.get("user").get("uid")
        dbRes = Connection.select().where(Connection.user_id_one == user_id)
        if len(dbRes) == 0:
            return {"result": []}

        other_people = [x.user_id_two for x in dbRes]
        for ppl in other_people:
            print(ppl)

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
