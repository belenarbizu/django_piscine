from django.shortcuts import render
from django.conf import settings
from django.http import JsonResponse
import random
import time

DURATION = 42

def update_session_name(request):
    """Helper para obtener o actualizar el nombre en la sesión basado en el tiempo."""
    now = time.time()
    expiry = request.session.get("expiry", 0)
    
    if now > expiry:
        request.session["name"] = random.choice(settings.NAMES)
        request.session["expiry"] = now + DURATION

    return request.session["name"], max(0, request.session["expiry"] - now)

def index(request):
    name, _ = update_session_name(request)
    return render(request, "ex00/index.html", {"name": name})

def get_name(request):
    """Endpoint para AJAX que devuelve el nombre actual en JSON."""
    name, time_left = update_session_name(request)
    return JsonResponse({"name": name, "time_left": time_left})