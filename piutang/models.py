from django.db import models
from kasir.models import Transaksi

class Pelanggan(models.Model):
    nama = models.CharField(max_length=200)
    telepon = models.CharField(max_length=20, blank=True)
    alamat = models.TextField(blank=True)
    dibuat = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Pelanggan"


class Piutang(models.Model):
    STATUS = [
        ('belum', 'Belum Lunas'),
        ('sebagian', 'Sebagian'),
        ('lunas', 'Lunas'),
    ]
    pelanggan = models.ForeignKey(Pelanggan, on_delete=models.CASCADE)
    transaksi = models.OneToOneField(Transaksi, on_delete=models.SET_NULL, null=True, blank=True)
    nominal = models.DecimalField(max_digits=12, decimal_places=0)
    terbayar = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    status = models.CharField(max_length=10, choices=STATUS, default='belum')
    jatuh_tempo = models.DateField(null=True, blank=True)
    catatan = models.TextField(blank=True)
    dibuat = models.DateTimeField(auto_now_add=True)

    @property
    def sisa(self):
        return self.nominal - self.terbayar

    def __str__(self):
        return f"{self.pelanggan.nama} - Rp{self.nominal}"

    class Meta:
        verbose_name_plural = "Piutang"


class PembayaranPiutang(models.Model):
    piutang = models.ForeignKey(Piutang, on_delete=models.CASCADE, related_name='pembayaran')
    jumlah = models.DecimalField(max_digits=12, decimal_places=0)
    tanggal = models.DateTimeField(auto_now_add=True)
    catatan = models.TextField(blank=True)

    def __str__(self):
        return f"Bayar {self.piutang.pelanggan.nama} - Rp{self.jumlah}"