from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views.generic.base import TemplateView
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy

from .utils import is_user_logged_in

# Create your views here.
@login_required(login_url="/accounts/access")
def index(request):
    print(request.user.is_authenticated)
    return HttpResponse("welcome user, this is the home page, here you can see your feed")

class IndexView(LoginRequiredMixin, TemplateView):
    template_name = "home/index.html"

@login_required(login_url="/accounts/access")
def logout_user(request):
    username = is_user_logged_in(request=request)
    if username != None:
        logout(request=request)
        return HttpResponseRedirect(reverse_lazy("users-app:login-view"))