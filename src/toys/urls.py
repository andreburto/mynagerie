from django.urls import path

from toys import views


urlpatterns = [
    path('', views.dashboard, name="dashboard"),
    path('data', views.dashboard_data, name="dashboard_data"),
    path('sheet', views.sheet, name="sheet"),
    path('sheet/data', views.sheet_data, name="sheet_data"),
    path('sheet/data/<int:id>', views.sheet_data, name="sheet_data_by_id"),
]
