from rest_framework import serializers
from .models import Doctor

class CreateDoctroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        exclude = ('user',)
        