from django.urls import path
from .views import (logout_user,
                    IndexView,
                    SearchView,
                    UserView)

app_name = 'home-app'

urlpatterns = [
    path('', IndexView.as_view(), name='index-view'),
    path('search/', SearchView.as_view(), name="search-view"),
    path('user/username=<str:username>', UserView.as_view(), name='user-view'),
    path('exit/', logout_user, name='logout-view')
]
