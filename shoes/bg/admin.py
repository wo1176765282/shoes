from django.contrib import admin
from .models import User,Shoes
# Register your models here.
from django.contrib.admin import AdminSite
AdminSite.site_header = "鞋子管理"

@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ['name', 'phone', 'size', 'color']
