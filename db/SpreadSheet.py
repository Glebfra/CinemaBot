from peewee import CharField, ForeignKeyField

from db.BaseModel import BaseModel, db


class SpreadSheet(BaseModel):
    spreadsheet_id: str = CharField()
    url: str = CharField()


class SpreadSheetRange(BaseModel):
    spreadsheet_id = ForeignKeyField(SpreadSheet, backref='ranges')
    name: str = CharField(null=True)


if __name__ == '__main__':
    db.connect()
    db.create_tables([SpreadSheet, SpreadSheetRange], safe=True)
