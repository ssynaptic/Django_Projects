from django.shortcuts import render
from django.http import (HttpResponseRedirect,
                         HttpResponse)
from .forms import (LogInForm,
                    SignUpForm)
from .models import User

# Create your views here.
def get_login_data(request):
    if request.method == "POST":
        form = LogInForm(request.POST)

        if form.is_valid():
            print(form.cleaned_data)
            if User.objects.filter(username=form.cleaned_data["username"], password=form.cleaned_data["password"]).exists():
                return HttpResponseRedirect("/home/init")

    else:
        form = LogInForm()

    return render(request=request,
                  template_name="login_form.html",
                  context={"form": form,
                           "failed_login": True})

def get_signup_data(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)

        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            User.objects.create(first_name=first_name,
                                last_name=last_name,
                                username=username,
                                password=password)
            return HttpResponseRedirect("/home/registered")

    else:
        form = SignUpForm()

    return render(request=request,
                  template_name="signup_form.html",
                  context={"form": form})