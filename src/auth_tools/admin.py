from django.contrib import admin, messages

from . import models


# Register your models here.
@admin.register(models.GoogleCredentials)
class GoogleCredentialsAdmin(admin.ModelAdmin):
    list_display = ("name", )


@admin.register(models.GoogleSheets)
class GoogleSheetsAdmin(admin.ModelAdmin):
    list_display = ("name", "sheet_id", "sheet_data_link", )
