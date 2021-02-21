#!/bin/bash

source venv/bin/activate
export FLASK_SECRET_KEY='testing'
export FLASK_ENV='development' 
python app.py