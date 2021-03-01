from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response


from apps.store.models import Store
from apps.store.serializers import StoreSerializer
import string
import random
# Create your views here.

class StoreList(generics.ListCreateAPIView):
    queryset = Store.objects.all()
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
        return Response({'link':request.headers['Host']+'store/'+temp.get_absolute_url()})





class Getlink(generics.RetrieveUpdateAPIView):
    lookup_field='id'
    queryset = Store.objects.all()
    serializer_class = StoreSerializer

    

    