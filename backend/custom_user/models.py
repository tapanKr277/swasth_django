from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models
from django.utils import timezone
from doctor.models import BaseModel
from datetime import date

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
        return self.create_user(email, password, **extra_fields)

class CustomUser(BaseModel,AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=10, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    dob = models.DateField()
    blood_group = models.CharField(max_length=10)
    phone_number = models.CharField(max_length=10, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    objects = CustomUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name', 'last_name', 'dob', 'blood_group', 'phone_number']

    def __str__(self):
        return self.email
    
    class Meta:
        db_table = 'custom_user'
        verbose_name = 'Custom User'
        verbose_name_plural = 'Custom Users'