from django.shortcuts import render
from core.forms import AgregaClienteForm, AgregaEmpleadoForm, AgregaProductoForm
from core.models import Cliente, Empleado, Producto

# Create your views here.
def inicio(request):
    return render(request, 'core/index.html')



def agregar_cliente(request):
    if request.method=='POST':
        agr_cliente_form=AgregaClienteForm(request.POST)
        if agr_cliente_form.is_valid():
            data=agr_cliente_form.cleaned_data
            cliente=Cliente(nombre=data['nombre'], apellido=data['apellido'], email=data['email'])
            cliente.save()
            return render(request, 'core/index.html')

    agr_cliente_form=AgregaClienteForm()
    return render(request, 'core/agregar_cliente.html', {'agr_cliente_form':agr_cliente_form})



def agregar_empleado(request):
    if request.method=='POST':
        agr_empleado_form=AgregaEmpleadoForm(request.POST)
        if agr_empleado_form.is_valid():
            data=agr_empleado_form.cleaned_data
            empleado=Empleado(nombre=data['nombre'], apellido=data['apellido'], puesto=data['puesto'], email=data['email'])
            empleado.save()
            return render(request, 'core/index.html')

    agr_empleado_form=AgregaEmpleadoForm()
    return render(request, 'core/agregar_empleado.html', {'agr_empleado_form':agr_empleado_form})



def agregar_producto(request):
    if request.method=='POST':
        agr_producto_form=AgregaProductoForm(request.POST)
        if agr_producto_form.is_valid():
            data=agr_producto_form.cleaned_data
            producto=Producto(nombre=data['nombre'], precio=data['precio'])
            producto.save()
            return render(request, 'core/index.html')

    agr_producto_form=AgregaProductoForm()
    return render(request, 'core/agregar_producto.html', {'agr_producto_form':agr_producto_form})