from django.shortcuts import render


def index(request):
    return render(request, "ex01/index.html")


def django_history(request):
    return render(request, "ex01/django.html")


def display(request):
    return render(request, "ex01/display.html")


def templates(request):
    return render(request, "ex01/templates.html")

