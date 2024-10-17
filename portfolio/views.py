from django.http import HttpResponse
from django.shortcuts import render
from .forms import DjangoForm
from service.models import Service


def HomePage(request):
    return render(request, "index.html")


def AboutPage(request):
    return render(request, "about.html")


def ServicePage(request):
    # for descending just add - before column name
    serviceDatas = Service.objects.all().order_by('service_title')
    data = {
        "serviceDatas": serviceDatas,
    }
    return render(request, "services.html", data)


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
        print(value1, value2)
        output = int(value1) + int(value2)
        data = {"value1": value1, "value2": value2, "output": output}
        return render(request, "output.html", data)
    except:
        pass

    return render(request, "output.html")


def djangoForm(request):
    data = {"fn": DjangoForm}
    return render(request, "djangoform.html", data)


from django.shortcuts import render


def Calculator(request):
    data = {"value1": "", "value2": "", "operator": "", "output": "", "error": ""}

    if request.method == "POST":
        try:
            value1 = request.POST["value1"]
            value2 = request.POST["value2"]
            operator = request.POST["operator"]

            # Store the input values in data for rendering
            data["value1"] = value1
            data["value2"] = value2
            data["operator"] = operator

            # Validate inputs
            if value1 == "":
                data["error"] = "Value1 must be provided"
            elif value2 == "":
                data["error"] = "Value2 must be provided"
            elif operator == "":
                data["error"] = "Operator must be provided"
            else:
                # Convert values to integers and perform calculation
                try:
                    num1 = int(value1)
                    num2 = int(value2)

                    if operator == "+":
                        data["output"] = num1 + num2
                    elif operator == "-":
                        data["output"] = num1 - num2
                    elif operator == "*":
                        data["output"] = num1 * num2
                    elif operator == "/":
                        if num2 == 0:
                            data["error"] = "Cannot divide by zero"
                        else:
                            data["output"] = num1 / num2
                    else:
                        data["error"] = "Invalid operator"
                except ValueError:
                    data["error"] = "Invalid number format"

        except Exception as e:
            data["error"] = str(e)

    return render(request, "calculator.html", data)
