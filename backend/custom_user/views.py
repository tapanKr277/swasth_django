from rest_framework.views import APIView
from .serializers import CreatePatientSerializer, CreateDoctorSerializer
from patient.serializers import ListAllPatientSerializer
from doctor.serializers import ListAllDoctorSerializer
from rest_framework import status
from rest_framework.response import Response
from patient.models import Patient
from django.db import transaction
from doctor.models import Doctor
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication
from .permissions import IsDoctorGrpoupUser

class CreatePatientUserView(APIView):
    @transaction.atomic
    def post(self, request):
        try:
            serialized_data = CreatePatientSerializer(data=request.data, many=False)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(serialized_data.data, status=status.HTTP_201_CREATED)
            else:
                transaction.set_rollback(True)
                return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            transaction.set_rollback(True)
            return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class ListAllPatientView(APIView):
    # permission_classes = [IsDoctorGrpoupUser]
    def get(self, request):
        patients = Patient.objects.all()
        serialized_data = ListAllPatientSerializer(patients, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)
 
class ListAllDoctorView(APIView):
    # permission_classes = [IsAuthenticated, IsAdminUser]
    def get(self, request):
        doctors = Doctor.objects.all()
        serialized_data = ListAllDoctorSerializer(doctors, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

class CreateDoctorUserView(APIView):
    @transaction.atomic
    def post(self, request):
        try:
            doctor_data = request.data
            serialized_data = CreateDoctorSerializer(data=doctor_data, many=False)
            if serialized_data.is_valid():
                serialized_data.save()
                return Response(serialized_data.data, status=status.HTTP_201_CREATED)
            else:
                transaction.set_rollback(True)
                return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            transaction.set_rollback(True)
            return Response(e, status=status.HTTP_500_INTERNAL_SERVER_ERROR)