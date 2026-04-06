from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("get_name/", views.get_name, name="get_name"),
    path("login/", views.login, name="login"),
    path("registration/", views.registration, name="registration")
]