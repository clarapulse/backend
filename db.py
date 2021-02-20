from playhouse.cockroachdb import CockroachDatabase
from peewee import *

# CDB = CockroachDatabase('my_app', user='root', host='10.1.0.8')
CDB = SqliteDatabase("b.db")


class BaseModel(Model):
    class Meta:
        database = CDB


class User(BaseModel):
    user_id = CharField(primary_key=True)
    name = CharField()
    email = CharField()
    url = TextField()
    is_highschool = BooleanField()
    highschool = CharField(null=True)
    university = CharField(null=True)


class Connection(BaseModel):
    connection_id = IntegerField(primary_key=True)
    user_id_one = CharField()
    user_id_two = CharField()

    class Meta:
        indexes = (
            (('user_id_one', 'user_id_two'), True),
        )


class Intention(BaseModel):
    intention_id = IntegerField(primary_key=True)
    user_id = CharField()
    univ_name = CharField()


@CDB.connection_context()
def initialize():
    CDB.create_tables([User, Connection])


initialize()
