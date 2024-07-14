from user.api.serializers import RegisterSerializer, UserInfoSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.db import transaction
from django.contrib.auth.models import User

@api_view(['POST'])
@transaction.atomic
def register(request):
    data = request.data
    serializer = RegisterSerializer(data=data)
    if serializer.is_valid():
        user = serializer.save()
        user.set_password(data['password'])
        user.save()
        user_data = UserInfoSerializer(user)
        return Response({
            "message":"Register Successfully",
            "data":user_data.data
        },status=status.HTTP_201_CREATED)
    
    return Response(
        serializer.errors,
        status=status.HTTP_422_UNPROCESSABLE_ENTITY
    )