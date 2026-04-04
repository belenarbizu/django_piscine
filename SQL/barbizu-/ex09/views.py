from django.shortcuts import render
from .models import People
from django.http import HttpResponse


def display(request):
    try:
        people = People.objects.filter(homeworld__climate__icontains='windy').order_by('name').select_related('homeworld')
        print(people)
        if not people:
            return HttpResponse("No data available, please use the following command line before use: python3 manage.py loaddata ex09_initial_data.json")
        return render(request, "ex09/ex09_display.html", {"people": people})
    except Exception as e:
        return HttpResponse(f"Error: {e}")

