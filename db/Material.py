from peewee import CharField, ForeignKeyField

from db.BaseModel import BaseModel, db
from db.Movie import Movie


class Material(BaseModel):
    movie = ForeignKeyField(Movie, backref='materials')
    name = CharField()
    status = CharField()
    url = CharField()
    plan = CharField()


if __name__ == '__main__':
    db.connect()
    db.create_tables([Material], safe=True)
