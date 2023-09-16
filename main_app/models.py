from django.db import models
from django.urls import reverse
from datetime import date

TYPES = (
  ('A', 'Album'),
  ('S', 'Single')
)

class Genre(models.Model):
  name=models.CharField(max_length=50)

  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('genres_detail', kwargs={'pk': self.id})


class Band(models.Model):
  name=models.CharField(max_length=100)
  city=models.CharField(max_length=100)
  country=models.CharField(max_length=100)
  formed_in=models.IntegerField()
  genres = models.ManyToManyField(Genre)

  def __str__(self):
    return f"{self.name} ({self.id})"
  
  def get_absolute_url(self):
    return reverse('detail', kwargs={'band_id': self.id})
  
  def new_albums(self):
    return self.album_set.filter(date__contains='2023').count() >= 1

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