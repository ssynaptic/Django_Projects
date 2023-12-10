from django.views.generic.base import TemplateView, View
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render
from django.shortcuts import redirect

from .forms import SignUpForm, LogInForm

from .models import UserAccount

# Create your views here.
class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        top_text = "Sign Up"
        bottom_text = "Already have an account? you can"
        go_to = "Log In"
        form_link = reverse_lazy("users-app:signup-view")
        link = reverse_lazy("users-app:login-view")
        return render(request=request,
                      template_name="users/creation-and-access.html",
                      context={"form": form,
                               "top_text": top_text,
                               "bottom_text": bottom_text,
                               "go_to": go_to,
                               "form_link": form_link,
                               "link": link
                      })
    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        password = request.POST["password"]
        UserAccount.objects.create_user(first_name=first_name,
                                        last_name=last_name,
                                        username=username,
                                        password=password)
        return HttpResponseRedirect(redirect_to=reverse_lazy("users-app:login-view"))

class LogInView(View):
    def get(self, request):
        form = LogInForm()
        top_text = "Log In"
        bottom_text = "Don't have an account? you can"
        go_to = "Sign Up"
        form_link = reverse_lazy("users-app:login-view")
        link = reverse_lazy("users-app:signup-view")
        return render(request=request,
                      template_name="users/creation-and-access.html",
                      context={"form": form,
                               "top_text": top_text,
                               "bottom_text": bottom_text,
                               "go_to": go_to,
                               "form_link": form_link,
                               "link": link
                      })

    def post(self, request):
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request=request,
                            username=username,
                            password=password)
        if user is not None:
            login(self.request, user)
            return HttpResponseRedirect(reverse_lazy("home-app:index-view"))
        else:
            form = LogInForm()
            top_text = "Log In"
            bottom_text = "Don't have an account? you can"
            go_to = "Sign Up"
            form_link = reverse_lazy("users-app:login-view")
            link = reverse_lazy("users-app:login-view")
            context = {
                "form": form,
                "login_failed": True,
                "top_text": top_text,
                "bottom_text": bottom_text,
                "go_to": go_to,
                "form_link": form_link,
                "link": link
            }
            return render(request=request,
                          template_name="users/creation-and-access.html",
                          context=context)
