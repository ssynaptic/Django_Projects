from django.urls import path
from .views import (init,
                    registered)

app_name = 'home'

urlpatterns = [
    path('init/', init, name='init'),
    path('registered', registered, name='registered'),
]