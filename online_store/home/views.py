from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def init(request):
    return HttpResponse("You are on the init page of the home app")

def welcome(request, pk):
    # return HttpResponse(f"Your id is: {pk}")
    return render(request=request,
                  template_name="welcome_page.html")