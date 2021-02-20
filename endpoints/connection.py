from flask_restful import Resource
from flask import session, jsonify
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
        return jsonify({"result": dbRes})

    @require_login
    def post(self):
        pass
