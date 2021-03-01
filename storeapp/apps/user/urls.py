from django.contrib import admin
from django.urls import include, path

from .views import UserView, login

urlpatterns = [
    path('signup', UserView.as_view()),
    path('login', login)
]
