from rest_framework import serializers
from doctor.serializers import CreateDoctroSerializer
from patient.serializers import CreatePatientSerializer
from .models import CustomUser
from patient.models import Patient
from django.contrib.auth.models import Group, Permission
from doctor.models import Doctor
from .utils import calculate_age

class PermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Permission
        fields = ['id', 'codename', 'name']

class GroupSerializer(serializers.ModelSerializer):
    permissions = PermissionSerializer(many=True)
    class Meta:
        model = Group
        fields = ['id', 'name', 'permissions']

class CreatePatientSerializer(serializers.ModelSerializer):
    patient = CreatePatientSerializer()
    password = serializers.CharField(write_only=True)
    age = serializers.CharField(read_only=True)
    class Meta:
        model = CustomUser
        exclude = ('is_active', 'is_staff','groups', 'user_permissions', 'is_superuser')
    
    def create(self, validated_data):
        patient_data = validated_data.pop('patient')
        validated_data['age'] = calculate_age(validated_data['dob'])
        user = CustomUser.objects.create_user(**validated_data)
        group = Group.objects.get(name="Patient")
        user.groups.add(group)
        Patient.objects.create(user=user, **patient_data)
        return user

class CreateDoctorSerializer(serializers.ModelSerializer):
    doctor = CreateDoctroSerializer()
    password = serializers.CharField(write_only=True)
    age = serializers.CharField(read_only=True)
    class Meta:
        model = CustomUser
        exclude = ('is_active', 'is_staff', 'groups', 'user_permissions', 'is_superuser')
    
    def create(self, validated_data):
        doctor_data = validated_data.pop('doctor')
        validated_data['age'] = calculate_age(validated_data['dob'])
        user = CustomUser.objects.create_user(**validated_data)
        group = Group.objects.get(name="Doctor")
        user.groups.add(group)
        Doctor.objects.create(user=user, **doctor_data)
        return user

class UserSerializer(serializers.ModelSerializer):
    groups = GroupSerializer(many=True)
    all_permissions = serializers.SerializerMethodField()
    class Meta:
        model = CustomUser
        exclude = ('password',)
    def get_permissions(self, obj):
        return list(obj.get_all_permissions())
