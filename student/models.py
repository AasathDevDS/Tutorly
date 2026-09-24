import datetime
from django.db import models
from django.utils import timezone

def get_default_dob():
    return timezone.now().date() - datetime.timedelta(days=365 * 10)

class Student(models.Model):
    class Gender(models.TextChoices):
        BOY = 'Boy', 'Boy'
        GIRL = 'Girl', 'Girl'
        
    student_id = models.CharField(max_length=10, unique=True)
    name = models.CharField(max_length=128)
    gender = models.CharField(max_length=4, choices=Gender.choices , default = 'BOY')
    
    # Neenga yositha maari default function-ai inga use pannalam
    dob = models.DateField(null=True, blank=True, default=get_default_dob)
    
    parent_name = models.CharField(max_length=128)
    # length 15 irunthaal "+94 77 123 4567" endru spaces irunthalum problem illai
    parent_phone = models.CharField(max_length=15) 
    whatsapp_number = models.CharField(max_length=15, blank=True)
    
    is_active = models.BooleanField(default=True)
    registered_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        # whatsapp_number empty string ("") aaga irunthalum intha condition true aagum
        if not self.whatsapp_number:
            self.whatsapp_number = self.parent_phone
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} ({self.student_id})"