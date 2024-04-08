from django.urls import path
from .views import student_view

urlpatterns = [
    path("students/", student_view)
]