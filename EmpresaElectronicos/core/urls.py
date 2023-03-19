from django.contrib import admin
from django.urls import path, include
from core.views import inicio, result_busc_productos, agregar_cliente, agregar_empleado, agregar_producto

urlpatterns = [
    path('', inicio, name='inicio'),
    path('resultado-busqueda-productos/', result_busc_productos, name='resultado_busq_productos'),
    path('agregar-cliente/', agregar_cliente, name='agrega_cliente'),
    path('agregar-empleado/', agregar_empleado, name='agrega_empleado'),
    path('agregar-producto/', agregar_producto, name='agrega_producto'),
]