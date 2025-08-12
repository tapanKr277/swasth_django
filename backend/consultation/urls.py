from django.urls import path
from .views import ConsultationView

urlpatterns = [
    path('get-patient/<str:id>/', ConsultationView.as_view(), name='get-patient-consultations'),
    path('create-consultation/', ConsultationView.as_view(), name='get-patient-consultations'),
]