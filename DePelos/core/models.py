from django.db import models

# Create your models here.

class Categoria (models.Model): 
    idCategoria = models.IntegerField(primary_key=True, verbose_name='Id de Mascota')
    nombreCategoria= models.CharField(max_length=50, verbose_name='Tipo de mascota')

    def __str__(self):
        return self.nombreCategoria

class Producto(models.Model):
    id_producto = models.CharField(max_length=30, primary_key=True, verbose_name='Nombre Del Producto')
    marca = models.CharField(max_length=20, verbose_name='Marca del Producto')
    tipo = models.CharField(max_length=500, verbose_name='Descripcion del producto')
    imagen = models.ImageField(upload_to="imagenes", null=True, verbose_name='Imagen del producto')
    categoria=models.ForeignKey(Categoria, on_delete=models.CASCADE)

    def __str__(self):
        return self.id_producto


class Categoria2 (models.Model): 
    idCategoria2 = models.IntegerField(primary_key=True, verbose_name='Id de Categoría')
    nombreCategoria2= models.CharField(max_length=50, verbose_name='Nombre de Categoría')

    def __str__(self):
        return self.nombreCategoria2

class Usuarios(models.Model):
    nombre = models.CharField(max_length=40, verbose_name='Nombre de usuario')
    email = models.CharField(max_length=40,primary_key=True, verbose_name='Email')
    numero =models.CharField(max_length=10, verbose_name='Fono')
    passs =models.CharField(max_length=10,  verbose_name='rut')
    categoria2=models.ForeignKey(Categoria2, on_delete=models.CASCADE)

    def __str__(self):
        return self.email


