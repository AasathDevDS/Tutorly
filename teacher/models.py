from django.db import models

# Create your models here.
class Teacher(models.Model):
  name = models.CharField(max_length=64)
  phone = models.PositiveIntegerField()
  whatsapp_number = models.PositiveIntegerField(blank=True , null=True)

  def __str__(self):
      return self.name
  
