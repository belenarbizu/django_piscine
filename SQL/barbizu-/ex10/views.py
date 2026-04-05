from django.shortcuts import render
from .models import People
from django.http import HttpResponse
from .forms import SearchForm


def index(request):
    try:
        form = SearchForm()
        genders = People.objects.values_list("gender", flat=True).distinct()
        characters = []
        empty_list = False
        if request.method == "POST":
            form = SearchForm(request.POST)
            if form.is_valid():
                min_date = form.cleaned_data["min_date"]
                max_date = form.cleaned_data["max_date"]
                diameter = form.cleaned_data["diameter"]
                gender = form.cleaned_data["gender"]

                results = People.objects.filter(
                    gender=gender,
                    homeworld__diameter__gt=diameter,
                    movies__release_date__range=(min_date, max_date)
                ).values(
                    'name',
                    'gender',
                    'movies__title',
                    'homeworld__name',
                    'homeworld__diameter'
                ).order_by('name')

                for item in results:
                    characters.append({
                        "name": item['name'],
                        "gender": item['gender'],
                        "film": item['movies__title'],
                        "homeworld": item['homeworld__name'],
                        "diameter": item['homeworld__diameter']
                    })
                if not characters:
                    empty_list = True

        return render(request, "ex10/index.html", {"characters": characters, "genders": genders, "form": form, "empty_list": empty_list})
    except Exception as e:
        return HttpResponse(f"Error: {e}")





            