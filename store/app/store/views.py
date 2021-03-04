from django.shortcuts import render
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from django.db.models import Avg, Count

from core.models import Store,Products,Orders,Category
from store.serializers import StoreSerializer,CategorySerializer,ProductsSerializer,OrdersSerializer
from rest_framework import generics, authentication, permissions
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings
from user.serializers import AuthTokenSerializer
from collections import Counter

# Create your views here.

class StoreList(generics.CreateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)

    # queryset = Store.objects.all()
    serializer_class = StoreSerializer

    # permission_classes = [IsAdminUser]
    def post(self,request):
        name=request.data['name']
        address=request.data['address']
        serl=StoreSerializer(data={'name':name,'address':address})
        if serl.is_valid():
            temp=serl.save()

        
        # import ipdb;ipdb.set_trace()
        # print(temp.get_absolute_url)
        return Response({'link':request.headers['Host']+'/api/store'+temp.get_absolute_url()})


class ProductStore(generics.CreateAPIView):
    # authentication_classes = (authentication.TokenAuthentication,)
    # permission_classes = (permissions.IsAuthenticated,)

    # queryset = Store.objects.all()
    serializer_class = ProductsSerializer

    # permission_classes = [IsAdminUser]
    def post(self,request):
        category=request.data['category']
        
        temp=Category.objects.filter(name=category).first()
        if not temp:
            temp=CategorySerializer(data={'name':category})
            if temp.is_valid():
                temp.save()   

        #import ipdb;ipdb.set_trace()
        serl=ProductsSerializer(data=request.data)
        if serl.is_valid():
            temp=serl.save()
            return Response({'id':temp.id,'product_name':temp.product_name})
        else:
            return  Response({'msg':'invalid requested data'})



class ListProducts(generics.ListAPIView):
    serializer_class = ProductsSerializer

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        queryset = Products.objects.all()
        id = self.request.query_params.get('id', None)
        if id is not None:
            queryset = queryset.filter(Products__id=id)

        sorted_items = queryset.annotate(itemcount=Count('category'))
        sorted_items = sorted_items.order_by('-itemcount')


        return sorted_items
        

# ubs = Publisher.objects.annotate(num_books=Count('book')).order_by('-num_books')[:5]



class Getlink(generics.RetrieveUpdateAPIView):
    authentication_classes = (authentication.TokenAuthentication,)
    permission_classes = (permissions.IsAuthenticated,)
    lookup_field='id'
    queryset = Store.objects.all()
    serializer_class = StoreSerializer