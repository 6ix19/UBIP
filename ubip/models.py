from django.db import models

class Direction_ip(models.Model):
    ip_inicio = models.CharField(max_length=20)
    ip_final = models.CharField(max_length=20)
    asn = models.CharField(max_length=100)  
    provedor = models.CharField(max_length=100)
    id_zona_georafica = models.ForeignKey(
        'zonas_geograficas',  
        on_delete=models.CASCADE      )

    class Meta:
        verbose_name = 'Rango de IP'
        db_table = 'direction_ip'

class zonas_geograficas(models.Model):
    estado_o_provincia = models.CharField(max_length=100) 
    ciudad = models.CharField(max_length=100) 
    coordenadas = models.CharField(max_length=100)
    nivel_de_conectividad = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Zona Geografica'
        db_table = 'zonas_geograficas'