import boto3
import json

from django.conf import settings
from django.contrib import admin, messages
from django.http import HttpResponseRedirect
from django.urls import path
from django.utils.html import format_html
from django.utils.safestring import mark_safe

from . import constants
from . import models
from . import views


# Register your models here.
class ToyModelAdminMixin(admin.ModelAdmin):
    fields = ("name", "description", "created_ts", "updated_ts", )
    list_display = ("name", "created_ts",)
    ordering = ("name", "created_ts", )
    readonly_fields = ["created_ts", "updated_ts", ]


class UrlToyModelAdminMixin(ToyModelAdminMixin):
    fields = ("name", "url", "description", "created_ts", "updated_ts", )
    list_display = ("name", "link_url", "created_ts",)

    def link_url(self, instance):
        return format_html('<a href="{}" target="_blank">{}</a>', instance.url, instance.url) if instance.url else ""


@admin.register(models.Manufacturer)
class ManufacturerAdmin(UrlToyModelAdminMixin):
    pass


@admin.register(models.License)
class LicenseAdmin(UrlToyModelAdminMixin):
    pass


@admin.register(models.Line)
class LineAdmin(ToyModelAdminMixin):
    fields = ("name", "manufacturer", "description", "created_ts", "updated_ts", )
    list_display = ("name", "manufacturer", "created_ts",)


@admin.register(models.Scale)
class ScaleAdmin(ToyModelAdminMixin):
    pass


@admin.register(models.Wave)
class WaveAdmin(ToyModelAdminMixin):
    fields = ("name", "line", "description", "created_ts", "updated_ts", )
    list_display = ("name", "line", "created_ts",)


@admin.register(models.Toy)
class ToyAdmin(ToyModelAdminMixin):
    fields = (
        "name", "manufacturer", "license", "line", "wave", "scale", "quantity", "description", "created_ts",
        "updated_ts", )
    list_display = ("name", "manufacturer", "license", "line", "scale", "quantity", "created_ts",)
    ordering = ("name", "created_ts",)
    readonly_fields = ["created_ts", "updated_ts", ]

    def get_urls(self):
        return [
           path('publish_json/', self.publish_json),
           path('sync_sheet/', self.sync_sheet),
        ] + super().get_urls()

    def publish_json(self, request):
        s3_client = boto3.client("s3")
        s3_client.put_object(
            ACL="public-read",
            Body=json.dumps(views.get_dashboard_data()).encode('utf-8'),
            Bucket=settings.BUCKET_NAME,
            ContentType="text/plain",
            Key=constants.TOYS_JSON_FILE)
        json_link_url = f"http://{settings.BUCKET_NAME}/{constants.TOYS_JSON_FILE}"
        admin_message  = f'JSON Published - <a href="{json_link_url}" target="_top">{json_link_url}</a>'
        self.message_user(request, mark_safe(admin_message))
        return HttpResponseRedirect("../")

    def sync_sheet(self, request):
        google_sheet_toy_list = views.get_sheet_data()
        sheets_toy_data = google_sheet_toy_list.get("toys")[1:]
        # This implies all toys are Super7. Needs a dropdown menu to select type.
        local_toys = models.Toy.objects.all()
        missing = []
        for toy in sheets_toy_data:
            toy_record = local_toys.filter(
                name=toy[0], line__name=toy[1], license__name=toy[2])
            if toy_record.count() == 0:
                missing.append(toy)
        if missing:
            toys_missing_from_local = ', '.join([f'{m[0]} ({m[1]})' for m in missing])
            message = f"Toys missing from local database: {toys_missing_from_local}"
            self.message_user(request, message, level=messages.ERROR)
        else:
            self.message_user(request, "All toys are synchronized.")
        return HttpResponseRedirect("../")
