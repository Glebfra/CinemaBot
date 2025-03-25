from peewee import CharField

from db.BaseModel import BaseModel, db


class Movie(BaseModel):
    name = CharField()


if __name__ == '__main__':
    db.connect()
    db.create_tables([Movie], safe=True)
