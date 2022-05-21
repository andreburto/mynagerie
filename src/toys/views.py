from django.conf import settings
from django.http import HttpResponse
from django.template.loader import render_to_string

from . import models


# Create your views here.
def dashboard(request):
    return HttpResponse("Dashboard")


def toy_list(request):
    return HttpResponse("Toy List")
