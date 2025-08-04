from django.contrib import admin
from .models import Consultation, FollowUp, Prescription, TestReport

# Register your models here.
admin.site.register(Consultation)
admin.site.register(FollowUp)
admin.site.register(Prescription)
admin.site.register(TestReport)