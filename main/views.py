from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Berita
from .models import Jurusan
from .models import Galeri
from .models import Eskul
from .models import Pesan

# Create your views here.
def beranda (request):
    berita_terbaru = Berita.objects.all().order_by('-published_date')[:3]
    galeri_terbaru = Galeri.objects.all().order_by('-id')[:4]
    jurusan = Jurusan.objects.all()
    informasi_statistik = [
        {'label': 'Siswa', 'value': 1492},
        {'label': 'Guru Profesional', 'value': 90},
        {'label': 'Program Keahlian', 'value':5},
    ]
    keunggulan = [
        {'title' : 'Guru Profesional', 'description': 'Dibimbing oleh tenaga pendidik profesional dan berpengalaman.', 'icon': 'bi bi-person-workspace'},
        {'title' : 'Prestasi Akademik & Non-Akademik', 'description': 'Siswa menorehkan prestasi di tingkat kota hingga nasional.', 'icon': 'bi bi-award'},
        {'title' : 'Lingkungan Belajar Positif', 'description': 'Menjunjung tinggi disiplin, toleransi, dan kerja sama.', 'icon': 'bi bi-people'},
        {'title' : 'Fasilitas Lengkap & Modern', 'description': 'Ruang kelas nyaman, lab, perpustakaan digital, serta area olahraga mendukung..', 'icon': 'bi bi-laptop'},
    ]
    return render (request, 'pages/beranda.html', {'berita_terbaru': berita_terbaru, 'informasi_statistik': informasi_statistik, 'keunggulan': keunggulan, 'jurusan': jurusan, 'galeri_terbaru': galeri_terbaru})

def profil (request):
    misi = [
        "Menyelenggarakan pendidikan menengah kejuruan yang berkualitas untuk menghasilkan lulusan yang kompeten di bidangnya.",
        "Membentuk karakter siswa yang disiplin, jujur, bertanggung jawab, dan berakhlak mulia.",
        "Mengembangkan potensi siswa melalui kegiatan ekstrakurikuler yang beragam.",
    ]
    informasi_sekolah =[
        {'label' : 'Nama Sekolah' , 'value': 'SMK Negeri 4 Tasikmalaya'},
        {'label' : 'NPSN' , 'value': '20279663'},
        {'label' : 'Nomor Statistik Sekolah' , 'value': '401327810004'},
        {'label' : 'Jalan' , 'value': '	Jl. Depok RT 02 RW 05'},
        {'label' : 'Kelurahan' , 'value': 'Sukamenak'},
        {'label' : 'Kecamatan' , 'value': 'Purbaratu'},
        {'label' : 'Kota' , 'value': 'Tasikmalaya'},
    ]
    return render (request, 'pages/profil.html', {'misi': misi, 'informasi_sekolah': informasi_sekolah})

def esktrakulikuler (request):
    eskul = Eskul.objects.all()
    return render (request, 'pages/ekstrakulikuler.html', {'eskul': eskul})

def kontak (request):
    if request.method == 'POST':
        nama = request.POST.get('nama', '').strip()
        email = request.POST.get('email', '').strip()
        subjek = request.POST.get('subjek', '').strip()
        pesan_text = request.POST.get('pesan', '').strip()

        if not nama or not email or not pesan_text:
            messages.error(request, 'Nama, email, dan pesan wajib diisi.')
            return render(request, 'pages/kontak.html', {'nama': nama, 'email': email, 'subjek': subjek, 'pesan': pesan_text})

        Pesan.objects.create(nama=nama, email=email, subjek=subjek, pesan=pesan_text)
        messages.success(request, 'Pesan berhasil dikirim. Hatur Nuhun!')
        return redirect('kontak')

    return render (request, 'pages/kontak.html')


def berita (request):
    berita = Berita.objects.all()
    return render (request, 'pages/berita.html', {'berita': berita})

def galeri (request):
    galeri = Galeri.objects.all()
    return render (request, 'pages/galeri.html', {'galeri': galeri})

def berita_detail (request, id):
    berita = Berita.objects.get(id=id)
    return render (request, 'pages/berita_detail.html', {'berita': berita})

def jurusan_detail (request, id):
    jurusan = Jurusan.objects.get(id=id)
    return render (request, 'pages/jurusan_detail.html', {'jurusan': jurusan})

