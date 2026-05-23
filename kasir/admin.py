from django.contrib import admin
from .models import Transaksi, DetailTransaksi

class DetailTransaksiInline(admin.TabularInline):
    model = DetailTransaksi
    extra = 0

@admin.register(Transaksi)
class TransaksiAdmin(admin.ModelAdmin):
    list_display = ['kode_transaksi', 'kasir', 'tanggal', 'total', 'metode_bayar']
    inlines = [DetailTransaksiInline]