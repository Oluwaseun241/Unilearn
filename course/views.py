# Django imports
from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated

# Own imports
from .models import Course, Material, Enrollment
from .serializers import (
    CourseSerializer,
    MaterialSerializer,
    EnrollmentSerializer,
)

class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class CourseDetailView(generics.RetrieveAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

class MaterialCreateView(generics.CreateAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class MaterialDetailView(generics.RetrieveAPIView):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer

class EnrollmentCreateView(generics.CreateAPIView):
    queryset = Enrollment.objects.all()
    serializer_class = EnrollmentSerializer

    def perform_create(self, serializer):
        serializer.save(course_id=self.kwargs['course_pk'], user_id=self.request.user_id)
