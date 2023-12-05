from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import logout
from django.views.generic.base import View
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse_lazy
from django.shortcuts import render

from .models import Post
from users.models import UserAccount, UserProfile

from .utils import is_user_logged_in

from users.models import UserAccount

# Create your views here.
class IndexView(LoginRequiredMixin, View):
    def get(self, request):
        context = {}
        posts_queryset = Post.objects.all()
        if posts_queryset.exists():
            posts = []
            for post in posts_queryset:
                first_name = post.owners_profile.user_account.first_name
                last_name = post.owners_profile.user_account.last_name
                username = post.owners_profile.user_account.username
                post_content = post.post_content
                views = post.views
                posts.append((first_name, last_name, username, post_content, views))
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
    def get(self, request):
        pass
    
    def post(self, request):
        query = request.POST["query"]
        return HttpResponse(f"Your query is {query}")
    
class UserView(LoginRequiredMixin, View):
    def get(self, request, username):
        user_account = UserAccount.objects.get(username=username)
        user_profile = UserProfile.objects.get(user_account=user_account)
        print(user_profile)
        context = {}

        return render(request=request,
                      template_name="home/user.html",
                      context=context)
        # return HttpResponse(f"Your username is {username}")

    def post(self, request):
        pass

class CreatePostView(LoginRequiredMixin, View):
    def get(self, request):
        return HttpResponse("Here you will can create your posts")

    def post(self, request):
        pass

@login_required(login_url="/accounts/access")
def logout_user(request):
    username = is_user_logged_in(request=request)
    if username != None:
        logout(request=request)
        return HttpResponseRedirect(reverse_lazy("users-app:login-view"))