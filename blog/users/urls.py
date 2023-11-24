from django.urls import path
from .views import (IndexView, SignUpView,
                    LogInView, success)

app_name = 'users-app'

urlpatterns = [
    path('', IndexView.as_view(), name='index-view'),
    path('create/', SignUpView.as_view(), name='create'),
    path('access/', LogInView.as_view(), name='access'),
    path('success/', success, name='success'),
]
