from django.urls import path
from . import views

app_name = 'piutang'
urlpatterns = [
    path('', views.list_piutang, name='list'),
    path('tambah/', views.tambah_piutang, name='tambah'),
    path('bayar/<int:pk>/', views.bayar_piutang, name='bayar'),
    path('pelanggan/tambah/', views.tambah_pelanggan, name='tambah_pelanggan'),
]