from batch.models import ClassBatch
from django.db import models
from student.models import Student


class Enrollment(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="enrollments"
    )
    class_batch = models.ForeignKey(
        ClassBatch, on_delete=models.CASCADE, related_name="enrollments"
    )
    enrollment_date = models.DateTimeField(auto_now_add=True)
    agreed_fees = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        null=True,
        blank=True,
        help_text="Custom fee for this student. If its Blank take the value of Subject fee from Batch Default Fee",
    )
    is_active = models.BooleanField(
        default=True
    ) 
    notes = models.TextField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["student", "class_batch"],
                name="unique_student_class_enrollment",
            )
        ]

    def save(self, *args, **kwargs):
        # Specific discount fee illana batch default fee edukka
        if self.agreed_fees is None and self.class_batch:
            self.agreed_fees = self.class_batch.default_fee
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.student.name} - {self.class_batch.id}"