from django.shortcuts import render, get_object_or_404
from .models import *
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework import status
from .serializers import *
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
import json

@swagger_auto_schema(
        method='post',
        request_body=RegistrationSerializer,
        responses={
        201: "Created: {'authorID': authorID}",
        400: 'Bad Request',
        422: 'Unprocessable Entity',
    },)
@api_view(['POST'])
def register(request):
    """
    Register a new author.
    """
    if Author.objects.filter(email=request.data["email"]).exists():
        return Response({'message':"Email already in use"}, status=status.HTTP_422_UNPROCESSABLE_ENTITY)
    serializer = RegistrationSerializer(data=request.data)
    if serializer.is_valid(): # make sure data match the model
        author = serializer.save()
        author_serializer = AuthorSerializer(author)
        return Response(author_serializer.data, status=status.HTTP_201_CREATED)
    else:
        return Response({'message':serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def upload(request):
    """
    Upload PDF file and save its data.
    """
    authorID = request.data.get('authorID')
    author = Author.objects.filter(authorID=authorID)
    if not author:
        return Response({'message': 'Author does not exist'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = HistoryItemSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET'])
def get_history(request, authorID):
    """
    Get specific history with authorID and id
    """
    history = get_object_or_404(HistoryItem, authorID=authorID, id=request.query_params.get('id'))
    serializer = HistoryItemSerializer(history)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_history(request, authorID):
    """
    Get all history with authorID and is_manager
    """
    author = Author.objects.filter(authorID=authorID).first()
    if not author:
        return Response({'message':"Author does not exist"}, status=status.HTTP_404_NOT_FOUND)
    if author.is_manager:
        history_items = HistoryItem.objects.all()
    else:
        history_items = HistoryItem.objects.filter(authorID=authorID)

    if history_items.count() > 0:
        serializer = HistoryItemSerializer(history_items, many=True)
        return Response(serializer.data)
    else:
        return Response({'message':"History empty"}, status=status.HTTP_404_NOT_FOUND)