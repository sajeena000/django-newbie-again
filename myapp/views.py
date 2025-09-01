from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):
    return HttpResponse("Hello!")

def sajeena(request):
    return HttpResponse("Hello! Sajeena!")

def iloveanime(request):
    return HttpResponse("Sajeena miss loves anime.")