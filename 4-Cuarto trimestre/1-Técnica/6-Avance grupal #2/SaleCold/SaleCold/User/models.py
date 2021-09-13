
from django.db import models
from django.db.models.base import Model
from django.db.models.expressions import F
# Create your models here.
class TypeUser (models.Model):
    description = models.CharField('Tipo de usuario', max_length=80, unique=True, null=False)

    def __str__(self): 
        return self.description
    
    class Meta:
        verbose_name = 'Tipo de usuario'
        verbose_name_plural = 'Tipos de usuario'
        db_table = 'TypeUser'
        ordering = ['id']

class TypeId(models.Model):
    description = models.CharField ('Identificación', max_length=30, unique=True, null=False)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Identificación'
        verbose_name_plural = 'Identificaciones'
        db_table = 'TypeId'
        ordering = ['id']

class Town(models.Model):
    description = models.CharField('Ciudad', max_length=80, unique=True, null=False)
    postal_code = models.PositiveSmallIntegerField('Código postal', unique=True, null=False)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Ciudad'
        verbose_name_plural = 'Ciudades'
        db_table = 'Town'
        ordering = ['id']


class User(models.Model):
    name = models.CharField('Nombres', max_length=50, null=False, unique=True)
    surname = models.CharField('Apellidos', max_length=50, null=False)
    user_id = models.PositiveIntegerField('Identificación',unique=True, null=False)
    email = models.EmailField('Correo', unique=True, null=False)
    password = models.CharField('Contraseña', max_length=50, null=False)
    address = models.CharField('Dirección',max_length=50, null=False)
    type_user = models.ForeignKey(TypeUser, on_delete=models.CASCADE)
    type_id = models.ForeignKey(TypeId, on_delete=models.CASCADE)
    town = models.ForeignKey(Town, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Usuario'
        verbose_name_plural = 'Usuarios'
        db_table = 'User'
        ordering = ['id']