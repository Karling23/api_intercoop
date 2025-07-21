from django.urls import path
from . import views

urlpatterns = [
    path('interbancaria/', views.crear_transferencia),
    path('confirmar/', views.confirmar_transferencia),
    path('pendientes/', views.transferencias_pendientes),
    path('confirmadas/', views.transferencias_confirmadas),
]
