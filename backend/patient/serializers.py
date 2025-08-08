from rest_framework import serializers
from .models import Patient
from custom_user.models import CustomUser
# from custom_user.serializers import UserSerializer


from django.contrib.auth.models import Group, Permission

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'codename', 'name']

class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)
    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']

class UserSerializer(serializers.ModelSerializer):
    # groups = GroupSerializer(many=True)
    # all_permissions = PermissionSerializer()

    class Meta:
        model = CustomUser
        exclude = ('password', 'is_active', 'is_staff', 'groups', 'user_permissions')

    # def get_permissions(self, obj):
    #     return list(obj.get_all_permissions())
    
class CreatePatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        exclude = ('user',)
    
class ListAllPatientSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    class Meta:
        model = Patient
        fields = '__all__' 