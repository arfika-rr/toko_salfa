from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Kategori, Produk

@login_required
def list_produk(request):
    produk = Produk.objects.select_related('kategori').order_by('nama')
    kategori = Kategori.objects.all()
    
    # Filter
    kat = request.GET.get('kategori')
    cari = request.GET.get('cari')
    if kat:
        produk = produk.filter(kategori_id=kat)
    if cari:
        produk = produk.filter(nama__icontains=cari)
    
    return render(request, 'produk/list.html', {
        'produk': produk,
        'kategori': kategori,
        'kat_aktif': kat,
        'cari': cari,
    })

@login_required
def tambah_produk(request):
    kategori = Kategori.objects.all()
    if request.method == 'POST':
        Produk.objects.create(
            nama=request.POST['nama'],
            kategori_id=request.POST.get('kategori') or None,
            barcode=request.POST.get('barcode') or None,
            harga_jual=request.POST['harga_jual'],
            harga_beli=request.POST['harga_beli'],
            stok=request.POST['stok'],
            stok_minimum=request.POST['stok_minimum'],
            satuan=request.POST['satuan'],
        )
        messages.success(request, 'Produk berhasil ditambahkan.')
        return redirect('produk:list')
    return render(request, 'produk/form.html', {'kategori': kategori, 'action': 'Tambah'})

@login_required
def edit_produk(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    kategori = Kategori.objects.all()
    if request.method == 'POST':
        produk.nama = request.POST['nama']
        produk.kategori_id = request.POST.get('kategori') or None
        produk.barcode = request.POST.get('barcode') or None
        produk.harga_jual = request.POST['harga_jual']
        produk.harga_beli = request.POST['harga_beli']
        produk.stok = request.POST['stok']
        produk.stok_minimum = request.POST['stok_minimum']
        produk.satuan = request.POST['satuan']
        produk.aktif = 'aktif' in request.POST
        produk.save()
        messages.success(request, 'Produk berhasil diupdate.')
        return redirect('produk:list')
    return render(request, 'produk/form.html', {
        'kategori': kategori,
        'produk': produk,
        'action': 'Edit'
    })

@login_required
def hapus_produk(request, pk):
    produk = get_object_or_404(Produk, pk=pk)
    produk.delete()
    messages.success(request, 'Produk berhasil dihapus.')
    return redirect('produk:list')

@login_required
def list_kategori(request):
    kategori = Kategori.objects.all().order_by('nama')
    cari = request.GET.get('cari')
    if cari:
        kategori = kategori.filter(nama__icontains=cari)
    return render(request, 'produk/kategori.html', {
        'kategori': kategori,
        'cari': cari,
    })

@login_required
def tambah_kategori(request):
    if request.method == 'POST':
        nama = request.POST.get('nama', '').strip()
        deskripsi = request.POST.get('deskripsi', '').strip()
        if not nama:
            messages.error(request, 'Nama kategori harus diisi.')
            return redirect('produk:kategori')
        if Kategori.objects.filter(nama__iexact=nama).exists():
            messages.error(request, f'Kategori "{nama}" sudah ada.')
            return redirect('produk:kategori')
        Kategori.objects.create(nama=nama, deskripsi=deskripsi)
        messages.success(request, f'Kategori "{nama}" berhasil ditambahkan.')
        return redirect('produk:kategori')
    return redirect('produk:kategori')

@login_required
def edit_kategori(request, pk):
    kategori = get_object_or_404(Kategori, pk=pk)
    if request.method == 'POST':
        nama = request.POST.get('nama', '').strip()
        deskripsi = request.POST.get('deskripsi', '').strip()
        if not nama:
            messages.error(request, 'Nama kategori harus diisi.')
            return redirect('produk:kategori')
        if Kategori.objects.filter(nama__iexact=nama).exclude(pk=pk).exists():
            messages.error(request, f'Kategori "{nama}" sudah ada.')
            return redirect('produk:kategori')
        kategori.nama = nama
        kategori.deskripsi = deskripsi
        kategori.save()
        messages.success(request, f'Kategori "{nama}" berhasil diupdate.')
        return redirect('produk:kategori')
    return render(request, 'produk/edit_kategori.html', {'kategori': kategori})

@login_required
def hapus_kategori(request, pk):
    kategori = get_object_or_404(Kategori, pk=pk)
    if kategori.produk_set.exists():
        messages.error(request, f'Kategori "{kategori.nama}" tidak bisa dihapus karena masih ada produk.')
        return redirect('produk:kategori')
    nama = kategori.nama
    kategori.delete()
    messages.success(request, f'Kategori "{nama}" berhasil dihapus.')
    return redirect('produk:kategori')