from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    #path('ubip/', views.ubip, name='ubip'),
    #path('ubip/<str:ip>/', views.ubip, name='ubip_detail'),
    #path('ubip/zonas_geograficas/', views.zonas_geograficas, name='zonas_geograficas'),
    #path('ubip/zonas_geograficas/<int:id_zona_geografica>/', views.zonas_geograficas, name='zona_geografica_detail'),
]
