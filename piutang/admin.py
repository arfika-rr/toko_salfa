from django.contrib import admin
from .models import Pelanggan, Piutang, PembayaranPiutang

@admin.register(Pelanggan)
class PelangganAdmin(admin.ModelAdmin):
    list_display = ['nama', 'telepon', 'alamat']

class PembayaranInline(admin.TabularInline):
    model = PembayaranPiutang
    extra = 0

@admin.register(Piutang)
class PiutangAdmin(admin.ModelAdmin):
    list_display = ['pelanggan', 'nominal', 'terbayar', 'status', 'jatuh_tempo']
    inlines = [PembayaranInline]