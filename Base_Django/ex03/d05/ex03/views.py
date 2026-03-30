from django.shortcuts import render

# Create your views here.
def index(request):
    noir = (0, 0, 0)
    rouge = (255, 0, 0)
    bleu = (0, 0, 255)
    vert = (0, 255, 0)

    change_value = int(255 / 50)

    colors = []
    colors.append([noir, rouge, bleu, vert])
    for i in range(50):
        noir = (0 + i * change_value, 0 + i * change_value, 0 + i * change_value)
        rouge = (255 - i * change_value, 0, 0)
        bleu = (0, 0, 255 - i * change_value)
        vert = (0, 255 - i * change_value, 0)
        colors.append([noir, rouge, bleu, vert])
    return render(request, 'ex03/index.html', {'colors': colors})