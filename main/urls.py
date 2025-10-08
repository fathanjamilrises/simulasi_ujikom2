from django.urls import path
from . import views

urlpatterns = [
    path('', views.beranda, name='beranda'),
    path('profil/', views.profil, name='profil'),
    path('kontak/', views.kontak, name='kontak'),
    path('ekstrakulikuler/', views.esktrakulikuler, name='ekstrakulikuler'),
    path('berita/', views.berita, name='berita'),
    path('galeri/', views.galeri, name='galeri'),
    path('berita/<int:id>', views.berita_detail, name='berita_detail'),
    path('jurusan/<int:id>', views.jurusan_detail, name='jurusan_detail'),
]