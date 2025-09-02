from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "hello/index.html")

def sajeena(request):
    return HttpResponse("Hello! Sajeena!")

def iloveanime(request):
    return HttpResponse("Sajeena miss loves anime.")

def greet(request, name):
    return render(request, "hello/greet.html",{
        "name": name.capitalize()
    })
