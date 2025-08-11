from rest_framework import serializers
from .models import Doctor
from custom_user.models import CustomUser

class CreateDoctroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        exclude = ('user',)

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        exclude = ('password', 'is_active', 'is_staff', 'groups', 'user_permissions')
        
class ListAllDoctorSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Doctor
        fields = '__all__'
