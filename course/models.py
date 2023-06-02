from django.db import models

# Create your models here.

class Course(models.Model):
    id
    instructor_id
    course_code
    category
    price
    created_at
    updated_at

class Material(models.Model):
    id
    title
    description
    course_id
    file
    created_at
