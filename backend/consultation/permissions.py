from rest_framework.permissions import BasePermission

class IsDoctorOrPatientGrpoupUser(BasePermission):
    def has_object_permission(self, request, view, obj):
        return (request.user and request.user.is_authenticated and request.user.groups.filter(name__in = ["Doctor", "Patient"]).exists())