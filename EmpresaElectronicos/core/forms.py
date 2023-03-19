from django import forms

class AgregaClienteForm(forms.Form):
    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    email=forms.EmailField()

class AgregaEmpleadoForm(forms.Form):
    nombre=forms.CharField(max_length=20)
    apellido=forms.CharField(max_length=20)
    puesto=forms.CharField(max_length=20)
    email=forms.EmailField()

class AgregaProductoForm(forms.Form):
    nombre=forms.CharField(max_length=20)
    precio=forms.FloatField()

