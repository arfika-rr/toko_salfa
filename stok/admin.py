from django.contrib import admin
from .models import StokMasuk

@admin.register(StokMasuk)
class StokMasukAdmin(admin.ModelAdmin):
    list_display = ['produk', 'jumlah', 'harga_beli', 'tanggal', 'dicatat_oleh']