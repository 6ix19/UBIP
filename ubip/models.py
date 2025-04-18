from django.db import models


class actividad(models.Model):
    ip = models.CharField(max_length=20)
    frecuencia_de_uso = models.DecimalField(max_digits=4, decimal_places=2)
    tipo_de_trafico = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Actividad'
        db_table = 'actividad'

class conectividad(models.Model):
    id_conectividad = models.AutoField(primary_key=True)
    densidad_de_ip = models.IntegerField(max_length=100)
    codigo_postal = models.CharField(max_length=20)

    class Meta:
        verbose_name = 'Conectividad'
        db_table = 'conectividad'

class ip(models.Model):
    ip_inicio = models.CharField(max_length=20)
    ip_final = models.CharField(max_length=20)
    asn = models.CharField(max_length=100)  
    provedor = models.CharField(max_length=100)
    id_zona_georafica = models.ForeignKey('zonas_geograficas', on_delete=models.CASCADE      )

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

class nivel_socioeconomico(models.Model):
    id_nivel_socioeconomico = models.AutoField(primary_key=True)
    nivel = models.CharField(max_length=20)
    ingreso_minimo = models.DecimalField(max_digits=10, decimal_places=2)
    ingreso_maximo = models.DecimalField(max_digits=10, decimal_places=2)
    descripcion = models.TextField()

    class Meta:
        verbose_name = 'Nivel Socioeconomico'
        db_table = 'nivel_socioeconomico'

class secotres_economicos(models.Model):
    id_sector_economico = models.AutoField(primary_key=True)
    sector = models.CharField(max_length=100)
    descripcion = models.TextField()

    class Meta:
        verbose_name = 'Sector Economico'
        db_table = 'secotres_economicos'

#class caracteriticas_socioeconomicas(models.Model):
#    id_colonia = models.AutoField(primary_key=True)
#    nombre_colonia = models.CharField(max_length=100)
#    codigo_postal = models.CharField(max_length=20)
#    id_nivel_socioeconomico = models.ForeignKey(nivel_socioeconomico, on_delete=models.CASCADE)
#    poblacion_total = models.IntegerField()
#    id_sector_economico = models.ForeignKey(secotres_economicos, on_delete=models.CASCADE)
#    vivienda_total = models.IntegerField()
#    acceso_internet = models.DecimalField(max_digits=5, decimal_places=2)
#    vehiculo_promedio = models.DecimalField(max_digits=3, decimal_places=1)
#    delincuencia_percibida = models.CharField(max_length=10)
#    costo_promedio_renta = models.DecimalField(max_digits=10, decimal_places=2)
#    infraestructura = models.CharField(max_length=100)
#    id_zona_georafica = models.ForeignKey(zonas_geograficas, on_delete=models.CASCADE)
#    class Meta:
#        verbose_name = 'Caracteristicas Socioeconomicas'
#        db_table = 'caracteriticas_socioeconomicas'


                           