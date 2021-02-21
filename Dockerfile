FROM python:3.8.2-alpine3.11
RUN apk add build-base
RUN apk add libffi-dev
RUN apk add python3-dev

# Allow statements and log messages to immediately appear in the Knative logs
ENV PYTHONUNBUFFERED True

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME

# do this properly later
ENV FLASK_SECRET_KEY 'a716fd99-2db6-4b58-bd2b-388217f20dac' 
ENV FLASK_DEBUG 'development'

COPY requirements.txt ./requirements.txt

# Install production dependencies.
RUN pip install -r requirements.txt

COPY . ./
# Run the web service on container startup. Here we use the gunicorn
# webserver, with one worker process and 8 threads.
# For environments with multiple CPU cores, increase the number of workers
# to be equal to the cores available.
# Timeout is set to 0 to disable the timeouts of the workers to allow Cloud Run to handle instance scaling.
CMD exec gunicorn --bind 0.0.0.0:$PORT --workers 1 --threads 8 --timeout 0 app:app
