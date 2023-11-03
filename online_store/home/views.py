from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def init(request):
    return HttpResponse("You are on the init page of the home app")

def registered(request):
    return HttpResponse("You are now registered congratulations")