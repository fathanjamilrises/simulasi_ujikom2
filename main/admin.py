from django.contrib import admin
from .models import Berita
from .models import Jurusan
from .models import Galeri
from .models import Eskul

# Register your models here.
admin.site.register(Berita)
admin.site.register(Jurusan)
admin.site.register(Galeri) 
admin.site.register(Eskul)