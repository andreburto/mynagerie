from datetime import datetime, timezone

from django.contrib import admin
from django.db import models
from django.utils.html import format_html


# Create your models here.
class ToyModelMixin(models.Model):
    name = models.CharField(max_length=256, blank=False, help_text="Descriptive title of the record.", unique=False)
    description = models.TextField(max_length=1024, blank=True, null=True, help_text="Notes about the object.")
    created_ts = models.DateTimeField(blank=True, null=True)
    updated_ts = models.DateTimeField(blank=True, null=True)

    class Meta:
        abstract = True

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.name}"

    def __str__(self):
        return f"{self.name}"

    def save(self, *args, **kwargs):
        if not self.created_ts:
            self.created_ts = datetime.now(timezone.utc)
        self.updated_ts = datetime.now(timezone.utc)
        super().save(*args, **kwargs)


class GoogleModelMixin(models.Model):
    name = models.CharField(max_length=30, blank=False)

    class Meta:
        abstract = True

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.name}"

    def __str__(self):
        return f"{self.name}"


class UrlToyModelMixin(ToyModelMixin):
    url = models.URLField(blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=["name", ]),
            models.Index(fields=["url", ]),
        ]
        ordering = ["name", "created_ts", ]


class Manufacturer(UrlToyModelMixin):
    pass


class License(UrlToyModelMixin):
    pass


class Line(ToyModelMixin):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING, default="", blank=True, null=True)


class Scale(ToyModelMixin):
    pass


class Wave(ToyModelMixin):
    line = models.ForeignKey(Line, on_delete=models.DO_NOTHING, default="", blank=True, null=True)

    class Meta:
        indexes = [
            models.Index(fields=["name", ]),
            models.Index(fields=["line", ]),
        ]
        ordering = ["name", "line", "created_ts", ]


class Toy(ToyModelMixin):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.DO_NOTHING)
    license = models.ForeignKey(License, on_delete=models.DO_NOTHING)
    line = models.ForeignKey(Line, on_delete=models.DO_NOTHING)
    wave = models.ForeignKey(Wave, on_delete=models.DO_NOTHING, default="", blank=True, null=True)
    scale = models.ForeignKey(Scale, on_delete=models.DO_NOTHING)
    quantity = models.IntegerField(default=1, blank=False, null=False)

    class Meta:
        indexes = [
            models.Index(fields=["name", "manufacturer", "license", "line", "scale", ]),
            models.Index(fields=["manufacturer", ]),
            models.Index(fields=["license", ]),
            models.Index(fields=["line", ]),
            models.Index(fields=["scale", ]),
            models.Index(fields=["name", ]),
        ]
        ordering = ["name", "manufacturer", "license", "line", "wave", "created_ts", ]


class GoogleCredentials(GoogleModelMixin):
    credentials = models.TextField(max_length=4096, blank=False)

    class Meta:
        indexes = [
            models.Index(fields=["name", ]),
        ]
        ordering = ["name", ]
        verbose_name_plural = "Google Credentials"


class GoogleSheets(GoogleModelMixin):
    sheet_id = models.CharField(max_length=100, blank=False)
    sheet_range = models.CharField(max_length=100, blank=False)
    credentials = models.ForeignKey(GoogleCredentials, on_delete=models.DO_NOTHING)

    class Meta:
        indexes = [
            models.Index(fields=["name", ]),
            models.Index(fields=["sheet_id", ]),
        ]
        ordering = ["name", ]
        verbose_name_plural = "Google Sheets"

    @admin.display()
    def sheet_data_link(self):
        return format_html('<a href="/toys/sheet/data/{}" target="_blank">View sheet data</a>', self.id)