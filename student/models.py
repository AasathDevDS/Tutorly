import datetime
from django.db import models
from django.utils import timezone


def get_default_dob():
    return timezone.now().date() - datetime.timedelta(days=365 * 10)


class Student(models.Model):
    student_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=128)
    dob = models.DateField(
        null=True, blank=True
    )  # illana default=get_default_dob
    parent_name = models.CharField(max_length=128)
    parent_phone = models.CharField(
        max_length=12
    )  # Siblings-kaaga unique thevai illa
    whatsapp_number = models.CharField(max_length=12, blank=True)
    is_active = models.BooleanField(default=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # WhatsAPP number illai enraal parent_phone-ah default-aa vaikkom
        if not self.whatsapp_number:
            self.whatsapp_number = self.parent_phone
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.student_id})"