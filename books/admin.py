from django.contrib import admin
from .models import Books, Employees

@admin.register(Books)
class BookAdmin(admin.ModelAdmin):
    list_display = ('creat_at', 'actualized_at', 'active', 'title', 'url')

@admin.register(Employees)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('creat_at', 'actualized_at', 'active', 'book', 'name', 'email', 'business_unity', 'type_function')
