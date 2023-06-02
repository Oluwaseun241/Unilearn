from django.db import models
from shortuuid.django_fields import ShortUUIDField
from accounts.model import Instructor 
# Create your models here.

class Course(models.Model):
    id = ShortUUIDField(primary_key=True)
    instructor_id = models.ForeignKey(Instructor, on_delete=models.CASCADE, related_name='instructor_id')
    course_code = models.CharField
    category
    price
    created_at
    updated_at

class Material(models.Model):
    id = ShortUUIDField(primary_key=True)
    title
    description
    course_id
    file
    created_at
