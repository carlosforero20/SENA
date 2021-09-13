from django.contrib import admin
from .models import DeliveryType
from .models import PaymentType
from .models import TypeAccountingDocument
from .models import OrderDetail
from .models import OrderHeader
from .models import AccountingDocument
# Register your models here.

@admin.register(PaymentType)
class PaymentTypeAdmin(admin.ModelAdmin):
    list_display = ['account', 'description']
    list_per_page = 3

admin.site.register(TypeAccountingDocument)

@admin.register(OrderDetail)
class OrderDetailAdmin(admin.ModelAdmin):
    list_display = ['amount', 'subtotal', 'total']
    
    list_filter = ['amount']
    list_per_page = 20

@admin.register(OrderHeader)
class OrderHeader(admin.ModelAdmin):
    list_display = ['date', 'status', 'payment_reference']
    list_editable = ['status']
    list_filter = ['date']
    search_fields = ['date']
    list_per_page = 10

@admin.register(AccountingDocument)
class AccountingDocumentType (admin.ModelAdmin):
    list_display = ['reference','date']
    search_fields = ['reference']
    list_per_page = 10
