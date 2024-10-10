from django.http import HttpResponse
from django.shortcuts import render


def HomePage(request):
    return render(request, "index.html")


def AboutPage(request):
    return render(request, "about.html")


def ServicePage(request):
    return render(request, "services.html")

def ContactPage(request):
    return render(request, "contact.html")
