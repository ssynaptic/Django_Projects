from django.views.generic.base import TemplateView, View
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render
# from django.shortcuts import redirect

from .forms import SignUpForm, LogInForm

from .models import UserAccount, UserProfile

# Create your views here.
class IndexView(TemplateView):
    template_name = "users/index.html"
# class SignUpView(CreateView):
#     model = UserAccount
#     success_url = reverse_lazy("users-app:login-view")
#     template_name = "users/signup.html"
#     form_class = SignUpForm

#     def form_valid(self, form):
#         # super().form_valid(form)
#         first_name = form.cleaned_data["first_name"]
#         last_name = form.cleaned_data["last_name"]
#         username = form.cleaned_data["username"]
#         password = form.cleaned_data["password"]
#         UserAccount.objects.create_user(first_name=first_name,
#                                         last_name=last_name,
#                                         username=username,
#                                         password=password)
#         ua = UserAccount.objects.get(first_name=first_name,
#                                      last_name=last_name,
#                                      username=username)
#         UserProfile.objects.create(user_account=ua)
#         return HttpResponseRedirect(redirect_to=self.success_url)
    
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         return context

class SignUpView(View):
    def get(self, request):
        form = SignUpForm()
        return render(request=request,
                      template_name="users/signup.html",
                      context={"form": form})
    def post(self, request):
        first_name = request.POST["first_name"]
        last_name = request.POST["last_name"]
        username = request.POST["username"]
        password = request.POST["password"]
        UserAccount.objects.create_user(first_name=first_name,
                                        last_name=last_name,
                                        username=username,
                                        password=password)
        ua = UserAccount.objects.get(first_name=first_name,
                                     last_name=last_name,
                                     username=username)
        UserProfile.objects.create(user_account=ua)
        return HttpResponseRedirect(redirect_to=reverse_lazy("home-app:index-view"))

class LogInView(View):
    def get(self, request):
        form = LogInForm()
        return render(request=request,
                      template_name="users/login.html",
                      context={"form": form})
    
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
            return HttpResponse("Failed to login")

def success(request):
    return HttpResponse("Account Created Successfully")
