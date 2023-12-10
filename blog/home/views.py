from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views.generic.base import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import Post
from users.models import UserAccount

from .utils import is_user_logged_in

from .forms import CreatePostForm

# Create your views here.
class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        context = {}
        posts_queryset = Post.objects.all()
        if posts_queryset.exists():
            posts = []
            for post in posts_queryset:
                first_name = post.owners_profile.first_name
                last_name = post.owners_profile.last_name
                username = post.owners_profile.username
                post_content = post.post_content
                views = post.views
                date = post.date_and_time_published.strftime("%d/%m/%y")
                posts.append((first_name, last_name,
                              username, post_content,
                              views, date))
            context.update({"there_are_posts": True})
            context.update({"data": posts})
        else:
            context.update({"there_are_products": False})
        return render(request=request,
                      template_name="home/index.html",
                      context=context)

    def post(self, request):
        pass

class SearchView(LoginRequiredMixin, View):
    def post(self, request):
        query = request.POST["query"]
        return HttpResponse(f"Your query is {query}")

class UserView(LoginRequiredMixin, View):
    def get(self, request, username):
        user_account = UserAccount.objects.get(username=username)
        context = {"user_account": user_account}
        return render(request=request,
                      template_name="home/user.html",
                      context=context)
class CreatePostView(LoginRequiredMixin, View):
    def get(self, request):
        form = CreatePostForm()
        context = {"form": form}
        return render(request=request,
                      template_name="home/create-post.html",
                      context=context)

    def post(self, request):
        form = CreatePostForm(request.POST)
        if form.is_valid():
            ua = UserAccount.objects.get(username=request.user.username,
                                         password=request.user.password)
            Post.objects.create(owners_profile=ua,
                                post_content=form.cleaned_data["post_content"])
            return HttpResponseRedirect(reverse_lazy("home-app:index-view"))

@login_required(login_url="/accounts/access")
def logout_user(request):
    username = is_user_logged_in(request=request)
    if username != None:
        logout(request=request)
        return HttpResponseRedirect(reverse_lazy("users-app:login-view"))