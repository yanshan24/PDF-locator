from rest_framework import serializers
from .models import *
import requests

class RegistrationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['authorID', 'email', 'password', 'is_manager']

    def save(self):
        author = Author(
            email=self.validated_data['email'],
            is_manager=self.validated_data['is_manager'],
        )
        password = self.validated_data['password']
        author.set_password(password)
        author.save()
        return author