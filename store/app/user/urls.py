from django.urls import path

from . import views

app_name = 'user'

urlpatterns = [
    path('create/', views.CreateUserView.as_view(), name='create'),
    path('token/', views.CreateTokenView.as_view(), name='token'),
    path('hello/', views.ManageUserView.as_view(), name='hello'),
]