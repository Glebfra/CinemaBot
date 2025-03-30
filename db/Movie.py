from peewee import CharField, ForeignKeyField

from db.BaseModel import BaseModel, db
from db.SpreadSheet import SpreadSheetRange


class Movie(BaseModel):
    name: str = CharField()
    spreadsheet_range: SpreadSheetRange = ForeignKeyField(SpreadSheetRange, backref='movies')


class Material(BaseModel):
    movie = ForeignKeyField(Movie, backref='materials')
    name = CharField(null=True)
    status = CharField(null=True)
    url = CharField(null=True)
    plan = CharField(null=True)


if __name__ == '__main__':
    db.connect()
    db.create_tables([Movie, Material], safe=True)
