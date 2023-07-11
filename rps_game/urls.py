"""
URL configuration for rps_game project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from gameapp import views

app_name = "rps_game"

urlpatterns = [
    path("admin/", admin.site.urls, name="admin"),
    path("", views.home, name="home"),
    # path("play/", views.play_game, name="play_game"),
    # path("display_date/", views.display_date),
    # path("result/", views.winner, name="winner"),
    path("", include("gameapp.urls")),
    # path("DemoForm/", views.forms, name="forms"),
    # path("DemoForm/", include("forms.urls")),
    # path("DemoForm/", views.form, name="form"),
]
