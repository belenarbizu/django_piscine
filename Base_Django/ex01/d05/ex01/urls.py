from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("django/", views.django_history, name="django_history"),
    path("display/", views.display, name="display"),
    path("templates/", views.templates, name="templates"),
]