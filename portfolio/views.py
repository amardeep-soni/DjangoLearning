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


def UserForm(request):
    data = {}
    try:
        value1 = request.GET["value1"]
        value2 = request.GET["value2"]
        output = int(value1) + int(value2)
        data = {"value1": value1, "value2": value2, "output": output}
    except:
        pass

    return render(request, "userForm.html", data)
