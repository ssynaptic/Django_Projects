from django.views.generic.base import TemplateView, View
from django.views.generic.edit import CreateView
from django.contrib.auth import authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.shortcuts import render
# from django.shortcuts import redirect

from .forms import SignUpForm, LogInForm

from .models import UserAccount, UserProfile

from uuid import uuid4

# Create your views here.
class IndexView(TemplateView):
    template_name = "users/index.html"
class SignUpView(CreateView):
    model = UserAccount
    success_url = reverse_lazy("users-app:success")
    template_name = "users/signup.html"
    form_class = SignUpForm

    def form_valid(self, form):
        super().form_valid(form)
        first_name = form.cleaned_data["first_name"]
        last_name = form.cleaned_data["last_name"]
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password"]
        ua = UserAccount.objects.get(first_name=first_name,
                                     last_name=last_name,
                                     username=username,
                                     password=password)
        UserProfile.objects.create(user_account=ua)
        current_session_id = uuid4()
        status = "active"
        self.request.session["session_id"] = f"{current_session_id}/{status}"
        return HttpResponseRedirect(redirect_to=self.success_url)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

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
            return HttpResponseRedirect(reverse_lazy("home-app:index"))
        else:
            return HttpResponse("Failed to login")

def success(request):
    return HttpResponse("Account Created Successfully")
