from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Band, Genre
from .forms import AlbumForm


def home(request):
  return render(request, 'home.html')

def about(request):
  return render(request, 'about.html')

def bands_index(request):
  bands = Band.objects.all()
  return render(request, 'bands/index.html', {
    'bands': bands
  })

def bands_detail(request, band_id):
  band=Band.objects.get(id=band_id)
  id_list = band.genres.all().values_list('id')
  genres_not_listed = Genre.objects.exclude(id__in=id_list)
  album_form = AlbumForm()
  return render(request, 'bands/detail.html', {
    'band': band,
    'album_form': album_form,
    'genres': genres_not_listed
  })

class BandCreate(CreateView):
  model = Band
  fields = ['name', 'city', 'country', 'formed_in']

class BandUpdate(UpdateView):
  model = Band
  fields = ['city', 'country', 'formed_in']

class BandDelete(DeleteView):
  model = Band
  success_url = '/bands'

def add_album(request, band_id):
  form = AlbumForm(request.POST)
  if form.is_valid():
    new_album = form.save(commit=False)
    new_album.band_id = band_id
    new_album.save()
  return redirect('detail', band_id = band_id)

def assoc_genre(request, band_id, genre_id):
  Band.objects.get(id=band_id).genres.add(genre_id)
  return redirect('detail', band_id=band_id)

def unassoc_genre(request, band_id, genre_id):
  genre = Band.objects.get(id=band_id).genres.filter(id=genre_id)
  genre.delete()
  return redirect('detail', band_id=band_id)


class GenreCreate(CreateView):
  model = Genre
  fields = ['name']

class GenreList(ListView):
  model = Genre

class GenreDetail(DetailView):
  model = Genre

class GenreUpdate(UpdateView):
  model = Genre
  fields = ['name']

class GenreDelete(DeleteView):
  model = Genre
  success_url='/genres'