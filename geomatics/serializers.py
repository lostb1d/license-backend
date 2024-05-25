from dataclasses import field
from pyexpat import model
from rest_framework import serializers, viewsets
from .models import *



#geomatics seriliazers
class questionSerializers(serializers.ModelSerializer):
    class Meta:
        model = geomaticsQuestions
        fields = '__all__'

class correctOptionSerializers(serializers.ModelSerializer):
    class Meta:
        model = correctOption
        fields = '__all__'
