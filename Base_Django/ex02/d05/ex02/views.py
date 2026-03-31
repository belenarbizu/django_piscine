from django.shortcuts import render
from .forms import InputForm
import datetime
from django.conf import settings
import os


def index(request):
    context = {}
    history = []
    context['form'] = InputForm()

    if settings.LOG_PATH:
        if os.path.exists(settings.LOG_PATH):
            with open(settings.LOG_PATH, 'r') as f:
                history = f.readlines()
        else:
            with open(settings.LOG_PATH, 'w') as f:
                pass

    if request.method == 'POST':
        form = InputForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['text']
            timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            history.append(f"{timestamp} - {text}\n")
            context['history'] = history

            with open(settings.LOG_PATH, 'a') as f:
                f.write(f"{timestamp} - {text}\n")

    return render(request, 'ex02/index.html', context)


