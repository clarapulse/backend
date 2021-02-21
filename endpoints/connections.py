from flask_restful import Resource
from flask import session, request
import requests
import os
from endpoints import FCM_TOKENS, require_login
from playhouse.shortcuts import model_to_dict
from db import *
from pyfcm import FCMNotification
from endpoints import FCM_KEY, FCM_TOKENS


@CDB.connection_context()
def get_connections(user_id):
    dbRes = Connection.select().where(
        Connection.user_id_one == user_id or Connection.user_id_two == user_id
    )
    if len(dbRes) == 0:
        return []

    return [x.user_id_two for x in dbRes]


def send_fcm(data_message, title=None):
    push_service = FCMNotification(api_key=FCM_KEY)
    try:
        if type(FCM_TOKENS) is list:
            print(FCM_TOKENS, data_message)
            result = push_service.notify_multiple_devices(
                registration_ids=FCM_TOKENS, message_body=data_message
            )
            print(result, "++++++++++++++", flush=True)
        else:
            print(FCM_TOKENS, "single device", data_message)
            result = push_service.notify_single_device(
                registration_id=FCM_TOKENS, message_body=data_message
            )
            print(result, flush=True)
    except Exception as e:
        print(e, flush=True)


class Connections(Resource):
    @require_login
    @CDB.connection_context()
    def get(self):
        user_id = session.get("user").get("uid")
        other_people = get_connections(user_id)
        res = []
        for other_person in other_people:
            other = User.select().where(User.user_id == other_person).get()
            res.append(model_to_dict(other))
        return res

    @require_login
    @CDB.connection_context()
    def post(self):
        user_id = session.get("user").get("uid")

        other = request.form.get("who")
        try:
            Connection.create(user_id_one=user_id, user_id_two=other)
        except IntegrityError as e:
            print(e)
            return {"success": False}, 500

        send_fcm("connect request")
        return {"success": True}


class PotentialConnections(Resource):
    @require_login
    @CDB.connection_context()
    def get(self):
        # get a <REQUESTED_AMD> random other people. guranteed not to include the requested user

        user_id = session.get("user").get("uid")

        REQUESTED_AMT = 4
        ignored = get_connections(user_id) + [user_id]
        res = []

        scott = {
            "user_id": "gStfLeZMqYaBArkkVXoCdwlVYJQ2",
            "url": "https://images-ext-2.discordapp.net/external/PaHiVmDDYd6rvA0mNkMksQTYe5vxm3spid5U6o4A31A/https/lh6.googleusercontent.com/-bbMB4noEp8g/AAAAAAAAAAI/AAAAAAAAAAA/AMZuuckoz6PP1B1RZiz5WRlf3Dnd2OE-PQ/s96-c/photo.jpg",
            "name": "Scott Chow",
            "is_highschool": False,
            "university": "Harvard University",
        }  # scott comes second
        people = [model_to_dict(p) for p in User.select().order_by(fn.Random())]
        people.insert(1, scott)

        for person in people:
            if person["user_id"] not in ignored:
                res.append(person)
            if len(res) == REQUESTED_AMT:
                return res
        return res
