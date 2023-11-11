from django.shortcuts import render
from django.http import (HttpResponseRedirect,
                         HttpResponse)
from django.urls import reverse_lazy
from .forms import (LogInForm,
                    SignUpForm)
from .models import User

# Create your views here.
def get_login_data(request):
    if request.method == "POST":
        form = LogInForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user_object = User.objects.filter(username=username, password=password).first()
            if user_object:
                pk = user_object.id
                return HttpResponseRedirect(reverse_lazy("home-app:welcome", kwargs={"pk": pk}))

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

            if User.objects.filter(username=username, password=password).exists():
                return HttpResponse("There is another user with the same username and password")

            else:
                User.objects.create(first_name=first_name,
                                    last_name=last_name,
                                    username=username,
                                    password=password)
                return HttpResponseRedirect(reverse_lazy("accounts-app:login"))

    else:
        form = SignUpForm()

    return render(request=request,
                  template_name="signup_form.html",
                  context={"form": form})