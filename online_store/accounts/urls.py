from django.urls import path
from .views import (get_login_data,
                    get_signup_data)
app_name = "accounts"
urlpatterns = [
    path('login/', get_login_data, name='login'),
    path('signup/', get_signup_data, name='signup')
    # path('thanks/', thanks, name='loged'),
]