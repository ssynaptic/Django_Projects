from django.contrib import admin
from django.urls import path, include
from .views import to_index

app_name = 'core-app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', to_index),
    path('accounts/', include('users.urls', namespace='users-app')),
    path('home/', include('home.urls', namespace='home-app')),
]
