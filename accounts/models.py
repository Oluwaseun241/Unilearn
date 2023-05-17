# Django Import
from shortuuid.django_fields import ShortUUIDField
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

# Own import
import uuid
from django.conf import settings

class UserManager(BaseUserManager):

   def create_user(self, email, password=None, **extra_fields):
      if not email:
         raise ValueError('The Email Field must be set')
      email = self.normalize_email(email)
      user = self.model(email=email, **extra_fields)
      user.set_password(password)
      user.save()
      return user

   def create_superuser(self, email, password=None, **extra_fields):
      extra_fields.setdefault('is_staff', True)
      extra_fields.setdefault('is_superuser', True)
      return self.create_user(email, password, **extra_fields)

class User(AbstractUser):
   id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
   username = None
   email = models.EmailField(unique=True)
   password = models.CharField(max_length=120)
   name = models.CharField(max_length=255)
   created_at = models.DateTimeField(auto_now_add=True)
   is_instructor = models.BooleanField(default=False)
   # is_staff = models.BooleanField(default=False)
   # is_superuser = models.BooleanField(default=False)

   objects = UserManager()

   USERNAME_FIELD = 'email'
   REQUIRED_FIELDS = ['name']

   def __str__(self):
      return self.email

class Instructor(models.Model):
   id = ShortUUIDField(primary_key=True, length=6, max_length=6, editable=False)
   user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='instructor')
   bio = models.CharField(max_length=250)
   contact_info = models.CharField(max_length=250)
   profile_picture = models.ImageField(upload_to='Unilearn\profile_pictures', null=True)

   def __str__(self):
      return self.user.email

class Student(models.Model):
   id = ShortUUIDField(primary_key=True, length=6, max_length=6, editable=False)
   user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='student')
   matric_no = models.IntegerField()

   def __str__(self):
      return self.user.email