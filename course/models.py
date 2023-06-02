from django.db import models
from shortuuid.django_fields import ShortUUIDField
# Create your models here.

class Course(models.Model):
    id = ShortUUIDField(primary_key=True)
    instructor_id
    course_code
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
