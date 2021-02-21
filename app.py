import time
import endpoints
import os
import importlib, inspect


# flask
from flask import Flask, session, request, g
from flask_restful import Api, Resource
from flask_session import Session
from datetime import timedelta
from flask_cors import CORS
import argparse


app = Flask(__name__)
CORS(app)


parser = argparse.ArgumentParser(description="Process some integers.")
parser.add_argument(
    "--debug", default=False, action="store_true", help="Skip authentication"
)
args, unknown = parser.parse_known_args()
endpoints.CONFIG["debug"] = args.debug


app.config.update(
    {
        "SECRET_KEY": os.getenv("FLASK_SECRET_KEY"),
        "SESSION_TYPE": "filesystem",
        "SESSION_COOKIE_SECURE": not args.debug,
        "SESSION_USE_SIGNER": True,
        "PERMANENT_SESSION_LIFETIME": timedelta(weeks=52),
    }
)

Session(app)

api = Api(app)


(_, _, filenames) = next(os.walk("endpoints"))

for file in filenames:
    if file.endswith(".py") and file != "__init__.py":
        moduleName = os.path.splitext(file)[0].lower()
        module = importlib.import_module(f"endpoints.{moduleName}")
        for name, obj in inspect.getmembers(module):
            if (
                inspect.isclass(obj)
                and issubclass(obj, Resource)
                and name != "Resource"
            ):
                api.add_resource(obj, f"/{name.lower()}")


@app.before_request
def setup_request():
    g.start = time.time()  # get start time of request
    session.modified = (
        True  # in case session modification was a mutable item (list or dict)
    )


@app.after_request
def log_request(response):
    duration = round(time.time() - g.start, 2)  # get time taken for request
    if session.get("loggedin"):
        user_info = session.get("user")
        user = f"From {user_info.get('email')}:\n"
    else:
        user = "From unauthenticated user:\n"
    request_args = f"\n Params: {dict(request.args)}"
    log_params = [
        ("user_info", user, "purple"),
        ("method", request.method, "blue"),
        ("path", request.path, "blue"),
        ("status", response.status, "green"),
        ("duration", duration, "yellow"),
        ("params", request_args, "black"),
    ]
    parts = ["Processed Request:\n"]
    for name, value, color in log_params:
        parts.append(str(value))
    print(" ".join(parts))
    return response


port = int(os.environ.get("PORT", 8000))
if __name__ == "__main__":
    app.run(host="0.0.0.0", threaded=True, port=port, use_reloader=False)
