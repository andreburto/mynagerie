from django.contrib import admin
from django.db import models
from django.utils.html import format_html


# Create your models here.
class GoogleModelMixin(models.Model):
    name = models.CharField(max_length=30, blank=False)

    class Meta:
        abstract = True

    def __repr__(self):
        return f"{self.__class__.__name__}: {self.name}"

    def __str__(self):
        return f"{self.name}"


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
