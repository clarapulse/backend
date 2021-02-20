"""
Protect routes with firebase.
"""



from firebase_admin import credentials, auth, initialize_app
import json
from flask import request
import functools
from flask import session

#Connect to firebase
cred = credentials.Certificate('firebase_creds.json')
firebase = initialize_app(cred)


def require_login(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        if session['registered']:
            return func(*args, **kwargs)
        else:
            if not request.headers.get('Authorization'):
                return {'message': 'No token provided'},400
            try:
                user = auth.verify_id_token(request.headers.get('Authorization'))
                session['registered'] = True
                session['user'] = user
            except auth.InvalidIdTokenError:
                print("Invalid id token")
                return {'message':'Invalid token provided.'},400
            except auth.ExpiredIdTokenError:
                print("Expired")
                return {'message':'Invalid token provided.'},400
            except auth.RevokedIdTokenError:
                print("Revoked")
                return {'message':'Invalid token provided.'},400
            except auth.CertificateFetchError:
                print("Fetch error")
                return {'message':'Invalid token provided.'},400
            return func(*args, **kwargs)
    return wrapper
