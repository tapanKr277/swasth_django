from django.db import models
import uuid

# Create your models here.
class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Doctor(BaseModel):
    specialization = models.CharField(max_length=30)
    phone_number = models.CharField(max_length=10)
    license_number = models.CharField(max_length=50)
    year_of_experience = models.PositiveIntegerField()
    hospital_name = models.CharField(max_length=200)
    available_timings = models.CharField(max_length=200)

    def __str__(self):
        return self.specialization

    class Meta:
        verbose_name = "doctor"
        verbose_name_plural = "doctors"
