from flask_restful import Resource
from flask import session, request
import requests
import os
from endpoints import require_login
from db import *


class Connections(Resource):
    # @require_login
    @CDB.connection_context()
    def get(self):
        user_id = session.get("user").get("uid")
        dbRes = Connection.select().where(Connection.user_id_one == user_id)
        if len(dbRes) == 0:
            return {"result": []}
        return {"result": [{"u1": x.user_id_one, "u2": x.user_id_two} for x in dbRes]}

    @require_login
    @CDB.connection_context()
    def post(self):
        user_id = session.get("user").get("uid")
        another_assholes_id = request.form.get("who")
        try:
            Connection.create(user_id_one=user_id, user_id_two=another_assholes_id)
        except IntegrityError as e:
            return {"success": False}
        return {"success": True}
