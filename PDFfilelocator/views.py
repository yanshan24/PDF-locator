from django.shortcuts import render
from .models import *
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegistrationSerializer
from drf_yasg.utils import swagger_auto_schema

@swagger_auto_schema(method='post', request_body=RegistrationSerializer)
@api_view(['POST'])
def register(request):
    # register an account
    if Author.objects.filter(email=request.data["email"]).exists():
        return Response({'message':"Email already in use"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid(): # make sure data match the model
        author = serializer.save()
        return Response({'authorID':author.authorID}, status=status.HTTP_201_CREATED)
    else:
        return Response({'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)


        