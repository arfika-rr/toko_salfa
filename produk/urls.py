from django.urls import path
from . import views

app_name = 'produk'
urlpatterns = [
    path('', views.list_produk, name='list'),
    path('tambah/', views.tambah_produk, name='tambah'),
    path('edit/<int:pk>/', views.edit_produk, name='edit'),
    path('hapus/<int:pk>/', views.hapus_produk, name='hapus'),
    path('kategori/', views.list_kategori, name='kategori'),
    path('kategori/tambah/', views.tambah_kategori, name='tambah_kategori'),
    path('kategori/edit/<int:pk>/', views.edit_kategori, name='edit_kategori'),
    path('kategori/hapus/<int:pk>/', views.hapus_kategori, name='hapus_kategori'),
]