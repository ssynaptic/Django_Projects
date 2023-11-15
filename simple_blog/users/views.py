from django.shortcuts import render
from django.http import HttpResponse
from . import forms
from .models import UserAccount, UserProfile

# Create your views here.
def index(request):
    return render(request=request,
                  template_name="users-index-page.html",
                  context={})

def create_account(request):
    if request.method == "GET":
        form = forms.AccountCreationForm()
        return render(request=request,
                      template_name="create_account.html",
                      context={"form": form})

    if request.method == "POST":
        form = forms.AccountCreationForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            ua = UserAccount(
                first_name=first_name,
                last_name=last_name,
                username=username,
                password=password)

            up = UserProfile(account=ua)
            ua.save()
            up.save()
            return HttpResponse("Axcount Created Successfully")