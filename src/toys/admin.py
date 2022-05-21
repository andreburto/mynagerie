from django.contrib import admin
from django.utils.html import format_html

from . import models


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


@admin.register(models.Toy)
class ToyAdmin(ToyModelAdminMixin):
    fields = (
        "name", "manufacturer", "license", "line", "scale", "quantity", "description", "created_ts", "updated_ts", )
    list_display = ("name", "manufacturer", "license", "line", "scale", "quantity", "created_ts",)
    ordering = ("name", "created_ts",)
    readonly_fields = ["created_ts", "updated_ts", ]
