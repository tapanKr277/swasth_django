from django.db import models
from doctor.models import BaseModel

# Create your models here.
class Patient(BaseModel):
    class Gender(models.TextChoices):
        MALE = 'male', 'Male'
        FEMALE = 'female', 'Female'

    patient_code = models.CharField(max_length=8)
    gender = models.CharField(max_length=10, choices=Gender.choices)
    emergency_contact_name = models.CharField(max_length=20)
    emergency_contact_number = models.CharField(max_length=10)
    known_allergies = models.TextField()
    existing_conditions = models.TextField()
    insurance_provider = models.CharField(max_length=100)
    insurance_policy_number = models.CharField(max_length=20)
    blood_group = models.CharField(max_length=10)

    def __str__(self):
        return self.patient_code

    
    class Meta:
        db_table = 'patient'
        verbose_name = "Patient"
        verbose_name_plural = "Patients"