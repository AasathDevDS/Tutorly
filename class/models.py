from django.db import models
from grade.models import Grade
from subject.models import Subject
from teacher.models import Teacher

class ClassBatch(models.Model):
    # Foreign Keys
    grade = models.ForeignKey(
        Grade, on_delete=models.CASCADE, related_name="classes"
    )
    subject = models.ForeignKey(
        Subject, on_delete=models.CASCADE, related_name="classes"
    )
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="classes"
    )

    # Fees configuration
    default_fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        help_text="Default monthly fee for this class (e.g. 2500.00)",
    )

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Class / Batch"
        verbose_name_plural = "Classes / Batches"

    def __str__(self):
        return f"{self.name} - {self.grade}"