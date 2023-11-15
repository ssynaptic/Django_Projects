from django.urls import path
from . import views

app_name = "users-app"

urlpatterns = [
    path("", views.index, name="index-page-view"),
    path("create/", views.create_account, name="create")
]