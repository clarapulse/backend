from flask_restful import Resource
from flask import session, jsonify, request
import requests
import os
from endpoints import require_login
from db import *


class Connections(Resource):
    @require_login
    @CDB.connection_context()
    def get(self):
        user_id = session.get("user_id")
        dbRes = User.get(User.user_id == user_id)
        if len(dbRes) == 0:
            return jsonify({"result": []})
        return jsonify({"result": [x for x in dbRes]})

    @require_login
    @CDB.connection_context()
    def post(self):
        user_id = session.get("user_id")
        another_assholes_id = request.form.get("who")
        try:
            Connection.create(
                user_id_one=user_id,
                user_id_two=another_assholes_id
            )
        except IntegrityError as e:
            return jsonify({"success": False})
        return jsonify({"success": True})
