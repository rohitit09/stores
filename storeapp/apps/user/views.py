from datetime import datetime, timedelta

from django.conf import settings
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework_jwt.utils import jwt_encode_handler, jwt_payload_handler

from .models import StoreUser


class UserView(generics.CreateAPIView):
    queryset = StoreUser.objects.all()
    # serializer_class = StoreSerializer
    permission_classes = [AllowAny, ]

    def post(self, request):
        if not self.request.data.get('phone_number'):
            return Response({"message": "Invalid Request"})

        if StoreUser.objects.filter(phone_number=request.data.get('phone_number')):
            return Response({"message": "phone number already registered"})

        user_obj = StoreUser.objects.create(
            phone_number=self.request.data.get('phone_number'))

        user_obj.set_password(request.data.get('password'))
        user_obj.is_active = True
        user_obj.save()

        create_success_message = 'Your registration is completed successfully. Activate your account by entering the OTP which we have sent to your email.'

        return Response({'message': create_success_message})


@api_view(['POST'])
@permission_classes((AllowAny, ))
def login(request):
    phone_number = request.data.get('phone_number')
    password = request.data.get('password')

    if not (phone_number and password):
        return Response({"message": "Invalid Request"})

    user_obj_query = StoreUser.objects.filter(
        phone_number=phone_number)

    if not user_obj_query.exists():
        return Response({"message": "user not found"})

    user_obj = user_obj_query.first()

    if not user_obj.is_active:
        return Response({"message": "user not active"})

    payload = jwt_payload_handler(user_obj)
    token = jwt_encode_handler(payload)

    expiration = datetime.utcnow(
    ) + settings.JWT_AUTH['JWT_EXPIRATION_DELTA']
    expiration_epoch = expiration.timestamp()

    data = {
        "token": token,
        "token_expiration": expiration_epoch
    }
    return Response({'data': data})
