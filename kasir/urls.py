from django.urls import path
from . import views

app_name = 'kasir'
urlpatterns = [
    path('', views.kasir, name='kasir'),
    path('barcode/', views.cari_barcode, name='barcode'),
    path('proses/', views.proses_transaksi, name='proses'),
    path('riwayat/', views.riwayat_transaksi, name='riwayat'),
    path('riwayat/<int:pk>/', views.detail_transaksi, name='detail'),
    path('riwayat/<int:pk>/batal/', views.batal_transaksi, name='batal'),
    path('riwayat/<int:pk>/hapus/', views.hapus_transaksi, name='hapus'),
    path('export/csv/', views.export_csv, name='export_csv'),
    path('export/excel/', views.export_excel, name='export_excel'),
    path('export/pdf/', views.export_pdf, name='export_pdf'),
]