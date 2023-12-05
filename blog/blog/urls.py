from django.contrib import admin
from django.urls import path, include

app_name = 'core-app'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls', namespace='users-app')),
    path('home/', include('home.urls', namespace='home-app')),
]
