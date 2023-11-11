from django.urls import path
from .views import (init,
                    welcome)

app_name = 'home-app'

urlpatterns = [
    path('init/', init, name='init'),
    path('welcome/<int:pk>', welcome, name='welcome'),
    # path('registered/', registered, name='registered'),
]