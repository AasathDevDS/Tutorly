from rest_framework import viewsets
from .models import ClassBatch
from .serializers import ClassBatchSerializer

# Create your views here.
class ClassBatchViewSet(viewsets.ModelViewSet):
    queryset = ClassBatch.objects.all()
    serializer_class = ClassBatchSerializer 
