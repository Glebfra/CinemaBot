import os.path

from peewee import CharField, Model, SqliteDatabase

path = os.path.dirname(os.path.realpath(__file__))
db = SqliteDatabase(f'{path}/sqlite.db')


class BaseModel(Model):
    class Meta:
        database = db
