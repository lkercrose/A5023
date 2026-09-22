from django.http import HttpResponse


def index(request):
    return HttpResponse("Actividad 1.1 - Entornos de desarrollo")