from django.urls import path
from .views import (SignUpView, LogInView)

app_name = 'users-app'

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup-view'),
    path('login/', LogInView.as_view(), name='login-view'),
]
