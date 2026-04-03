from django.http import HttpResponse
from django.shortcuts import render
from ex01.models import Movies


def populate(request):
    try:
        results = []
        Movies.objects.create(title="The Phantom Menace", episode_nb=1, director="George Lucas", producer="Rick McCallum", release_date="1999-05-19")
        results.append("OK.")
        Movies.objects.create(title="Attack of the Clones", episode_nb=2, director="George Lucas", producer="Rick McCallum", release_date="2002-05-16")
        results.append("OK.")
        Movies.objects.create(title="Revenge of the Sith", episode_nb=3, director="George Lucas", producer="Rick McCallum", release_date="2005-05-19")
        results.append("OK.")
        Movies.objects.create(title="A New Hope", episode_nb=4, director="George Lucas", producer="Gary Kurtz, Rick McCallum", release_date="1977-05-25")
        results.append("OK.")
        Movies.objects.create(title="The Empire Strikes Back", episode_nb=5, director="Irvin Kershner", producer="Gary Kurtz, Rick McCallum", release_date="1980-05-17")
        results.append("OK.")
        Movies.objects.create(title="Return of the Jedi", episode_nb=6, director="Richard Marquand", producer="Howard G. Kazanjian, George Lucas, Rick McCallum", release_date="1983-05-25")
        results.append("OK.")
        Movies.objects.create(title="The Force Awakens", episode_nb=7, director="J. J. Abrams", producer="Kathleen Kennedy, J. J. Abrams, Bryan Burk", release_date="2015-12-11")
        results.append("OK.")
        return HttpResponse(results)
    except Exception as e:
        return HttpResponse(f"Error: {e}")


def display(request):
    try:
        movies = Movies.objects.all()
        if not movies:
            return HttpResponse("No data available.")
        return render(request, "ex03/ex03_display.html", {"movies": movies})
    except Exception as e:
        return HttpResponse(f"Error: {e}")