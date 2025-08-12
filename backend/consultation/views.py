from django.shortcuts import render
from rest_framework.views import APIView
from .permissions import IsDoctorOrPatientGrpoupUser
from .models import Consultation
from patient.models import Patient
from .serializers import ConsultationSerializer, CreateConsultationSerializer
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ConsultationView(APIView):
    # permission_classes = [IsDoctorOrPatientGrpoupUser]
    def get(self, request, id):
        consultations = Consultation.objects.filter(patient=id)
        serialized_data = ConsultationSerializer(consultations, many=True)
        return Response(serialized_data.data, status=status.HTTP_200_OK)

    def post(self, request):
        serialized_data = CreateConsultationSerializer(data=request.data, many=False)
        if(serialized_data.is_valid()):
            serialized_data.save()
            return Response(serialized_data.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized_data.errors, status=status.HTTP_400_BAD_REQUEST)