from django.contrib import admin
from .models import Band, Album, Genre
# Register your models here.
admin.site.register(Band)
admin.site.register(Album)
admin.site.register(Genre)