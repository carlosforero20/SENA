from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField('Categoria', max_length=50)
    description = models.TextField('Descripcion', max_length=150)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'category'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField('Productos', max_length=50)
    price = models.DecimalField ('Precio', default=0.00, max_digits=9, decimal_places=2)
    amount = models.PositiveIntegerField('cantidad', default=0)
    description = models.TextField('Descripcion', max_length=150)
    state = models.BooleanField('Estado', default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table ='products'
        ordering = ['id']
