from django.contrib import admin
from django.urls import path,include

from .views import StoreList,Getlink

urlpatterns = [
    path('create_store', StoreList.as_view()),
     path('view_store/<str:id>' ,Getlink.as_view()),
]