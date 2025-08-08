from django.urls import path
from .views import CreatePatientUserView, CreateDoctorUserView, ListAllPatientView

urlpatterns = [
    path('create/patient/', CreatePatientUserView.as_view(), name='create-patient'),
    path('create/doctor/', CreateDoctorUserView.as_view(), name='create-doctor'),
    path('get-all-patient-list/', ListAllPatientView.as_view(), name='list-all-patient-list'),
]
