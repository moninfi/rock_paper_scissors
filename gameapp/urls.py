from django.contrib import admin
from django.urls import path
from . import views

app_name = "rps_game"

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", views.home),
    # path("display_date/", views.display_date),
    # path("forms/", views.forms, name="forms"),
]
