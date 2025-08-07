from django.db import models
from doctor.models import BaseModel
# Create your models here.
class Consultation(BaseModel):
    patient = models.ForeignKey('patient.Patient', on_delete=models.CASCADE, related_name="consultations")
    doctor = models.ForeignKey('doctor.Doctor', on_delete=models.CASCADE, related_name="consultations")
    visitReason = models.CharField(max_length=200)
    diagnosis = models.CharField(max_length=200)
    notes = models.CharField(max_length=500)
    visit_date_and_time = models.DateTimeField(auto_now_add=True)
    is_follow_u_required = models.BooleanField(default=False)
    
    def __str__(self):
        return self.patient.patient_code

    class Meta:
        db_table = 'consultation'
        verbose_name = 'Consultation'
        verbose_name_plural  = 'Consultations'

class FollowUp(BaseModel):
    class Status(models.TextChoices):
        UPCOMING = 'upcoming', 'Upcoming'

    consultation = models.OneToOneField('Consultation', on_delete=models.CASCADE)
    scheduled_date = models.DateField()
    scheduledTime = models.TimeField()
    status = models.CharField(choices=Status.choices)
    notes = models.TextField(max_length=500)

    def __str__(self):
        return self.consultation.patient.patient_code

    class Meta:
        db_table = 'follow_up'
        verbose_name = 'FollowUp'
        verbose_name_plural  = 'FollowUps'

class Prescription(BaseModel):
    consultation = models.ForeignKey('Consultation', on_delete=models.CASCADE, related_name="prescriptions")
    medicineName = models.CharField(max_length=100)
    dosage = models.CharField(max_length=500)
    duration = models.CharField(max_length=500)
    instructions = models.TextField(max_length=500)

    def __str__(self):
        return self.medicineName

    class Meta:
        db_table = 'prescription'
        verbose_name = 'Prescription'
        verbose_name_plural  = 'Prescriptions'
        

class TestReport(BaseModel):
    consultation = models.ForeignKey('Consultation', on_delete=models.CASCADE, related_name="test_reports")
    testType = models.CharField(max_length=200)
    resultSummary = models.TextField(max_length=500)
    reportFileUrl = models.FileField(upload_to="reports/")
    testDate = models.DateField()
    testTime = models.TimeField()

    def __str__(self):
        return self.consultation.patient.patient_code

    class Meta:
        db_table = 'test_reports'
        verbose_name = 'Test Report'
        verbose_name_plural = 'Test Reports'