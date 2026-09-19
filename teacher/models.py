from django.db import models
from django.utils import timezone

class Teacher(models.Model):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=15)
    whatsapp_number = models.CharField(max_length=15, blank=True, null=True)
    salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    is_active = models.BooleanField(default=True)
    joined_at = models.DateField(default=timezone.now)

    def save(self, *args, **kwargs):
        # Whatsapp number fill pannalana, phone number-ah default-ah set pannum
        if not self.whatsapp_number:
            self.whatsapp_number = self.phone
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name