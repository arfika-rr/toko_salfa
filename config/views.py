from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.utils import timezone
from django.db.models import F, Sum
from kasir.models import Transaksi, DetailTransaksi
from produk.models import Produk
from piutang.models import Piutang

@login_required
def dashboard(request):
    hari_ini = timezone.now().date()
    
    # Transaksi hari ini
    transaksi_hari_ini = Transaksi.objects.filter(tanggal__date=hari_ini)
    omzet_hari_ini = transaksi_hari_ini.aggregate(s=Sum('total'))['s'] or 0

    # Hitung keuntungan hari ini
    detail_hari_ini = DetailTransaksi.objects.filter(transaksi__tanggal__date=hari_ini)
    keuntungan_hari_ini = sum(
        (d.harga_satuan - d.produk.harga_beli) * d.jumlah
        for d in detail_hari_ini.select_related('produk')
    )

    # Transaksi bulan ini
    bulan_ini = timezone.now().month
    tahun_ini = timezone.now().year
    transaksi_bulan = Transaksi.objects.filter(
        tanggal__month=bulan_ini,
        tanggal__year=tahun_ini,
    )
    omzet_bulan = transaksi_bulan.aggregate(s=Sum('total'))['s'] or 0

    # Keuntungan bulan ini
    detail_bulan = DetailTransaksi.objects.filter(
        transaksi__tanggal__month=bulan_ini,
        transaksi__tanggal__year=tahun_ini,
    )
    keuntungan_bulan = sum(
        (d.harga_satuan - d.produk.harga_beli) * d.jumlah
        for d in detail_bulan.select_related('produk')
    )

    context = {
        'transaksi_hari_ini': transaksi_hari_ini.count(),
        'omzet_hari_ini': omzet_hari_ini,
        'keuntungan_hari_ini': keuntungan_hari_ini,
        'omzet_bulan': omzet_bulan,
        'keuntungan_bulan': keuntungan_bulan,
        'stok_menipis': Produk.objects.filter(stok__lte=F('stok_minimum')).count(),
        'piutang_belum_lunas': Piutang.objects.exclude(status='lunas').count(),
        'transaksi_terakhir': Transaksi.objects.order_by('-tanggal')[:5],
        'produk_menipis': Produk.objects.filter(stok__lte=F('stok_minimum'))[:5],
    }
    return render(request, 'dashboard.html', context)