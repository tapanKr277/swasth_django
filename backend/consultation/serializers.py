from .models import Consultation, Prescription, TestReport, FollowUp
from rest_framework import serializers
from patient.models import Patient
from doctor.models import Doctor

class ConsultationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultation
        fields = '__all__'

class CreateConsultationSerializer(serializers.ModelSerializer):
    patient_id = serializers.PrimaryKeyRelatedField(
        queryset = Patient.objects.all(), source="patient"
    )
    doctor_id = serializers.PrimaryKeyRelatedField(
        queryset =  Doctor.objects.all(), source="doctor"
    )
    class Meta:
        model = Consultation
        fields = [
            'id', 'patient_id', 'doctor_id', 'visitReason',
            'diagnosis', 'notes', 'is_follow_u_required', 'visit_date_and_time'
        ]
        read_only_fields = ['id', 'visit_date_and_time']
    
    def validate(self, data):
        if data['patient'].user == data['doctor'].user:
            raise serializers.ValidationError("Doctor and patient cannot be the same person.")
        return data
    
class PrescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Prescription
        fields = '__all__'
    
class FollowUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = FollowUp
        fields = '__all__'

class TestReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = TestReport
        fields = '__all__'
        