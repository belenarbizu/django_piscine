from django.shortcuts import render
from .models import Planets, People, Movies
from django.http import HttpResponse


def index(request):
    try:
        if request.method == "POST":
            min_date = request.POST.get("min_date")
            max_date = request.POST.get("max_date")
            diameter = request.POST.get("diameter")
            gender = request.POST.get("gender")
            characters = []
            if min_date and max_date and diameter and gender:
                movies = Movies.objects.filter(release_date__range=(min_date, max_date), characters__gender=gender).distinct()
                planets = Planets.objects.filter(diameter__gte=diameter).distinct()
                people = People.objects.filter(gender=gender).distinct()
                print(movies)
                print(planets)
                print(people)
                name = people.values_list("name", flat=True)
                gender = people.values_list("gender", flat=True)
                film = movies.values_list("title", flat=True)
                homeworld = planets.values_list("name", flat=True)
                diameter = planets.values_list("diameter", flat=True)
                for i in range(len(name)):
                    characters.append({"name": name[i], "gender": gender[i], "film": film[i], "homeworld": homeworld[i], "diameter": diameter[i]})
            return render(request, "ex10/ex10_index.html", {"characters": characters})
        
        genders = People.objects.values_list("gender", flat=True).distinct()
        return render(request, "ex10/ex10_index.html", {"genders": genders})
    except Exception as e:
        return HttpResponse(f"Error: {e}")





            