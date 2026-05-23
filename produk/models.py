from django.db import models

class Kategori(models.Model):
    nama = models.CharField(max_length=100)
    deskripsi = models.TextField(blank=True)

    def __str__(self):
        return self.nama

    class Meta:
        verbose_name_plural = "Kategori"


class Produk(models.Model):
    kategori = models.ForeignKey(Kategori, on_delete=models.SET_NULL, null=True, blank=True)
    nama = models.CharField(max_length=200)
    barcode = models.CharField(max_length=100, unique=True, blank=True, null=True)
    harga_jual = models.DecimalField(max_digits=12, decimal_places=0)
    harga_beli = models.DecimalField(max_digits=12, decimal_places=0)
    stok = models.IntegerField(default=0)
    stok_minimum = models.IntegerField(default=5)
    satuan = models.CharField(max_length=20, default='pcs')
    aktif = models.BooleanField(default=True)
    dibuat = models.DateTimeField(auto_now_add=True)
    diubah = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.nama

    @property
    def stok_menipis(self):
        return self.stok <= self.stok_minimum

    class Meta:
        verbose_name_plural = "Produk"