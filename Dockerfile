FROM python:3.8.2-alpine3.11
RUN apk add build-base
RUN apk add libffi-dev
RUN apk add python3-dev

WORKDIR /home/src
COPY . .
RUN pip install -r requirements.txt
CMD ["gunicorn", "app:app", "--workers", "20", "--timeout", "2", "-b", "0.0.0.0:80"]
