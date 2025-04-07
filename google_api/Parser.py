from db.models import Material, Movie, SpreadSheet
from google_api.GoogleSpreadSheet import GoogleSpreadSheet


class Parser:
    @staticmethod
    def parse():
        keys = ['name', 'status', 'url', 'plan']

        for sheet in SpreadSheet.select():
            google_sheet = GoogleSpreadSheet.create_from_spreadsheet(sheet)
            value_ranges = google_sheet.get_values([sheet_range.name for sheet_range in sheet.ranges])['valueRanges']

            for value_range in value_ranges:
                values: list[list[str | None]] = value_range['values']
                movie_name = values[2][1]
                movie, created = Movie.get_or_create(name=movie_name)
                if created:
                    movie.save()

                for value in values[4:]:
                    if len(value) == 2:
                        continue
                    data = dict(zip(keys, value[1:]))
                    material, created = Material.get_or_create(movie=movie, name=data['name'])
                    material.update(**data)
                    material.save()


if __name__ == '__main__':
    Parser.parse()
