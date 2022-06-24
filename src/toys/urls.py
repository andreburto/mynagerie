from django.urls import path

from toys import views


urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('data', views.dashboard_data, name="dashboard_data"),
    path('list', views.toy_list, name="toy_list"),
]
