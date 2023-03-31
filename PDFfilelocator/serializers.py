import datetime
import json
from rest_framework import serializers
from .models import *
import requests

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('email', 'is_manager', 'authorID')

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('authorID', 'email', 'password', 'is_manager')

    def save(self):
        author = Author(
            email=self.validated_data['email'],
            is_manager=self.validated_data['is_manager'],
            username=self.validated_data['email']
        )
        password = self.validated_data['password']
        author.set_password(password)
        author.save()
        return author

class HistoryItemSerializer(serializers.ModelSerializer):
    pdf_file = serializers.CharField(max_length=None, allow_blank=True)
    file_name = serializers.CharField(read_only=True)
    created_at = serializers.DateTimeField(read_only=True)
    authorID = serializers.CharField(max_length=40)
    json_data = serializers.JSONField()

    def create(self, validated_data):
        #print(validated_data)
        pdf_file = validated_data.pop('pdf_file')
        authorID = validated_data.pop('authorID')
        json_data = validated_data.pop('json_data')

        request_data = self.context['request'].data
        file_name = request_data.get('file_name')

        # create history item instance
        history_item = HistoryItem.objects.create(
            file_name=file_name,
            pdf_file = pdf_file,
            created_at=datetime.datetime.now(),
            authorID=authorID,
            json_data=json_data
        )

        return history_item
    
    class Meta:
        model = HistoryItem
        fields = ('id', 'file_name', 'json_data', 'created_at', 'authorID', 'pdf_file')

