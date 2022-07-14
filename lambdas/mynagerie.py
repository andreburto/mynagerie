import boto3
import json
import os

from google.oauth2 import service_account
from googleapiclient.discovery import build


GOOGLE_SHEETS_SCOPE_RO = ["https://www.googleapis.com/auth/spreadsheets.readonly"]


def get_service_credentials():
    return {
        "type": "service_account",
        "project_id": "thrird-party",
        "private_key_id": os.getenv("PRIVATE_KEY_ID"),
        "private_key": os.getenv("PRIVATE_KEY"),
        "client_email": os.getenv("CLIENT_EMAIL"),
        "client_id": os.getenv("CLIENT_ID"),
        "auth_uri": "https://accounts.google.com/o/oauth2/auth",
        "token_uri": "https://oauth2.googleapis.com/token",
        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
        "client_x509_cert_url": (
            "https://www.googleapis.com/robot/v1/metadata/"
            "x509/mynagerie%40thrird-party.iam.gserviceaccount.com")
    }


def get_sheet_data():
    sheet_id = os.getenv("SHEET_ID")
    sheet_range = os.getenv("SHEET_RANGE")
    service_credentials = get_service_credentials()

    creds = service_account.Credentials.from_service_account_info(
        service_credentials, scopes=GOOGLE_SHEETS_SCOPE_RO)
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=sheet_id, range=sheet_range).execute()
    return {"toys": result.get('values', []), }


def mynagerie_handler():
    pass
