from django.http import HttpResponse


def Home(request):
    return HttpResponse("Welcome to Home page!")


def aboutUs(request):
    return HttpResponse("Welcome to About us page!")


def courses(request):
    return HttpResponse("Welcome to About us page!")


def OneCourse(request, course):
    return HttpResponse("Your courseNames is: " + course)


def singleCourse(request, courseName):
    return HttpResponse("Your courseNames is: " + courseName)


def singleCourseId(request, courseId):
    return HttpResponse("Your courseId is: " + str(courseId))


def slugCourses(request, slugCourse):
    return HttpResponse("Your courseName is: " + slugCourse)
