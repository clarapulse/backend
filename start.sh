#!/bin/bash

source venv/bin/activate
export FLASK_SECRET_KEY='testing'
export FLASK_ENV='development' 
nodemon -x "python app.py" -e py,html