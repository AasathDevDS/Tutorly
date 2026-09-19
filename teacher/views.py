from rest_framework import viewsets
from .serializers import TeacherSerializer
from .models import Teacher


# Create your views here.
class TeacherViewSet(viewsets.ModelViewSet):
  queryset = Teacher.objects.all()
  serializer_class = TeacherSerializer
  