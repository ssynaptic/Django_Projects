from django.urls import path
from .views import (IndexView, SignUpView,
                    LogInView, handle_uploaded_file)

app_name = 'users-app'

urlpatterns = [
    path('', IndexView.as_view(), name='index-view'),
    path('signup/', SignUpView.as_view(), name='signup-view'),
    path('login/', LogInView.as_view(), name='login-view'),
    path('upload-photo/', handle_uploaded_file, name='upload-photo-view'),
]
