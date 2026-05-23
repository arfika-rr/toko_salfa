from django.contrib import admin
from .models import Kategori, Produk

@admin.register(Kategori)
class KategoriAdmin(admin.ModelAdmin):
    list_display = ['nama', 'deskripsi']

@admin.register(Produk)
class ProdukAdmin(admin.ModelAdmin):
    list_display = ['nama', 'kategori', 'barcode', 'harga_jual', 'stok', 'stok_minimum', 'aktif']
    list_filter = ['kategori', 'aktif']
    search_fields = ['nama', 'barcode']