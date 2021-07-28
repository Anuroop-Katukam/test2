from rest_framework import serializers
from .models import *

class fileSerializer(serializers.ModelSerializer):
    class Meta:
        model = file
        fields = '__all__'


class SimpleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Simple
        fields = '__all__'
