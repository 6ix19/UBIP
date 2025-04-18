from django.shortcuts import render
from .models import ip, zonas_geograficas, actividad, conectividad, nivel_socioeconomico, secotres_economicos#, caracteriticas_socioeconomicas

# Create your views here.

def index (request):
    return render(request, 'ubip/index.html')

