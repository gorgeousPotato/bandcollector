from django.db import models
from django.urls import reverse
from datetime import date

TYPES = (
  ('A', 'Album'),
  ('S', 'Single')
)

class Band(models.Model):
  name=models.CharField(max_length=100)
  city=models.CharField(max_length=100)
  country=models.CharField(max_length=100)
  formed_in=models.IntegerField()

  def __str__(self):
    return f"{self.name} ({self.id})"
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'band_id': self.id})
  
  def lot_of_albums(self):
    return self.album_set >= 3

class Album(models.Model):
  type = models.CharField(
    max_length=1,
    choices=TYPES,
    default=TYPES[0][0]
    )
  name = models.CharField(max_length=100)
  date = models.DateField('release date')

  band = models.ForeignKey(Band, on_delete=models.CASCADE)

  def __str__(self):
    return f"{self.get_type_display()} {self.name} on {self.date}"
  
  class Meta:
    ordering = ['-date']