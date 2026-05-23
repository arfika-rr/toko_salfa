from django.urls import path
from . import views

app_name = 'stok'
urlpatterns = [
    path('', views.list_stok, name='list'),
    path('tambah/', views.tambah_stok, name='tambah'),
    path('export/csv/', views.export_stok_csv, name='export_csv'),
    path('export/excel/', views.export_stok_excel, name='export_excel'),
    path('export/pdf/', views.export_stok_pdf, name='export_pdf'),
]