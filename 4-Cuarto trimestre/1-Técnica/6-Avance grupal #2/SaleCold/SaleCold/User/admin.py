from django.contrib import admin

# Register your models here.
from .models import TypeUser
from .models import TypeId
from .models import Town
from .models import User

admin.site.register(TypeUser)
admin.site.register(TypeId)

@admin.register(Town)
class TownAdmin(admin.ModelAdmin):
    list_display = ['description', 'postal_code'] 
    list_editable = ['postal_code']
    search_fields = ['description']
    list_per_page = 5

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname', 'user_id', 'email', 'address']
    search_fields = ['name', 'user_id']
    list_per_page = 10