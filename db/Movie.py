from peewee import CharField, ForeignKeyField

from db.BaseModel import BaseModel, db


class Movie(BaseModel):
    name = CharField()


class Material(BaseModel):
    movie = ForeignKeyField(Movie, backref='materials')
    name = CharField(null=True)
    status = CharField(null=True)
    url = CharField(null=True)
    plan = CharField(null=True)


if __name__ == '__main__':
    db.connect()
    db.create_tables([Movie, Material], safe=True)
