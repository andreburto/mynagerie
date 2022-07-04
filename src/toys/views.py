import json

from django.db.models import Count, F
from django.http import HttpResponse, JsonResponse
from django.template.loader import render_to_string
from django.urls import reverse

from google.oauth2 import service_account
from googleapiclient.discovery import build

from . import constants, models


# Create your views here.
def dashboard(request):
    return HttpResponse(render_to_string(
        "toys/dashboard.html",
        {
            "data_url": reverse("dashboard_data"),
        }))


def get_dashboard_data():
    all_toys_qs = models.Toy.objects.filter(manufacturer__name=constants.MANUFACTURER_SUPER7)
    # Columns are ordered by default at the model level.
    all_toys_list = (all_toys_qs.values("name", "line__name", "license__name")
                     .annotate(line=F("line__name"), license=F("license__name"))
                     .values("name", "line", "license"))
    toys_by_line = (all_toys_qs.values("line")
                    .annotate(count=Count("id"), name=F("line__name"))
                    .values("name", "count"))
    toys_by_license = (all_toys_qs.values("license")
                       .annotate(count=Count("id"), name=F("license__name"))
                       .values("name", "count"))
    license_and_line = (all_toys_qs.values("line__name", "license__name")
                        .annotate(count=Count("id"), line=F("line__name"), license=F("license__name"))
                        .values("line", "license", "count")
                        .order_by("license", "line"))
    return {
        "toys": list(all_toys_list),
        "count_by_line": list(toys_by_line),
        "count_by_license": list(toys_by_license),
        "license_and_line": list(license_and_line),
    }


def dashboard_data(request):
    return JsonResponse(get_dashboard_data())


def sheet(request):
    return HttpResponse("Toys List via Google Sheets")


def get_sheet_data(id=None):
    if id:
        google_sheet = models.GoogleSheets.objects.get(id=id)
    else:
        google_sheet = models.GoogleSheets.objects.all().order_by("id").first()

    service_credentials = json.loads(str(google_sheet.credentials.credentials).strip())

    creds = service_account.Credentials.from_service_account_info(
        service_credentials, scopes=constants.GOOGLE_SHEETS_SCOPE_RO)
    service = build('sheets', 'v4', credentials=creds)

    # Call the Sheets API
    sheet = service.spreadsheets()
    result = sheet.values().get(
        spreadsheetId=google_sheet.sheet_id, range=google_sheet.sheet_range).execute()
    return {"toys": result.get('values', []), }


def sheet_data(request, id=None):
    return JsonResponse(get_sheet_data(id))
