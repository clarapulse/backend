"""
Protect routes with firebase.
"""


from firebase_admin import credentials, auth, initialize_app
import json
from flask import request
import functools
from flask import session

CONFIG = {"debug": False}
FCM_TOKENS = [
    "fCSgnX5QQAmigtLe6c9gLo:APA91bFEdoWtgfBKMJB27VS3qjVbaCOUUxRajLDxRZonwEK2j0XuBK3nM1AR73CMhP8ESvn3F6p9p2-cgZd2OS7HZoVZjUzNsgw5g5hOwuC5TxZvRv-_QxqZYDbXLvVdssXj_vWOxpOn"
]
# Connect to firebase
cred = credentials.Certificate("firebase_creds.json")
firebase = initialize_app(cred)
FCM_KEY = "AAAA39F-IVM:APA91bFlK2JFoLOf9slR8VfMymf3ylRzaJAargobw6gWDpUMeSNoVraNfD1b1DfvUNCFnhhdqL4b79uVMt6UGCvvfPt0uKvo6psewpxW1S9diom1X9DXVz2OmJujEYJW400DWTMwxhB0"


def require_login(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if CONFIG.get("debug") or session.get("loggedin"):
            # maybe set session user here for the future?
            return func(*args, **kwargs)

        if not request.headers.get("Authorization"):
            return {"message": "No token provided"}, 400
        try:
            user = auth.verify_id_token(request.headers.get("Authorization"))
            session["loggedin"] = True
            session["user"] = user

        except auth.InvalidIdTokenError:
            print("Invalid id token")
            return {"message": "Invalid token provided."}, 400
        except auth.ExpiredIdTokenError:
            print("Expired")
            return {"message": "Invalid token provided."}, 400
        except auth.RevokedIdTokenError:
            print("Revoked")
            return {"message": "Invalid token provided."}, 400
        except auth.CertificateFetchError:
            print("Fetch error")
            return {"message": "Invalid token provided."}, 400
        return func(*args, **kwargs)

    return wrapper
