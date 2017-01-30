import json
import gspread
from oauth2client.client import SignedJwtAssertionCredentials

def get_google_sheet():
    json_key = json.load(open('cabinet-access.json'))
    scope = ['https://spreadsheets.google.com/feeds']
    credentials = SignedJwtAssertionCredentials(json_key['client_email'], json_key['private_key'], scope)
    authorization = gspread.authorize(credentials)
    spreadsheet = authorization.open('Leahy Sanders Cabinet Votes')
    worksheet = spreadsheet.get_worksheet(0)

    return worksheet.get_all_records()
