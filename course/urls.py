from django.urls import path
from .views import (
    CourseListView,
    CourseDetailView,
    MaterialCreateView,
    MaterialDetailView,
    EnrollmentCreateView,
)

urlpatterns = [
    path("courses/", CourseListView.as_view(), name='course_list'),   
    path("courses/<str:pk>/", CourseDetailView.as_view(), name='course_detail'),
    path("courses/<str:course_pk>/materials/<str:pk>/", MaterialDetailView.as_view(), name='course_detail'),
    path("courses/<str:course_pk>/enrollments/", EnrollmentCreateView.as_view(), name='course_list'),
]
