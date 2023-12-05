from django.urls import path
from .views import (logout_user,
                    IndexView,
                    SearchView,
                    UserView,
                    CreatePostView)

app_name = 'home-app'

urlpatterns = [
    path('', IndexView.as_view(), name='index-view'),
    path('search/', SearchView.as_view(), name="search-view"),
    path('user/username=<str:username>', UserView.as_view(), name='user-view'),
    path('create-post/', CreatePostView.as_view(), name='create-post-view'),
    path('exit/', logout_user, name='logout-view')
]
