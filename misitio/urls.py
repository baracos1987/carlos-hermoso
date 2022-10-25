#Se creó este archivo urls.py con su respectivo contenido
from django.urls import path
from.import views

urlpatterns = [
    path('', views.index, name='home'), #ingresa al index de la pagina desde el archivo views.py
    path('Rodamientos', views.Rodamientos, name='Rodamientos'),#ingresa al Rodamientos de la pagina desde el archivo views.py
    path('contactenos', views.contact, name='contactenos'), #ingresa al contacto de la pagina desde el archivo views.py
    path('menu', views.menu, name='menu'),
]

