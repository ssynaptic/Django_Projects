from django.urls import path
from .views import (get_login_data,
                    thanks)
app_name = "accounts"
urlpatterns = [
    path('login/', get_login_data, name="login"),
    # path('thanks/', thanks, name='loged'),
]