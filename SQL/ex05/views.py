from django.http import HttpResponse
from django.shortcuts import render
from .models import Movies


def populate(request):
    try:
        data = [
            {"title": "The Phantom Menace", "episode_nb": 1, "director": "George Lucas", "producer": "Rick McCallum", "release_date": "1999-10-16"},
            {"title": "Attack of the Clones", "episode_nb":2, "director": "George Lucas", "producer": "Rick McCallum", "release_date": "2002-05-16"},
            {"title": "Revenge of the Sith", "episode_nb":3, "director": "George Lucas", "producer": "Rick McCallum", "release_date": "2005-05-19"},
            {"title": "A New Hope", "episode_nb":4, "director": "George Lucas", "producer": "Gary Kurtz, Rick McCallum", "release_date": "1977-05-25"},
            {"title": "The Empire Strikes Back", "episode_nb":5, "director": "Irvin Kershner", "producer": "Gary Kutz, Rick McCallum", "release_date": "1980-05-17"},
            {"title": "Return of the Jedi", "episode_nb":6, "director": "Richard Marquand", "producer": "Howard G. Kazanjian, George Lucas, Rick McCallum", "release_date": "1983-05-25"},
            {"title": "The Force Awakens", "episode_nb":7, "director": "J. J. Abrams", "producer": "Kathleen Kennedy, J. J. Abrams, Bryan Burk", "release_date": "2015-12-11"}
        ]
        results = []
        for movie in data:
            _, created =Movies.objects.get_or_create(episode_nb=movie["episode_nb"], defaults=movie)
            if created:
                results.append("OK.")
            else:
                results.append("Already exists.")
        return HttpResponse(results)
    except Exception as e:
        return HttpResponse(f"Error: {e}")


def display(request):
    try:
        movies = Movies.objects.all()
        if not movies:
            return HttpResponse("No data available.")
        return render(request, "ex05/ex05_display.html", {"movies": movies})
    except Exception as e:
        return HttpResponse(f"Error: {e}")


def remove(request):
    try:
        if request.method == "POST":
            title = request.POST.get("title")
            if title:
                Movies.objects.filter(title=title).delete()

        titles = Movies.objects.values_list("title", flat=True)
        if not titles:
            return HttpResponse("No data available.")
        return render(request, "ex05/ex05_remove.html", {"titles": titles})
    except Exception as e:
        return HttpResponse(f"Error: {e}")