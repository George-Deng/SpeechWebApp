  
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager


class CustomUser(AbstractBaseUser, PermissionsMixin):
    USER_TYPE_CHOICES = (
      (1, 'patient'),
      (2, 'doctor')
  )
    email = models.EmailField(_('email address'), unique=True)
    user_type = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['user_type']

    objects = CustomUserManager()

    def __str__(self):
        return self.email

class Doctor(models.Model):
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  name = models.CharField(max_length=100, blank=True, null=True)

  license_number = models.CharField(max_length=200, null=True)
  clinic_name = models.CharField(max_length=200, null=True)
  
  def __str__(self):
    if self.name == None:
      return self.user.email
    return self.name +":" +self.user.email

class Patient(models.Model):
  user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
  name = models.CharField(max_length=100, blank=True, null=True)
  doctor = models.ForeignKey(Doctor, on_delete=models.DO_NOTHING, related_name="patients")
  def __str__(self):
    if self.name == None:
      return self.user.email
    return self.name +":" +self.user.email
  
