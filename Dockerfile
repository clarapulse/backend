FROM python:3.8.2-alpine3.11
RUN apk add build-base
RUN apk add libffi-dev
RUN apk add python3-dev

WORKDIR /home/src
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 80


# do this properly later
ENV FLASK_SECRET_KEY 'a716fd99-2db6-4b58-bd2b-388217f20dac' 
COPY . .
CMD ["gunicorn", "app:app", "--workers", "20", "--timeout", "120", "-b", "0.0.0.0:80"]
