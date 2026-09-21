from rest_framework import serializers
from .models import Enrollment


class EnrollmentSerializer(serializers.ModelSerializer):
    student_name = serializers.CharField(source="student.name", read_only=True)
    student_id_code = serializers.CharField(source="student.student_id", read_only=True)
    class_batch_name = serializers.CharField(source="class_batch.name", read_only=True)

    class Meta:
        model = Enrollment
        fields = [
            "id",
            "student",
            "student_name",
            "student_id_code",
            "class_batch",
            "class_batch_name",
            "enrollment_date",
            "agreed_fees",
            "is_active",
            "notes",
        ]
        read_only_fields = ["id", "enrollment_date"]

    def validate(self, attrs):
        student = attrs.get("student")
        class_batch = attrs.get("class_batch")

        if self.instance is None and student and class_batch:
            if Enrollment.objects.filter(student=student, class_batch=class_batch).exists():
                raise serializers.ValidationError(
                    {"detail": "This student is already enrolled in this class batch."}
                )
        return attrs