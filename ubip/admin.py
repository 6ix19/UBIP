from django.contrib import admin
from . models import ip, zonas_geograficas, actividad, conectividad, nivel_socioeconomico, secotres_economicos#, caracteriticas_socioeconomicas

# Register your models here.

admin.site.register(ip)
admin.site.register(zonas_geograficas)
admin.site.register(actividad)
admin.site.register(conectividad)
admin.site.register(nivel_socioeconomico)
admin.site.register(secotres_economicos)    
#admin.site.register(caracteriticas_socioeconomicas)