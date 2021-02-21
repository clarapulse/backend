from playhouse.cockroachdb import CockroachDatabase
from peewee import *

CDB = CockroachDatabase("clara", user="root", host="35.222.46.226")
# CDB = SqliteDatabase("b.db")


class BaseModel(Model):
    class Meta:
        database = CDB


class User(BaseModel):
    user_id = CharField(primary_key=True)
    name = CharField()
    email = CharField()
    url = TextField()
    is_highschool = BooleanField(null=True)
    major = CharField(null=True)
    highschool = CharField(null=True)
    university = CharField(null=True)


class Connection(BaseModel):
    user_id_one = CharField()
    user_id_two = CharField()

    class Meta:
        primary_key = CompositeKey("user_id_one", "user_id_two")


class Intention(BaseModel):
    intention_id = IntegerField(primary_key=True)
    user_id = CharField()
    univ_name = CharField()


@CDB.connection_context()
def initialize():
    CDB.create_tables([User, Connection, Intention])


initialize()
