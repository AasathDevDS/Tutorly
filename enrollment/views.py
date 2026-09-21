from rest_framework import viewsets, filters
from .models import Enrollment
from .serializers import EnrollmentSerializer


class EnrollmentViewSet(viewsets.ModelViewSet):
    queryset = Enrollment.objects.select_related("student", "class_batch").all()
    serializer_class = EnrollmentSerializer