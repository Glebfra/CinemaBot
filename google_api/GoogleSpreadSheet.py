import apiclient
import httplib2
from oauth2client.service_account import ServiceAccountCredentials

from db.models import SpreadSheet

CREDENTIALS_FILE = 'credentials_service.json'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']


class GoogleSpreadSheet:
    def __init__(self, service, ID):
        self.service = service
        self.ID = ID

    @classmethod
    def create_from_spreadsheet(cls, spreadsheet: SpreadSheet):
        return cls.create_from_id(spreadsheet.spreadsheet_id)

    @classmethod
    def create_from_id(cls, ID):
        credentials: ServiceAccountCredentials = ServiceAccountCredentials.from_json_keyfile_name(
            CREDENTIALS_FILE, SCOPES
            )
        http_auth: httplib2.Http = credentials.authorize(httplib2.Http())
        service = apiclient.discovery.build('sheets', 'v4', http=http_auth)
        return cls(service, ID)

    def get_values(self, ranges) -> dict:
        return self.service.spreadsheets().values().batchGet(spreadsheetId=self.ID, ranges=ranges).execute()


if __name__ == '__main__':
    sheets = SpreadSheet.select()
    for sheet in sheets:
        google_sheet = GoogleSpreadSheet.create_from_spreadsheet(sheet)
        values = google_sheet.get_values([sheet_range.name for sheet_range in sheet.ranges])
        print(values)
        print(values['valueRanges'])
