from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Pelanggan, Piutang, PembayaranPiutang

@login_required
def list_piutang(request):
    piutang = Piutang.objects.select_related('pelanggan').order_by('-dibuat')
    status = request.GET.get('status')
    if status:
        piutang = piutang.filter(status=status)
    return render(request, 'piutang/list.html', {
        'piutang': piutang,
        'status_aktif': status,
    })

@login_required
def tambah_piutang(request):
    pelanggan = Pelanggan.objects.all().order_by('nama')
    if request.method == 'POST':
        p = Pelanggan.objects.get(pk=request.POST['pelanggan'])
        Piutang.objects.create(
            pelanggan=p,
            nominal=request.POST['nominal'],
            jatuh_tempo=request.POST.get('jatuh_tempo') or None,
            catatan=request.POST.get('catatan', ''),
        )
        messages.success(request, f'Piutang {p.nama} berhasil dicatat.')
        return redirect('piutang:list')
    return render(request, 'piutang/form.html', {'pelanggan': pelanggan})

@login_required
def bayar_piutang(request, pk):
    piutang = get_object_or_404(Piutang, pk=pk)
    if request.method == 'POST':
        jumlah = int(request.POST['jumlah'])
        PembayaranPiutang.objects.create(
            piutang=piutang,
            jumlah=jumlah,
            catatan=request.POST.get('catatan', ''),
        )
        piutang.terbayar += jumlah
        if piutang.terbayar >= piutang.nominal:
            piutang.status = 'lunas'
        elif piutang.terbayar > 0:
            piutang.status = 'sebagian'
        piutang.save()
        messages.success(request, f'Pembayaran Rp{jumlah:,} berhasil dicatat.')
        return redirect('piutang:list')
    return render(request, 'piutang/bayar.html', {'piutang': piutang})

@login_required
def tambah_pelanggan(request):
    if request.method == 'POST':
        Pelanggan.objects.create(
            nama=request.POST['nama'],
            telepon=request.POST.get('telepon', ''),
            alamat=request.POST.get('alamat', ''),
        )
        messages.success(request, 'Pelanggan berhasil ditambahkan.')
        return redirect('piutang:list')
    return render(request, 'piutang/pelanggan_form.html')