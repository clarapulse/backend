from playhouse.cockroachdb import CockroachDatabase
from peewee import *

CDB = CockroachDatabase('my_app', user='root', host='10.1.0.8')


class BaseModel(Model):
    class Meta:
        database = CDB


class User(BaseModel):
    user_id = CharField(primary_key=True)


class Connection(BaseModel):
    connection_id = IntegerField(primary_key=True)
    user_id_one = CharField()
    user_id_two = CharField()

