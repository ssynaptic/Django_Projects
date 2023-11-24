from django.urls import path
from .views import (IndexView, SignUpView,
                    LogInView, success)

app_name = 'users-app'

urlpatterns = [
    path('', IndexView.as_view(), name='index-view'),
    path('signup/', SignUpView.as_view(), name='signup-view'),
    path('login/', LogInView.as_view(), name='login-view'),
    path('success/', success, name='success'),
]
