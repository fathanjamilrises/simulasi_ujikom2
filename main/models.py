from django.db import models

# Create your models here.
class Berita (models.Model):
    title = models.CharField (max_length=200)
    description = models.TextField ()
    author = models.CharField(max_length=100)
    published_date = models.DateTimeField (auto_now_add=True)
    image_url = models.URLField (max_length=200, blank=True)

    def __str__(self):
        return self.title

class Jurusan(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.URLField(max_length=200, blank=True)
    nama_kaprog = models.CharField(max_length=100)
    jumlah_siswa = models.IntegerField(default=0)
    jumlah_guru = models.IntegerField(default=0)

    def __str__(self):
        return self.title


class Galeri(models.Model):
    alt = models.CharField(max_length=100)
    image_url = models.URLField(max_length=200)

    def __str__(self):
        return self.alt

class Eskul(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.URLField(max_length=200, blank=True)

    def __str__(self):
        return self.title


class Pesan(models.Model):
    nama = models.CharField(max_length=100)
    email = models.EmailField()
    subjek = models.CharField(max_length=200, blank=True)
    pesan = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nama
