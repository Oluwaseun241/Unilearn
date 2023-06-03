from django.db import models
from shortuuid.django_fields import ShortUUIDField
from accounts.models import Instructor 
# Create your models here.

class Course(models.Model):
    id = ShortUUIDField(primary_key=True)
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='instructor_id')
    course_code = models.CharField(max_length=20)
    category = models.CharField(max_length=30)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)

class Material(models.Model):
    id = ShortUUIDField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    course_id = models.ForeignKey(Course, on_delete=models.CASCADE,  related_name='course_id')
    file = models.FileField(upload_to=None)
    created_at = models.DateTimeField(auto_now_add=True)
