from django.contrib import admin
from .models import CrudUser

# Register your models here.
@admin.register(CrudUser)

class CrudUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'age']
