from django.db import models
from django.contrib.auth.models import User
from produk.models import Produk

class Transaksi(models.Model):
    METODE_BAYAR = [
        ('tunai', 'Tunai'),
        ('transfer', 'Transfer'),
        ('qris', 'QRIS'),
        ('piutang', 'Piutang'),
    ]
    STATUS = [
        ('selesai', 'Selesai'),
        ('batal', 'Dibatalkan'),
    ]
    kasir = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    kode_transaksi = models.CharField(max_length=20, unique=True)
    tanggal = models.DateTimeField(auto_now_add=True)
    total = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    bayar = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    kembalian = models.DecimalField(max_digits=12, decimal_places=0, default=0)
    metode_bayar = models.CharField(max_length=20, choices=METODE_BAYAR, default='tunai')
    status = models.CharField(max_length=10, choices=STATUS, default='selesai')
    alasan_batal = models.TextField(blank=True)

    def __str__(self):
        return self.kode_transaksi

    class Meta:
        verbose_name_plural = "Transaksi"


class DetailTransaksi(models.Model):
    transaksi = models.ForeignKey(Transaksi, on_delete=models.CASCADE, related_name='detail')
    produk = models.ForeignKey(Produk, on_delete=models.SET_NULL, null=True)
    jumlah = models.IntegerField()
    harga_satuan = models.DecimalField(max_digits=12, decimal_places=0)
    subtotal = models.DecimalField(max_digits=12, decimal_places=0)

    def save(self, *args, **kwargs):
        self.subtotal = self.jumlah * self.harga_satuan
        super().save(*args, **kwargs)

    def __str__(self):
        nama_produk = self.produk.nama if self.produk else "Produk Dihapus"
        return f"{self.transaksi.kode_transaksi} - {nama_produk}"