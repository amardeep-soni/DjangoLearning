"""
URL configuration for portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path
from portfolio import views

urlpatterns = [
    path("admin/", admin.site.urls),
    # static url
    path("", views.Home),
    path("about-us/", views.aboutUs),
    path("courses/", views.courses),
    # Dynamic Url
    # this will accept any type value either int, str or slug
    path("course/<course>", views.OneCourse),
    # with different type
    # this only accept string value like python, python@-
    path("course1/<str:courseName>", views.singleCourse),
    # this only accept integer value like 1
    path("course2/<int:courseId>", views.singleCourseId),
    # this only accept slug value like python-is-available
    path("course3/<slug:slugCourse>", views.slugCourses),
]
