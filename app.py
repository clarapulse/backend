
import os
import importlib, sys, inspect
# flask
from flask import Flask
from flask_socketio import SocketIO
from flask_restful import Api, Resource
from flask_session import Session
from datetime import timedelta

app = Flask(__name__)

app.config.update({
    'SECRET_KEY': os.getenv('FLASK_SECRET_KEY'),
    'SESSION_TYPE': 'filesystem',
    'SESSION_COOKIE_SECURE': os.getenv('FLASK_ENV') != 'development',
    'SESSION_USE_SIGNER': True,
    'PERMANENT_SESSION_LIFETIME': timedelta(weeks=52)
})

Session(app)

api = Api(app)

socketio = SocketIO(app, manage_session=False)


(_, _, filenames)  = next(os.walk('routes'))

for file in filenames:
    if file.endswith('.py') and file != '__init__.py':
        moduleName = os.path.splitext(file)[0].lower()
        module = importlib.import_module(f'routes.{moduleName}')
        for name, obj in inspect.getmembers(module):
            if inspect.isclass(obj) and issubclass(obj, Resource) and name != 'Resource':            
                api.add_resource(obj, f'/{name.lower()}')



if __name__ == '__main__':
    socketio.run(app)