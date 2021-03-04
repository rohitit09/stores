from django.urls import path,include
from .views import StoreList,Getlink,ProductStore,ListProducts
from . import  views

urlpatterns = [
    path('create_store', StoreList.as_view()),
    path('create_product', ProductStore.as_view()),
    path('view_store/<str:id>/' ,Getlink.as_view()),
    path('view_products/<str:id>', ListProducts.as_view()),
]