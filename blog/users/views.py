from django.views.generic.base import TemplateView, View
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render
from django.shortcuts import redirect

from .forms import SignUpForm, LogInForm, UploadFileForm
from .utils import handle_uploaded_file

from .models import UserAccount#, UserProfile

# Create your views here.
class IndexView(TemplateView):
    template_name = "users/index.html"
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
        # ua = UserAccount.objects.get(first_name=first_name,
        #                              last_name=last_name,
        #                              username=username)
        # UserProfile.objects.create(user_account=ua)
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
            form = LogInForm()
            context = {
                "form": form,
                "login_failed": True
            }
            return render(request=request,
                          template_name="users/login.html",
                          context=context)

def upload_file(request):
    handle_uploaded_file()
    # if request.method == "POST":
        # form = UploadFileForm
# def success(request):
#     return HttpResponse("Account Created Successfully")
