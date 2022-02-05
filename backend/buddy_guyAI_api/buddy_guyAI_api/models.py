from django.db import models

# Create your models here.



# from django.db import models
# from django.contrib.auth.models import User
# from django.contrib.auth.models import(
#     BaseUserManager, AbstractBaseUser
# )
# class Doctor(BaseUserManager): 
#     #user is onetomany fields? licesnse number to patient name?
#     user = models.OneToOneField(User,on_delete = models.CASCADE, null=True,blank = True)
#     name = models.CharField(max_length = 200, null= True)
#     email = models.CharField(max_length= 200, null=True)
#     #phone number could be stored by pip install django-phonenumber-field, char field for now
#     phone_number = models.CharField(max_length= 200, null=True)
#     #license number format:  e.g. CAMD-9999-9999
#     license_number = models.CharField(max_length=200, null=True)
#     clinic_name = models.CharField(max_length=200, null=True)

#     def __str__(self):
#         return self.name

#     def create_user(self, email, password=None):
#         if not email:
#             raise ValueError('Users must have an email address')

#         user = self.model(
#             email=self.normalize_email(email),
#         )

#         user.set_password(password)
#         user.save(using=self._db)
#         return user

#     def create_staffuser(self, email, password):
#         """
#         Creates and saves a staff user with the given email and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         user.staff = True
#         user.save(using=self._db)
#         return user

#     def create_superuser(self, email, password):
#         """
#         Creates and saves a superuser with the given email and password.
#         """
#         user = self.create_user(
#             email,
#             password=password,
#         )
#         user.staff = True
#         user.admin = True
#         user.save(using=self._db)
#         return user

# #patient?
# class Patient(models.Model):
#     user = models.OneToOneField(User,on_delete = models.CASCADE, null=True,blank = True)
#     name = models.CharField(max_length = 200, null= True)
#     email = models.CharField(max_length= 200, null=True)
#     #phone number could be stored by pip install django-phonenumber-field, char field for now
#     phone_number = models.CharField(max_length= 200, null=True)
#     #diagnosis is a char? could be true/false
#     diagnosis = models.CharField(max_length=200, null=True)
#     #for the doctor to have many patients
#     doctor = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null = True, blank = True)
#     #could add address
#     #address = models.CharField(max_length= 200, null=True)

#     def __str__(self):
#         return self.name


