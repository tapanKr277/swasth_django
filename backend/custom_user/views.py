from rest_framework.views import APIView
from .serializers import CreatePatientSerializer, CreateDoctorSerializer
from patient.serializers import ListAllPatientSerializer
from rest_framework import status
from rest_framework.response import Response
from patient.models import Patient
from django.db import transaction

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
    def get(self, request):
        patients = Patient.objects.all()
        serialized_data = ListAllPatientSerializer(patients, many=True)
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