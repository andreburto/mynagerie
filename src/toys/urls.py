from django.urls import path

from . import views


urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('list', views.toy_list, name="toy_list"),
]
