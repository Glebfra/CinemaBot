import os.path

from peewee import CharField, ForeignKeyField, Model, SqliteDatabase

path = os.path.dirname(os.path.realpath(__file__))
db = SqliteDatabase(f'{path}/../.data/sqlite.db')


class BaseModel(Model):
    class Meta:
        database = db


class SpreadSheet(BaseModel):
    spreadsheet_id: str = CharField()
    url: str = CharField()


class SpreadSheetRange(BaseModel):
    spreadsheet_id = ForeignKeyField(SpreadSheet, backref='ranges')
    name: str = CharField(null=True)


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
    db.create_tables([SpreadSheet, SpreadSheetRange, Movie, Material], safe=True)
