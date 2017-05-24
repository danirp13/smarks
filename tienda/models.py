from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Categoria(models.Model):
    id_categoria = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    descripcion = models.CharField(max_length=250, blank=True, null=True)
    def get_absolute_url(self):
        return reverse ('categoria-list')
    def __str__(self):
    	return self.nombre


class Producto(models.Model):
    id_producto = models.AutoField(primary_key=True)
    id_categoria = models.ForeignKey(Categoria)
    photo = models.ImageField(upload_to='photos/')
    nombre = models.CharField(max_length=80, blank=True, null=True)
    cantidad = models.BigIntegerField(blank=True, null=True)
    precio = models.BigIntegerField(blank=True, null=True)
    fecha_ingreso = models.DateField(blank=True, null=True)
    def get_absolute_url(self):
        return reverse ('producto-list')
    def __str__(self):
    	return self.nombre
    
class Cliente(models.Model): 
    id_cliente = models.AutoField(primary_key=True)
    cedula = models.BigIntegerField(blank=True, null=True)
    nombre = models.CharField(max_length=80, blank=True, null=True)
    apellidos = models.CharField(max_length=80, blank=True, null=True)
    email = models.CharField(max_length=80, blank=True, null=True)
    celular = models.BigIntegerField(blank=True, null=True)
    def get_absolute_url(self):
        return reverse ('cliente-list')
    def __str__(self):
        return self.nombre     

class Venta(models.Model): 
    id_venta = models.AutoField(primary_key=True)
    cliente = models.ForeignKey(Cliente, blank=True, null=True)
    cantidad_venta = models.BigIntegerField(blank=True, null=True)
    valor = models.BigIntegerField(blank=True, null=True)
    fecha_venta = models.DateField(blank=True, null=True)
    productos= models.ManyToManyField(Producto)
    def get_absolute_url(self):
        return reverse ('venta-list')
    def __str__(self):
        return (str(self.id_venta))    
    