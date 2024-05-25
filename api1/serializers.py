from dataclasses import field
from pyexpat import model
from rest_framework import serializers, viewsets
from geomatics.models import *
from accounts.models import *
from django.contrib.auth import get_user_model



#account serializers
CustomUser = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'first_name', 'last_name', 'course', 'validity', 'payment_detail']

class UserUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['first_name', 'last_name', 'course', 'validity', 'payment_detail']