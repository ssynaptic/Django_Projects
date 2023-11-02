from django.shortcuts import render
from django.http import (HttpResponseRedirect,
                         HttpResponse)
from .forms import LoginForm
from .models import User

# Create your views here.
def get_login_data(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            if User.objects.filter(username=form.cleaned_data["username"], password=form.cleaned_data["password"]).exists():
                return HttpResponseRedirect("/home/init")

    else:
        form = LoginForm()

    return render(request=request,
                  template_name="login_form.html",
                  context={"form": form})

def thanks(request):
    # return HttpResponse("Thanks for login")
    return render(request=request,
                  template_name="home_initial.html",
                  context={})