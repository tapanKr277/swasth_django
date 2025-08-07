from django.db import models
import uuid
from django.utils import timezone

# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Doctor(BaseModel):
    user = models.OneToOneField('custom_user.CustomUser', on_delete=models.CASCADE, related_name='doctor')
    specialization = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    license_number = models.CharField(max_length=50)
    year_of_experience = models.PositiveIntegerField()
    hospital_name = models.CharField(max_length=200)
    available_timings = models.CharField(max_length=200)

    def __str__(self):
        return self.specialization

    class Meta:
        db_table = 'doctor'
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"

class DoctorPatient(BaseModel):
    doctor = models.ForeignKey("doctor", on_delete=models.CASCADE, related_name='doctors_patients')
    patient = models.ForeignKey("patient.patient", on_delete=models.CASCADE, related_name='doctors_patients')

    def __str__(self):
        return self.doctor.user.first_name + " " + self.patient.user.first_name