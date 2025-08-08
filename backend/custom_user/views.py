from rest_framework.views import APIView
from .serializers import CreateDoctroSerializer, CreatePatientSerializer, CreateDoctorSerializer
from patient.serializers import ListAllPatientSerializer
from rest_framework import status
from rest_framework.response import Response
from patient.models import Patient
from django.contrib.auth.models import Group, Permission

class CreatePatientUserView(APIView):
    def post(self, request):
        serialized_data = CreatePatientSerializer(data=request.data, many=False)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        
class ListAllPatientView(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serialized_data = ListAllPatientSerializer(patients, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

class CreateDoctorUserView(APIView):
    def post(self, request):
        doctor_data = request.data
        serialized_data = CreateDoctorSerializer(data=doctor_data, many=False)
        if serialized_data.is_valid():
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)