from django.urls import path
from .views import init

app_name = 'home'

urlpatterns = [
    path('init/', init, name='init'),
]