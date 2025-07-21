from django.db import models

class Transferencia(models.Model):
    ESTADOS = [
        ('pendiente', 'Pendiente'),
        ('completada', 'Completada'),
        ('rechazada', 'Rechazada'),
    ]

    cuenta_origen = models.CharField(max_length=20)
    cuenta_destino = models.CharField(max_length=20)
    cooperativa_origen = models.CharField(max_length=100)
    cooperativa_destino = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)
    comision = models.DecimalField(max_digits=10, decimal_places=2, default=0.41)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='pendiente')
    fecha_envio = models.DateTimeField(auto_now_add=True)
    fecha_confirmacion = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.cuenta_origen} → {self.cuenta_destino} ({self.estado})"

