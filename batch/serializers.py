from rest_framework import serializers
from .models import ClassBatch


class ClassBatchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClassBatch
        fields = "__all__"