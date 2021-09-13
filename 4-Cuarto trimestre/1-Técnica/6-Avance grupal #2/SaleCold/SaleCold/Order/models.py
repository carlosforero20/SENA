from django.db import models
from Product.models import Products
from User.models import User
# Create your models here.


class DeliveryType(models.Model):
    description = models.CharField('Tipo de entrega', null=False, unique=True, max_length=100)


    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Tipo de entrega'
        verbose_name_plural = 'Tipos de entrega'
        db_table = 'DeliveryType'
        ordering = ['id']

class PaymentType(models.Model):
    account = models.CharField('Tipo de pago', max_length=80, unique=True, null=False) #se agrega atributo para los número de cuenta
    description = models.CharField('Numero de cuenta', max_length=80, unique=True, null=False)

    def __str__(self):
        return self.account

    class Meta:
        verbose_name = 'Tipo de pago '
        verbose_name_plural = 'Tipos de pago'
        db_table = 'PaymentType'
        ordering = ['id']

class TypeAccountingDocument(models.Model):
    description = models.CharField('Tipo documento contable', max_length=80, unique=True, null=False)

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Tipo de documento contable '
        verbose_name_plural = 'Tipos de documentos contables'
        db_table = 'TypeAccountingDocument'
        ordering = ['id']

class OrderDetail(models.Model):
    amount = models.PositiveSmallIntegerField('Cantidad', default=0, null=False)
    subtotal = models.DecimalField('Subtotal', max_digits=10, decimal_places=2, null=False)
    total = models.DecimalField('Total', max_digits=10, decimal_places=2, null=False)
    product = models.ManyToManyField(Products)

    def __int__(self):
        return self.amount

    class Meta:
        verbose_name = 'Detalle de pedido'
        verbose_name_plural = 'Detalles de pedido'
        db_table = 'OrderDetail'
        ordering = ['id']

class OrderHeader(models.Model):
    date = models.DateField('Fecha de pedido', blank=False, auto_created=True)
    status = models.BooleanField('Confirmado', default=True)
    payment_reference = models.CharField('Referencía de pago', max_length=80, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_type = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    delivery_type = models.ForeignKey (DeliveryType, on_delete=models.CASCADE)
    order_detail = models.OneToOneField(OrderDetail, on_delete=models.CASCADE)

    def __date__(self):
        return self.date

    class Meta:
        verbose_name = 'Cabecera de pedido'
        verbose_name_plural = 'Cabeceras de pedido'
        db_table = 'HeaderOrder'
        ordering = ['id']

class AccountingDocument(models.Model):
    reference = models.CharField('Referencia', max_length=50, null=False, unique=True)#Referencía de la factura..
    date = models.DateField('Fecha', blank=False, auto_created=True)
    type_accounting_document = models.ForeignKey(TypeAccountingDocument, on_delete=models.CASCADE)
    order_header = models.OneToOneField(OrderHeader, on_delete=models.CASCADE)

    def __str__(self):
        return self.reference

    class Meta:
        verbose_name = 'Documento contable'
        verbose_name_plural = 'Documentos contables'
        db_table = 'AccountingDocument'
        ordering = ['id'] 
        