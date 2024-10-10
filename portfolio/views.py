from django.http import HttpResponse
from django.shortcuts import render


def HomePage(request):
    data = {
        "title": "Home",
        "heading": "Welcome to My Portfolio",
        "paragraph": "This is a simple portfolio template built using Django.",
        "isActive": True,
    }
    return render(request, "index.html", data)


def AboutPage(request):
    return render(request, "about.html")



def ServicePage(request):
    data = {
        "services": [
            {
                "title": "Service 1",
                "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
            },
            {
                "title": "Service 2",
                "description": "Nullam facilisis dolor ac neque convallis, at varius ligula condimentum.",
            },
            {
                "title": "Service 3",
                "description": "Ut tincidunt velit vel nunc pharetra, vel consectetur erat bibendum.",
            },
        ],
    }
    return render(request, "services.html", data)


def ContactPage(request):
    return render(request, "contact.html")
