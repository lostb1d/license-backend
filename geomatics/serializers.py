from dataclasses import field
from pyexpat import model
from rest_framework import serializers, viewsets
from .models import *


class questionSerializers(serializers.ModelSerializer):
    class Meta:
        model = questions
        fields = '__all__'

class correctOptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = correctOption
        fields = '__all__'

