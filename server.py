from flask import Flask
from flask_cors import CORS

app = Flask(__name__)

app.register_blueprint(process_lecture)
app.register_blueprint(courses_api)
app.register_blueprint(lectures_api)

CORS(app)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == '__main__':
	app.run(debug=True)
