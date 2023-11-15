from django.contrib import admin
from django.urls import include, path

app_name = 'main-app'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('users.urls', namespace='users-app'))
]