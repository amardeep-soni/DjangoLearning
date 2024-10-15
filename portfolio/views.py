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


def UserForm2(request):
    data = {}
    try:
        value1 = request.POST["value1"]
        value2 = request.POST["value2"]
        output = int(value1) + int(value2)
        data = {"value1": value1, "value2": value2, "output": output}
    except:
        pass

    return render(request, "userForm2.html", data)


def UserForm3(request):
    data = {}
    try:
        value1 = request.POST["value1"]
        value2 = request.POST["value2"]
        output = int(value1) + int(value2)
        data = {"value1": value1, "value2": value2, "output": output}
        return render(request, "output.html", data)
    except:
        pass

    return render(request, "userForm3.html")


def UserForm4(request):
    return render(request, "userForm4.html")


def Output(request):
    data = {}
    try:
        value1 = request.POST["value1"]
        value2 = request.POST["value2"]
        output = int(value1) + int(value2)
        data = {"value1": value1, "value2": value2, "output": output}
        return render(request, "output.html", data)
    except:
        pass

    return render(request, "userForm3.html")
