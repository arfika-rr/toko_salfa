from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # tambah ini
    path('', views.dashboard, name='dashboard'),
    path('produk/', include('produk.urls', namespace='produk')),
    path('kasir/', include('kasir.urls', namespace='kasir')),
    path('stok/', include('stok.urls', namespace='stok')),
    path('piutang/', include('piutang.urls', namespace='piutang')),
    path('laporan/', include('laporan.urls', namespace='laporan')),
]