from django.db import models
from django.urls import reverse

class Band(models.Model):
  name=models.CharField(max_length=100)
  city=models.CharField(max_length=100)
  country=models.CharField(max_length=100)
  formed_in=models.IntegerField()

  def __str__(self):
    return f"{self.name} ({self.id})"
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'band_id': self.id})

