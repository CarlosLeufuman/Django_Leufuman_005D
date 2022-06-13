from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from . models import Categoria, Producto , Usuarios , Categoria2

class ProductoForm(forms.ModelForm):

    class Meta: 
        model= Producto
        fields = ['id_producto', 'marca', 'tipo','imagen', 'categoria']
        labels ={
            'id_producto': 'Nombre De Producto:', 
            'marca': 'Marca:', 
            'tipo': 'Descricion:', 
            'imagen': 'Imagen:',
            'categoria': 'Animal:',
        }
        widgets={
            'id_producto': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombre del Producto', 
                    'id': 'id_patente'
                }
            ), 
            'marca': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese marca', 
                    'id': 'marca'
                }
            ), 
            'tipo': forms.Textarea(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Descipcion del producto', 
                    'id': 'tipo'
                }
            ), 
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Descipcion del producto', 
                    'id': 'imagen'
                }
            ),  
            'categoria': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria',
                }
            )

        }

class UsuarioForm(forms.ModelForm):

    class Meta: 
        model= Usuarios
        fields = ['nombre', 'email', 'numero', 'passs','categoria2']
        labels ={
            'nombre': 'Nombre:', 
            'email': 'Email:', 
            'numero': 'Numero:', 
            'passs': 'Rut:',
            'categoria2': 'Sexo:',
        }
        widgets={
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Nombre y Apellido', 
                    'id': 'nombre'
                }
            ), 
            'email': forms.EmailInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese Email (nick@gmail.com)', 
                    'id': 'email'
                }
            ), 
            'numero': forms.NumberInput(
                attrs={
                    'class': 'form-control', 
                    'placeholder': 'Ingrese numero EJ: 9 5432 1234', 
                    'id': 'numero'
                }
            ), 
            'passs': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese RUT EJ: 20418238-1',
                    'id': 'passs',
                }
            ),
            'categoria2': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'categoria2',
                }
            )

        }