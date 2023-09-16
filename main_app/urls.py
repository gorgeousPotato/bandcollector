from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('bands/', views.bands_index, name='index'),
  path('bands/<int:band_id>', views.bands_detail, name='detail'),
  path('bands/create/', views.BandCreate.as_view(), name='bands_create'),
  path('bands/<int:pk>/update/', views.BandUpdate.as_view(), name='bands_update'),
  path('bands/<int:pk>/delete/', views.BandDelete.as_view(), name='bands_delete'),
  path('bands/<int:band_id>/add_album/', views.add_album, name='add_album'),
  path('bands/<int:band_id>/assoc_genre/<int:genre_id>', views.assoc_genre, name='assoc_genre'),
  path('bands/<int:band_id>/unassoc_genre/<int:genre_id>', views.unassoc_genre, name='unassoc_genre'),
  path('genres/create/', views.GenreCreate.as_view(), name='genres_create'),
  path('genres/', views.GenreList.as_view(), name='genres_index'),
  path('genres/<int:pk>/', views.GenreDetail.as_view(), name='genres_detail'),
  path('genres/<int:pk>/update/', views.GenreUpdate.as_view(), name='genres_update'),
  path('genres/<int:pk>/delete/', views.GenreDelete.as_view(), name='genres_delete'),
]
