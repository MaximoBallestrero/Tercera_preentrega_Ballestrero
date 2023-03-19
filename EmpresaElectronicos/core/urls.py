from django.contrib import admin
from django.urls import path, include
from core.views import inicio, agregar_cliente, agregar_empleado, agregar_producto

urlpatterns = [
    path('', inicio, name='inicio'),
    path('agregar-cliente/', agregar_cliente, name='agrega_cliente'),
    path('agregar-empleado/', agregar_empleado, name='agrega_empleado'),
    path('agregar-producto/', agregar_producto, name='agrega_producto'),
]