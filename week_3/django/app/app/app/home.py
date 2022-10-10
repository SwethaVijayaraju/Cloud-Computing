# pages/views.py
from django.http import HttpResponse


def homepage(request):
    return HttpResponse("Hi from MSIS!")
