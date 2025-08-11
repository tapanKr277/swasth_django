from datetime import date
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.models import Group, Permission

def calculate_age(dob: date) -> int:
    today = date.today()
    age = today.year - dob.year - ((today.month, today.day) < (dob.month, dob.day))
    return age

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("Email must be set")
        dob = extra_fields.get("dob")
        if dob:
            today = date.today()
            extra_fields["age"] = today.year - dob.year - (
                (today.month, today.day) < (dob.month, dob.day)
            )
        else:
            extra_fields["age"] = None
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)
        created_user = self.create_user(email, password, **extra_fields)
        try:
            group = Group.objects.get(name="Admin") 
        except:
            group = Group.objects.create(name="Admin")
            all_permissions = Permission.objects.all()
            group.permissions.set(all_permissions) 
            group.save()
        created_user.groups.add(group)
        return created_user