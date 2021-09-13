from django.db import models


# Create your models here.

# Module Products

class Category(models.Model):
    name = models.CharField('Nombre', max_length=80, null=False)
    description = models.CharField ('Descripción', max_length= 150, null=False, unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Categoría'
        verbose_name_plural = 'Categorías'
        db_table = 'Category'
        ordering = ['id']

class UnitMeasurement(models.Model):
    unit = models.CharField('Unidad de medida', max_length=100, null=False, unique=True)

    def __str__(self):
        return self.unit

    class Meta:
        verbose_name = 'Unidad de medida'
        verbose_name_plural = 'Unidades de medida'
        db_table = 'UnitMeasurement'
        ordering = ['id']

class Products(models.Model):
    product = models.CharField('Producto', max_length=80, unique=True, null=False)
    description = models.CharField('Descripción', max_length=150, null=False)
    unit_price = models.DecimalField('Precio', default=0.00, max_digits=10, decimal_places=2)
    amount = models.PositiveSmallIntegerField('Cantidad', default=0, null=False )
    discount = models.DecimalField('Descuento', null=True,blank=True, max_digits=7, decimal_places=2)
    categoty = models.ForeignKey(Category, on_delete=models.CASCADE)
    unit_measurement = models.ForeignKey(UnitMeasurement, on_delete=models.CASCADE)

    def __str__(self):
        return self.product

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'Product'
        ordering = ['id']
