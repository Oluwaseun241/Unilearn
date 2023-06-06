from django.db import models
from shortuuid.django_fields import ShortUUIDField
from accounts.models import Instructor, Student 
# Create your models here.

class Course(models.Model):
    id = ShortUUIDField(primary_key=True)
    instructor = models.ForeignKey(Instructor, on_delete=models.CASCADE)
    course_code = models.CharField(max_length=20)
    category = models.CharField(max_length=30)
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Material(models.Model):
    id = ShortUUIDField(primary_key=True)
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=150)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='materials')
    file = models.FileField(upload_to=None)
    created_at = models.DateTimeField(auto_now_add=True)

class Enrollment(models.Model):
    id = ShortUUIDField(primary_key=True)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
