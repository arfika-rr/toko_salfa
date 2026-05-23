from django.db import models
from django.contrib.auth.models import User
from produk.models import Produk

class StokMasuk(models.Model):
    produk = models.ForeignKey(Produk, on_delete=models.CASCADE)
    jumlah = models.IntegerField()
    harga_beli = models.DecimalField(max_digits=12, decimal_places=0)
    tanggal = models.DateTimeField(auto_now_add=True)
    dicatat_oleh = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    keterangan = models.TextField(blank=True)

    def __str__(self):
        return f"{self.produk.nama} +{self.jumlah} ({self.tanggal.date()})"

    class Meta:
        verbose_name_plural = "Stok Masuk"