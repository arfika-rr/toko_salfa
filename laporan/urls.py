from django.urls import path
from . import views

app_name = 'laporan'
urlpatterns = [
    path('', views.dashboard_laporan, name='dashboard'),
    path('export/csv/', views.export_laporan_csv, name='export_csv'),
    path('export/excel/', views.export_laporan_excel, name='export_excel'),
    path('export/pdf/', views.export_laporan_pdf, name='export_pdf'),
]