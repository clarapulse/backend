FROM python:3.8.2-alpine3.11

WORKDIR /home/src
RUN pip install flask peewee gunicorn
COPY . .
CMD ["gunicorn", "app:app", "--workers", "20", "--timeout", "2", "-b", "0.0.0.0:80"]
